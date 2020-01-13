from blueprints import db,app, internal_required, supplier_required, pembeli_required
from flask_jwt_extended import jwt_required, get_jwt_claims
from flask import Blueprint
from flask_restful import Api, reqparse, Resource, marshal, inputs
from sqlalchemy import desc
from .model import Products

bp_product = Blueprint('product', __name__)
api = Api(bp_product)

class ProductList(Resource):
    def __init__(self):
        pass
    
    #Get all listed product
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('p', type=int, location='args', default=1)
        parser.add_argument('rp', type=int, location='args', default=25)
        parser.add_argument('nama_produk', location='args')
        parser.add_argument('brand', location='args')
        parser.add_argument('lokasi_kota', location='args')
        parser.add_argument('persen_discount', location='args')
        parser.add_argument('gratis_ongkir', location='args')
        parser.add_argument('orderby', location='args', help='invalid order value', choices=('persen_discount', 'harga'))
        parser.add_argument('sort', location='args', help='invalid sort value', choices=('desc','asc'))

        args = parser.parse_args()

        offset = (args['p']*args['rp'])-args['rp']

        qry = Products.query

        if args['nama_produk'] is not None:
            qry = qry.filter(Products.nama_produk.like('%'+args['nama_produk']+'%'))

        if args['brand'] is not None:
            qry = qry.filter_by(brand=args['brand'])
        
        if args['lokasi_kota'] is not None:
            qry = qry.filter_by(lokasi_kota=args['lokasi_kota'])
        
        if args['persen_discount'] is not None:
            qry = qry.filter_by(persen_discount=args['persen_discount'])
        
        if args['gratis_ongkir'] is not None:
            qry = qry.filter_by(gratis_ongkir=args['gratis_ongkir'])

        if args['orderby'] is not None:
            if args['orderby'] =='persen_discount':
                if args['sort'] == 'desc':
                    qry = qry.order_by(desc(Products.persen_discount))
                else:
                    qry = qry.order_by(Products.persen_discount)
            elif args['orderby'] =='harga':
                if args['sort'] == 'desc':
                    qry = qry.order_by(desc(Products.harga))
                else:
                    qry = qry.order_by(Products.harga)

        rows = []
        for row in qry.limit(args['rp']).offset(offset).all():
            rows.append(marshal(row, Products.response_fields))
        
        return rows, 200

class ProductResource(Resource):
    def __init__(self):
        pass
    
    #get product with specific id (detail product page)
    def get(self, id):
        qry = Products.query.get(id)
        if qry is not None:
            return marshal(qry, Products.response_fields), 200
        return {'status': 'NOT_FOUND'}, 404

class ProductSupplierResource(Resource):

    #Tambah product baru oleh setiap supplier
    @jwt_required
    @supplier_required
    def post(self):
        claim = get_jwt_claims()
        parser = reqparse.RequestParser()
        parser.add_argument('nama_produk', location='json', required=True)
        parser.add_argument('kategori', location='json', required=True)
        parser.add_argument('brand', location='json', required=True)
        parser.add_argument('harga', type=int, location='json', required=True)
        parser.add_argument('lokasi_kota', location='json', required=True)
        parser.add_argument('harga_awal', type=int, location='json')
        parser.add_argument('persen_discount', location='json')
        parser.add_argument('deskirpsi_produk', location='json', required=True)
        parser.add_argument('gratis_ongkir', type=bool, location='json', required=True)
        parser.add_argument('nama_supplier', location='json', required=True)

        args = parser.parse_args()

        Product = Products(args['nama_produk'], args['kategori'], args['brand'], args['harga'], args['lokasi_kota'], args['harga_awal'], args['persen_discount'], args['deskirpsi_produk'], args['gratis_ongkir'], claim['id'], args['nama_supplier']) 
        db.session.add(Product)
        db.session.commit()

        app.logger.debug('DEBUG : %s', Product)

        return marshal(Product, Products.response_fields), 200, {'Content-Type':'application/json'}

    #Update product oleh supplier dengan specific id
    @jwt_required
    @supplier_required
    def put(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument('nama_produk', location='json', required=True)
        parser.add_argument('kategori', location='json', required=True)
        parser.add_argument('brand', location='json', required=True)
        parser.add_argument('harga', type=int, location='json', required=True)
        parser.add_argument('lokasi_kota', location='json', required=True)
        parser.add_argument('harga_awal', type=int, location='json')
        parser.add_argument('persen_discount', location='json')
        parser.add_argument('deskirpsi_produk', location='json', required=True)
        parser.add_argument('gratis_ongkir', type=bool, location='json', required=True)
        parser.add_argument('nama_supplier', location='json', required=True)

        args = parser.parse_args()

        claim = get_jwt_claims()
        qry = Products.query.get(id)
        if claim['id'] == qry.client_id :
            if qry is None:
                return {'status': 'NOT_FOUND'}, 404
            
            qry.nama_produk = args['nama_produk']
            qry.kategori = args['kategori']
            qry.brand = args['brand']
            qry.harga = args['harga']
            qry.lokasi_kota = args['lokasi_kota']
            qry.harga_awal = args['harga_awal']
            qry.persen_discount = args['persen_discount']
            qry.deskirpsi_produk = args['deskirpsi_produk']
            qry.gratis_ongkir = args['gratis_ongkir']
            db.session.commit()

            return marshal(qry, Products.response_fields), 200, {'Content-Type':'application/json'}
        
api.add_resource(ProductList, '/list')
api.add_resource(ProductResource,'/<id>')
api.add_resource(ProductSupplierResource,'/supplier','/supplier/<id>')


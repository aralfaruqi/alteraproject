from flask_restful import Api
from blueprints import app, manager
import sys, logging
from logging.handlers import RotatingFileHandler
from werkzeug.contrib.cache import SimpleCache

cache = SimpleCache()

api = Api(app, catch_all_404s = True)
    
if __name__ =='__main__':
    try:
        if sys.argv[1] == 'db':
            manager.run()
            sys.exit()
    except Exception as e:
        formatter = logging.Formatter("[%(asctime)s]{%(pathname)s:%(lineno)d} %(levelname)s -%(message)s")
        log_handler = RotatingFileHandler("%s/%s" %(app.root_path, '../storage/log/app.log'), maxBytes=10000000, backupCount=10)
        
        logging.getLogger().setLevel('INFO')
        log_handler.setFormatter(formatter)
        app.logger.addHandler(log_handler)
        app.run(debug=True, host='0.0.0.0', port=5000 )
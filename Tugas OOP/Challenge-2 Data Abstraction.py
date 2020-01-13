class Calculator:
    def run(self):
        print(self.heading())
        print("1: Open calculator"+"\n"+
        "99: Exit"+"\n"+
        "Masukkan pilihan anda: ")
        self.input0 = input()

        if self.input0 == '1':
            return self.masukan_value()
        elif self.input0 == '99':
            print('Bye')

    def heading(self):
        return "+++++++++++++CALCULATOR+++++++++++++"
    
    def masukan_value(self):
        print(self.heading())
        self.value1 = input("Masukan Value 1 : ")
        self.value2 = input("Masukan value 2 : ")
        return self.calculation_operation(self.value1,self.value2)
    
    def calculation_operation(self,value1=None,value2=None):
        print(self.heading())
        print("Please Enter Calculation Operation: "+"\n"+
        "1. Add value"+"\n"+
        "2. Sub value"+"\n"+
        "3. Multiply Value"+"\n"+
        "4. Divide Value")

        self.value1 = value1
        self.value2 = value2

        print(self.heading())
        self.input1 = input("Pilihan Anda : ")
        if self.input1 == '1':
            return self.add_value(self.value1,self.value2)
        elif self.input1 == '2':
            return self.sub_value(self.value1,self.value2)
        elif self.input1 == '3' :
            return self.multiply_value(self.value1,self.value2)
        elif self.input1 == '4' :
            return self.divide_value(self.value1,self.value2)
    
    def add_value(self,value1=None,value2=None):
        print(int(value1)+int(value2))
        
    def sub_value(self,value1=None,value2=None):
        print(int(value1)-int(value2))

    def multiply_value(self,value1=None,value2=None):
        print(int(value1)*int(value2))

    def divide_value(self,value1=None,value2=None):
        print(int(value1)/int(value2))

calculator = Calculator()
calculator.run()
    



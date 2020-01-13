def x_and_o(kata): 
    count_x = kata.count("x") 
    count_o = kata.count("o") 
    
    if count_x == count_o: 
        print("true") 
    else : 
        print("false")

x_and_o("xoxoxo")
x_and_o("oxooxo")
x_and_o("oxo")
x_and_o("xxxooo")
x_and_o("xoxooxxo")
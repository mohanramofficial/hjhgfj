import time
error=True
n=0
while n!=1:
    print"***Welcome to the Bin2Dec Converter.***\n"
    while error:
        try:
            bin2dec =raw_input("Please enter a binary number: ")
            error=False
        except NameError: 
            print"Enter a Binary number. Please try again.\n"
            time.sleep(0.5)
        except SyntaxError: 
            print"Enter a Binary number. Please try again.\n"
            time.sleep(0.5)


        #converts bin2dec
        decnum = 0 
        for i in bin2dec: 
            decnum = decnum * 2 + int(i)
            time.sleep(0.25)
        print decnum, "<<This is your answer.\n" #prints output
        hgf

def main():
    dadash()
    
def num1():
    while True:
        try: 
            first =int(input("First number?  ")) 
            return first
        except ValueError:
            print("Please enter a number")
            
def num2():
    while True:
        try: 
            second = int(input("Second number?  ")) 
            return second
        except ValueError:
            print("Please enter a number")
            
def symboll():
    while True:
        try: 
            symboll = input("choose a symbol ( + - / *)  ") 
            if symboll == "+":
                return symboll
            elif symboll == "-":
                return symboll
            elif symboll == "*":
                return symboll
            elif symboll == "/":
                return symboll
            else:
                print("Please enter a symbol")
        except ValueError:
            print("Please enter a symbol")

def dadash():
     fff = num1()
     soran = symboll()
     sss =num2()
     
     if soran == "+":
        print(fff + sss)
     elif soran == "-":
        print(fff - sss)
     elif soran == "*":
        print(fff * sss)
     elif soran == "/":
        print(fff / sss)


       


 
main()
"""
try:
    x = int(input("what is x? "))
    print(f"x is {x}")
except ValueError:
    print("x is not a number")  """
# print(f"x is {x}")  agar aa la xure except bnuse la rasty try  awa NameError ada
"""
try:
    x = int(input("what is x? "))
    
except ValueError:
    print("x is not a number") 
else:
    print(f"x is {x}")    
"""
"""
while True:
    try:
      x = int(input("what is x? "))
      ## atwane else la bdae break beneta era
    except ValueError:
       print( " x is not a number")
    else:
       break

print(f"x is {x}")    #agar la je break printaka bnusen awa prsearaka qat tawaw nabe


    """
"""
def main():
    x = git_int()
    print(f"x is {x}")

def git_int():
    while True:
        try:
          x = int(input("what is x? "))
        except ValueError:
          print( " x is not a number")
        else:
           return x    # atwane la jee return break bnuse return beneta xuarawa raste while

main()
"""

# def main():
#     x = git_int("what is x? ")
#     print(f"x is {x}")

# def git_int(prompt):
#     while True:
#         try:
#           return int(input(prompt))
#         except ValueError:
#           pass
          
        
# main()
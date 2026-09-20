try:
    num = int(input("Enter a number"))
    result = 100/num
    print(f"Result = {result}")

except ZeroDivisionError:
    print("Cannot div by zero")

except (ValueError, TypeError) as e:
    print(f"Error ={e}")
    print(f"Type ={type(e)}")
    
except:
    print ("Some error occured")

else:
    print("Done")
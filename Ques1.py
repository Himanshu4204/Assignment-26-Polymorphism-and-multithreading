#1. Write a python script to multiple 2 or 3 or 4 numbers with a single multiply method in a class using method overloading.?
class overloading:
    def multiply(self,a,b=None,c=None):
        if b is not None and c is not None:
            return a*b*c
        elif b is not None:
            return a*b
        else:
            return a
Obj=overloading()
print("Multiply is :",Obj.multiply(2))
print("Multiply is :",Obj.multiply(2,3))
print("Multiply is :",Obj.multiply(2,3,4))





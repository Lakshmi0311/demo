class Calculator():
   def __init__(self,a,b) -> None:
    self.x=a
    self.y=b
   def addition(self):
    return self.x+self.y
   def sub(self):
    return self.x-self.y
obj=Calculator(3,6)
print('adding values',obj.addition())
print(obj.sub())
class Complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img

    def show(self):
        print(self.real , "i +", self.img , "j")

    def __add__(self,num2):
        newreal = self.real + num2.real
        newimg = self.img + num2.img
        return Complex(newreal , newimg)
    
    def __mul__(self,num2):
        newreal = self.real * num2.real
        newimg = self.img * num2.img
        return Complex(newreal , newimg)
    
num1 = Complex(9,8)
num1.show()

num2 = Complex(6,3)
num2.show()

num3 = num1 + num2
num3.show()
num3 = num1 * num2
num3.show()


        


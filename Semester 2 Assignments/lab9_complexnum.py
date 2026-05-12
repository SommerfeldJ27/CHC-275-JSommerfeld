class complex:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    
    
    def __add__(self, other):
        return complex(self.a + other.a, self.b + other.b)
    
    def __sub__(self, other):
        return complex(self.a - other.a, self.b - other.b)
    
    def __mul__(self, other):
        return complex(self.a * other.a - self.b * other.b,
                       self.a * other.b + self.b + other.a)
    
    def __str__(self):
        if self.b > 0:
            return f"{self.a}+{self.b}i"
        elif self.b < 0:
            return f"{self.a}{self.b}i"
    def conj(self):
       return complex(self.a, -self.b)

def main():
    num1 = complex(5,4)
    num2 = complex(3,2)
    print("addition")
    print(num1+num2)
    print("subtraction")
    print(num1-num2)
    print("multiplication")
    print(num1*num2)
    print("conjugate")
    print(num1.conj())
    print(num2.conj())
    
if __name__ == "__main__":
    main()
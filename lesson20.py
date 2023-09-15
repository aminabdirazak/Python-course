class Calculate:  
    def getValue(self):
        global n1,n2;
        n1=int(input("Enter number : "))
        n2=int(input("Enter number : "))
    def __init__(self):
        print("kani waa constructor")

class Child(Calculate):
        def show(self):
            total=n1+n2;
            print("Total is: ",total)

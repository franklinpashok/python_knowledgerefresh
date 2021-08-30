#
# Example file for working with classes
#
class myClass():
    def method1(self):
        print("myclass method1")
    
    def method2(self, somestring):
        print("myclass method2 " + somestring)

# inherit from the above class
class anotherClass(myClass):
    def method1(self):
#below syntax is calling the method from another class as we inherited the class in the another class
        myClass.method1(self)
        print("anotherClass method1")
    
    def method2(self, somestring):
        print("anotherClass method2 ")

def main():
    c = myClass()
    c.method1()
    c.method2("this is a string")

    c2 = anotherClass()
    c2.method1()
    c2.method2("anotherclass string")

if __name__ == "__main__":
    main()
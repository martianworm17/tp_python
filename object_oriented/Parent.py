class Parent:   # Define parent class
    
    parentAttr = 100
    
    def __init__(self):
        print "Calling parent constructor"
        
    def parentMethod(self):
        print "Calling parent method"
        
    def setAttr(self, attr):
        Parent.parentAttr = attr
        
    def getAttr(self):
        print "Parent attribute :", Parent.parentAttr
        
    def awesomeMethod(self):
        print "This is awesome method from parent class."
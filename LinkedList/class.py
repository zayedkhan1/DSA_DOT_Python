class Cookie:
# constructor
    def __init__(self,color):
        self.color=color
    # getter and setter methods
    def get_color(self):
        return self.color
    def set_color(self,color):
        self.color=color
    # destructor
cookie_1=Cookie('green')
cookie_2=Cookie('blue')

# accessing the attributes using getter methods
print("first one color",cookie_1.get_color())
print("second one color",cookie_2.get_color())

# modifying the attribute using setter method
cookie_1.set_color('red')
cookie_2.set_color('yellow')

# accessing the attributes again using getter methods
print("\n first one color",cookie_1.get_color())
print(" second one color",cookie_2.get_color())

# another example with gun class
class Gun:
    def __init__(self,model,color):
        self.model=model
        self.color=color
    def get_model(self):
        return self.model
    def set_model(self,model):
        self.model=model    
    def get_color(self):
        return self.color
    def set_color(self,color):
        self.color=color

gun_1=Gun('AK-47','black')
print("\n Gun model:",gun_1.get_model(),gun_1.get_color())

gun_1.set_model('M-16')
gun_1.set_color('green')

print(" Gun model:",gun_1.get_model(),gun_1.get_color())
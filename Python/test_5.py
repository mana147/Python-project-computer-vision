class InOutString (object):

    def __init__ (self):
        self.s = ""

    def getString(self, t):
        self.s = t
    
    def outString(self) :
        t = self.s.upper()
        print (t)
#----------------------------------

t = input ("nhap ten vao day : ")

text = InOutString()
text.getString(t) 
text.outString()
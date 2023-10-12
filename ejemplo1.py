class User:

    name=None
    email=None

    #metodo de enviar correo
    def send_email(self):
        if self.email is not None:
            print("sending email}:"+self.email)
        else:
            print("error")

    def _str_(self):
        return "User: "+self.name+", "+self.email            
        
    #constructor 
    def _init_(self,name,email):
        self.name=name
        self.email=email

class Student(User):
    def _init_(self, name, email, score):
        super()._init_(name, email)
        self.score = score

    def _str_(self):
        return "Student: "+self.name+", "+self.email+", Score: "+str(self.score)  

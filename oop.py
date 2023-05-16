class student:
    def __init__(self,name,sex,age):
        self.name=name
        self.age=age
        self.sex=sex
    def info(self):
        print(self.name,self.sex,self.age)
aman=student("Asif","Male",24)
aman.info()
shohag=student("Shohag","Male",21)
shohag.info()
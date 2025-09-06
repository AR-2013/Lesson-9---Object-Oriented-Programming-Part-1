class student:
    grade = "graduated already"
    name = "Srileka"

    def introduction(self):
        print("Hi I am a teacher.")
    
    def details(self):
        print("My name is", self.name,".")
        print("My grade is", self.grade,".")

ob = student()
ob.introduction()
ob.details()
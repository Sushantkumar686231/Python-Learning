class Students:
    def __init__(self,name,age,grade,city):
        self.name=name
        self.age=age
        self.grade=grade
        self.city=city
    
    def display_info(self):
        print("Name :" ,{self.name})
        print("Age :" ,{self.age})
        print("Grade :" ,{self.grade})
        print("CIty :" ,{self.city})

s1=Students("Sushant",24,"A+","Delhi")
s2=Students("Prerane",24,"B+","Karnataka")


object_list=[]
object_list.append(s1)
object_list.append(s2)

for i in object_list:
    i.display_info()
    print("-----------------")
class Student_Attendance:
    def __int__(self,list,name,roll_no,dict1):
        self.list=list
        self.name=name
        self.roll_no=roll_no
        self.dict1=dict1
    def attendence_list(self):
        self.list=list(input("Name of Attendees: ").lower().split())
        self.roll_no=list(input("Enter roll no: ").split())
        self.dict1=dict(zip(self.roll_no,self.list))
        print("Name  | Roll")
        print("---------------")
        for i in self.dict1:
            print(self.dict1[i]," ",i)
    def Show_result(self):
        for i in self.dict1:
            if (n in self.dict1[i]):
                print("---",n, "is present and Roll_Number of",n,"is",i,"---")
                break
        else:
            print("---",n,"is not present...!")
s1=Student_Attendance()
s1.attendence_list()
n=input("Enter name to check: ").lower()
s1.Show_result()
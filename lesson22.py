class Files:
    def writeStudentInfo(self,name,tell,add):
        f=open("student.txt","a")
        text=name+" "+tell+" "+add
        f.write(text)
        f.close()
        print("data is saved success")
    def showInfo(self):
        f=open("student.txt","r")
        print(f.read())

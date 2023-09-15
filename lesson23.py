import lesson22 as les
ob=les.Files()
magac=input("Enter name: ")
tel=input("Enter tell: ")
add=input("Enter address: ")

ob.writeStudentInfo(magac,tel,add);
ob.showInfo()

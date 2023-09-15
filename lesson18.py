student={
    "id":"611",
    "Name":"maryan",
    "Tell":"79911",
    "Address":"Waaberi"
    }
print(student["Tell"])
print(student.get("Name"))

index=student.keys();
for i in index:
    print(i)

print("--------------------------------")
for i in index:
    print(i," =",student.get(i))

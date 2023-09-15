person=[
        ["ahmed","6889","kaaran"],
        ["maryan","1234","hodon"],
        ["Geedi","98756","shangaani"],
        ["socdaal","1232","shibis"]
    ]
#for a in range(0,len(person)):
#    print("Name: ",person[a][0]," Tell: ",person[a][1]," Address: ",person[a][2])


for row in person:
    for value in row:
        print(value,end="\t")
    print()

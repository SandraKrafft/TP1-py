def syracuse(entier):
    while entier != 1:
        print(entier)
        if entier % 2 == 0:
            entier = entier/2
        else:
            entier = entier*3+1
   


entier = int(input())
syracuse(entier)
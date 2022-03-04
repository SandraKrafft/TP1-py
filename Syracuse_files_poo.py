CFd = "text.txt"
CRd = "result.txt"

def syracuse(entier, fw):
    with open(fw,'w') as f:
        while entier != 1:
            f.write(str(entier))
            f.write("\n")
            if entier % 2 == 0:
                entier = entier/2
            else:
                entier = entier*3+1
   


with open(CFd, 'r') as f:
        entier = f.readlines()
        entier = ''.join(entier)
        new = int(entier)


syracuse(new,CRd)
     
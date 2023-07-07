f = open('requirements.txt', 'r')
new_req = open('req.txt', 'w')
Lines = f.readlines()
for l in Lines:
    new_req.writelines(l.split("==",1)[0] + "\n")




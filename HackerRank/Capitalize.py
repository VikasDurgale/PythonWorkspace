string = "132 456 Wq  m e"
mylist = string.split(' ')
print(mylist)
for i in range(len(mylist)):
    mylist[i] = mylist[i].capitalize()

print(" ".join(mylist))
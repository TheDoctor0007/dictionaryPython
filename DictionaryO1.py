'''
@author: Parth Mistry
'''
    
def insert(x):
    mydct[x] = x

def search(x):
    if mydct[x] == x:
        return mydct[x]
    return "not found"

def delete(x):
    mydct[x] = 0
    
list = [6,1,3,5,10,9]
n = max(list)+1
mydct = [0]*n
#print(mydct)
#print(len(list))
for i in list:
    insert(i)
print(mydct)
while(True):
    choice = input("What would you like to do? insert/delete/search/quit:\n")
    if choice == "insert":
        num = input("Please enter a number:\n")
        num = int(num)
        for n in range(len(mydct), num+1):
            mydct.append(0)
        insert(num)
        print(mydct)
    if choice == "search":
        num = input("Please enter a number:\n")
        num = int(num)
        res = search(num)
        print(res)
    if choice == "delete":
        num = input("Please enter a number:\n")
        num = int(num)
        delete(num)
        print(mydct)
    if choice == "quit":
        exit(0)

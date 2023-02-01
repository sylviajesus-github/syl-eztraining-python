#iterate 10 numbers and print for every iteration sum of
#that number and its previous number
s=0
for i in range(10):
    s=i+(i-1)
    print("For :",i," :",s)

#catch - try do it as for 0 previous number is 0

#print characters from string at even index
s="jesus christ"
x=list(s)
print(x)

for i in x:
    if s.index(i)%2==0:
        print(i)
#catch - two words shud be considered as one string

#REMOVE FIRST N characters from a string
my_string="charley Benjamin"
n=4
my_string.remove[:4]
print(my_string)










#the code below takes a string and checks whether its a palindrome or not!
if len(string)%2==0:
    print("NO")

else:
    for i in range(0,len(string)):
           if string[i]==string[len(string)-1-i]:
                 count+=1
    if count==len(string):
       print("YES")
    else:
       print("NO")
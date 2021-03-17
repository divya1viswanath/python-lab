dict={}
str1=input("Enter a string:")
for n in str1:
    keys=dict.keys()
    if n in keys:
        dict[n]+=1
    else:
        dict[n]=1
        print("Character Frequency")
    for k,v in dict.iems():
        print(k,v)

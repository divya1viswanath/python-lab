lis=input("Enter a list with some strings(space seperated):")
words_list=lis.split()
words_len=[]
for n in words_list:
    words_len.append((len(n),n))
    print(words_len)
    words_len.sort()
    print(words_len)
print("longest word:",words_len[-1][1])

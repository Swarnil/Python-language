def wordcount(n):
    s = len(n)
    count = 1
    for i in range(0,s):
        if (n[i] == ' ' or n[i] == '\n' or n[i] == '\t'):
            count = count+1
    return count

n = input("Enter the Sentence: ")
s = wordcount(n)
print("The number of words are: ", s)        




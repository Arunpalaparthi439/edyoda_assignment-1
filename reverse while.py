word ="Edyoda"
print("the original word is:", word)
reverse_word =""
count = len(word)
while count>0:
    reverse_word += word[count-1]
    count = count-1
print("the reverse word is:" ,reverse_word)

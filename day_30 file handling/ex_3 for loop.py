text_file = open('user.txt','w')

word_list= []

for i in range (1 ,8):
    print("Please enter data: ")
    line = input()
    word_list.append(line)

text_file.writelines(word_list)

text_file.close()


file = open("test.txt","w")
file.write("Text is wrapped in a way that best balances the number of characters on each line, enhancing layout quality and legibility. Because counting characters and balancing them across multiple lines is computationally expensive, this value is only supported for blocks of text spanning a limited number of lines (the Chromium implementation uses six wrapped lines or less), meaning that it is useful for cases such as headings or pull quotes.")
file.close()
file = open("test.txt").read()
for elem in file:
    print(elem)
"""
Write a function, that receives the path to a text file that contains JUST ONE word
per line, and returns a dictionary with the counter of words starting with each
letter from 'a' to 'z'.
"""




f = open('words.txt', 'r')
letter = {}
for line in f:
    letter.setdefault(line[0], 0)
    letter[line[0]] += 1
f.close()


print(letter)
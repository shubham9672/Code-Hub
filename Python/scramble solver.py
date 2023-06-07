import enchant
import itertools

word=input("Enter the scramble: ")
t=list(itertools.permutations(word,len(word)))
for i in range(0,len(t)):
    word_test = (''.join(t[i]))
    d = enchant.Dict("en_US")
    word_res = d.check(word_test)

    if word_res == True:
        print(word_test)





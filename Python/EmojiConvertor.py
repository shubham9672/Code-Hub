msg=input("> ")
words=msg.split(' ')
emojies={
    ":)" : "😃",
    ":(" : "😞"
}
output=""
for i in words:
    output+=emojies.get(i,i)+" "
print(output)
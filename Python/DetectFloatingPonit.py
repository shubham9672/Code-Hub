from re import match, compile

pattern = compile('^[-+]?\d*\.\d+$')
for i in range(int(input())):
    print(bool(pattern.match(input())))
function detectfloatnum():
    pattern = compile('^[-+]?\d*\.\d+$')
    for i in range(int(input())):
        print(bool(pattern.match(input())))

detectfloatnum()        

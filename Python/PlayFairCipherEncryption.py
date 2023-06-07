plainText=[]
keyMatrix = []
cipherTextList =[]
def index_2d(keyMatrix, v):
    for i, x in enumerate(keyMatrix):
        if v in x:
            return [i, x.index(v)]
def keyMatrixGeneration(keyMatrix,reducedAlphabet):
    alphacounter = 0 
    alpha = len(reducedAlphabet)
    #print(alpha,'[alpha]')
    while alphacounter < alpha and len(reducedAlphabet[alphacounter:alphacounter+5]) :
         tempReducedAlphabet = []
         #print(reducedAlphabet[0:5],'[reducedAlphabet temp]')
         tempReducedAlphabet.append(reducedAlphabet[alphacounter:alphacounter+5])
         alphacounter+=5
         keyMatrix.extend(tempReducedAlphabet)
    if alphacounter > alpha and len(reducedAlphabet[alphacounter-5:]):
         tempReducedAlphabet = []
         tempReducedAlphabet.append(reducedAlphabet[alphacounter-5:])
         keyMatrix.append(tempReducedAlphabet)
    return keyMatrix
def playFairCipher(plainText,key):
    # create key matrix
    #print(key,'[key]')
    #print('[playFairCipher def]')
    cipherText = ''
    keyList = list(key.strip(' '))
    keyListSet = set(keyList)  # use this to find difference in alphabet and key
    reducedKeyList = []
    for ch in keyList:
        if ch not in reducedKeyList:
            reducedKeyList.append(ch)
    tempKey = []
    #print(keyListSet,reducedKeyList)
    
    k = len(reducedKeyList)
    counter = 0
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    alphabetSet = set(alphabet)
    keycount = 5
    #print(k)
    if k==5:
       #print('k==5')
       keyMatrix.append(reducedKeyList[0:5])
    elif k>5:
       while keycount<=k:
            
            keyMatrix.append(reducedKeyList[keycount-5:keycount])
            keycount+=5
       if keycount > k:
                keyMatrix.append(reducedKeyList[keycount-5:])
       
    else:
       keyMatrix.append(reducedKeyList)
        
    print(keyMatrix,'[before keyMatrix]')    
    reducedAlphabetSet = alphabetSet-keyListSet
    #print(reducedAlphabetSet,'[reducedAlphabetSet]')
    reducedAlphabet = list(reducedAlphabetSet)
    reducedAlphabet.sort()
    #print(reducedAlphabet,'[reducedAlphabet list]')
    if 'i'and 'j' in reducedAlphabet:
        reducedAlphabet.remove('j')
    if 'i' not in reducedAlphabet and 'j' not in reducedAlphabet:
        ind = index_2d(keyMatrix,'j')
        print(ind,keyMatrix[ind[0]][ind[1]])
        keyMatrix[ind[0]].remove(keyMatrix[ind[0]][ind[1]])
    lengthCheck = False
    keyN = 0
    # generation of key matrix
    for i in range(0,len(keyMatrix)):
        if len(keyMatrix[i])<5:
            lengthCheck=True
            keyN = i
    if lengthCheck==True:
         tempReducedAlphabet = []
         tempReducedAlphabet.extend(reducedAlphabet[0:5-len(keyMatrix[keyN])])
         #print(tempReducedAlphabet,'[tempReducedAlphabet]')
         keyMatrix[keyN].extend(tempReducedAlphabet) 
         for i in tempReducedAlphabet:
             reducedAlphabet.remove(i)
         #print(reducedAlphabet,'[reducedAlphabet]')
         keyMatrixGeneration(keyMatrix,reducedAlphabet)
    else:
         keyMatrixGeneration(keyMatrix,reducedAlphabet)
    print(keyMatrix,'[keymatrix]')
    # matching plainText with key matrix
    for i in range(0,len(plainText)):
        first=[]
        second=[]
        first.extend(index_2d(keyMatrix,plainText[i][0]))
        second.extend(index_2d(keyMatrix,plainText[i][1]))
        if first[0]!=second[0] and first[1]!=second[1]:
            cipherText += keyMatrix[first[0]][second[1]]+ keyMatrix[second[0]][first[1]]
        elif first[0]==second[0]:
            if first[1]+1<len(keyMatrix[first[0]]):
               cipherText+=keyMatrix[first[0]][first[1]+1]
            else:
               cipherText+=keyMatrix[first[0]][0]
            if second[1]+1<len(keyMatrix[second[0]]):
               cipherText+=keyMatrix[first[0]][second[1]+1]
            else:
               cipherText+=keyMatrix[first[0]][0]
        else:
            if first[0]+1<len(keyMatrix):
               cipherText+=keyMatrix[first[0]+1][first[1]]
            else:
               cipherText+=keyMatrix[0][first[1]]
            if second[0]+1<len(keyMatrix):
               cipherText+=keyMatrix[second[0]+1][second[1]]
            else:
               cipherText+=keyMatrix[0][second[1]]
             
        #print(first,'[first]')
    print(cipherText,'[cipherText]')
    return cipherText
def plainTextConversion(s,key):
    
    i = 0
   
    sList = list(s.strip())
    n = len(sList)
    while(n>0):
       temp=[]
       checkSame=False
       #print(sList,'sList')
       for j in range(0,2):
           if j<len(sList) and sList[j] not in temp :
              temp.append(sList[j])
              checkSame = False
           elif j<len(sList) and sList[j] in temp :
              temp.append('x')
              checkSame = True
           else:
               checkSame = False
               continue
       #print(temp,'temp')
       sList.remove(sList[0])
      # print(checkSame)
       if len(temp)>1 and checkSame == False:
          sList.remove(sList[0])
          plainText.append(temp)
          n=n-2
       elif len(temp)>1 and checkSame == True:
           #do noting
          plainText.append(temp)
          n=n-1
       elif len(temp)<1 and checkSame == True:
           # do nothing
          plainText.append(temp) 
       else:
          temp.append('x')
          plainText.append(temp)
          n=n-2
          
      
       #print(n,'n')
       
       #print(plainText,'plainText')  
        
    print(plainText,'final')
    res = playFairCipher(plainText,key)
    return res
    
if  __name__ == '__main__':
s = input ('enter plainText : ')
  key = input('enter key text : ')
  s = ''.join(s.split())
  key = ''.join(key.split())
  print(s,'[s]')
  result = plainTextConversion(s,key) 
  print (result)
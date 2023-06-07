def generateKey(text, key): 
  key = list(key) 
  if len(text) == len(key): 
    return(key) 
  else: 
    for i in range(len(text) -len(key)): 
      key.append(key[i % len(key)]) 
  return("" . join(key)) 
  
def encryption(text, key): 
  encrypt_text = [] 
  for i in range(len(text)): 
    x = (ord(string[i]) +ord(key[i])) % 26
    x += ord('A') 
    encrypt_text.append(chr(x)) 
  return("" . join(encrypt_text)) 
def decryption(encrypt_text, key): 
  orig_text = [] 
  for i in range(len(encrypt_text)): 
    x = (ord(encrypt_text[i]) -ord(key[i]) + 26) % 26
    x += ord('A') 
    orig_text.append(chr(x)) 
  return("" . join(orig_text)) 
if __name__ == "__main__": 
  string = input("Enter the text: ")
  keyword = input("Enter the key: ")
  key = generateKey(string, keyword) 
  encrypt_text = encryption(string,key) 
  print("Encryption:", encrypt_text) 
  print("Decryption:", decryption(encrypt_text, key)) 

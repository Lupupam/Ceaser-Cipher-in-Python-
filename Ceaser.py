
#CAESER CIPHER SINGLE ROUND / TAMPER / DOUBLE ROUND-- PROGRAM BY HEM BHATT--


import sys

strs = 'abcdefghijklmnopqrstuvwxyz' # Used this string and used its index values to shift lowercase alphabets. ( Seemed easier than using ASCCII values since our functions only take english as input)
strs2= 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' #Using this string for upper case alphabets

def main():                                                  # Main function used to call other functions        
    
    
         
   inp = raw_input('Input Plain-text for single round encryption here: ')
   key= int(input('Whats the key (Enter Any Numerical Value):'))
   direction = raw_input('Enter Direction here (Enter left or right):')
   encrypt(inp,key,direction)                                                    #Encrypt function is called here
   inpt = raw_input('Input The CipherText that needs to be tampered: ')
   tamper(inpt)                                                  #Tamper function is called here
   inpd = raw_input('Input Cipher-text for single round decryption here: ')
   keyd= int(input('Whats the key:'))
   directiond = raw_input('Enter Key Direction here: ')
   decrypt(inpd,keyd,directiond)                                                 #Decrypt function is called here
   inp2 = raw_input('Input Plain text for two round-encryption here: ')
   key1= int(input('Whats the key number 1 (Enter Any Numerical Value):'))
   direction1 = raw_input('Enter Direction for key-1 here (Enter left or right):')
   key2= int(input('Whats the key number 2 (Enter Any Numerical Value):'))
   direction2 = raw_input('Enter Direction for key-2 here (Enter left or right):')
   doubleencrypt(inp2,key1,direction1,key2,direction2)                                    #Double-encrypt function is called here
   inp2d = raw_input('Input Cipher text for two round-encryption here: ')
   key1d= int(input('Whats the key number 1 (Enter Any Numerical Value):'))
   direction1d = raw_input('Enter Direction for key number 1 here (Enter left or right):')
   key2d= int(input('Whats the key 2 (Enter Any Numerical Value):'))
   direction2d = raw_input('Enter Direction for key number 2 here (Enter left or right):')
   doubledecrypt(inp2d,key1d,direction1d,key2d,direction2d)                                    #Double-decrypt function is called here
def encrypt(inp,key,direction):
    print "The number of characters in input is",len(inp)
    data = []  #array created to deal with spaces and alphabets in plaintext 
    y=len(inp)
    if (y >= 32):
       if direction == 'right':
        for i in inp:                     
          if i.strip() and i in strs:                 
            data.append(strs[(strs.index(i) + key) % 26]) # Modulo 26 is used to wrap around the 26 alphabets   
          elif i.strip() and i in strs2:
             data.append(strs2[(strs2.index(i) + key) % 26])
            
          else:
            data.append(i)
          
      
       elif direction == 'left':                           
         for i in inp:                     
           if i.strip() and i in strs:                 
               data.append(strs[(strs.index(i) - key) % 26])    
           elif i.strip() and i in strs2:
             data.append(strs2[(strs2.index(i) - key) % 26])
           else:
             data.append(i)
            
       else:
         y =raw_input("Please restart and enter left or right") #As required by the program
         sys.exit(0) 
         #execfile("homeworksecure.py")
        

       output = ''.join(data)                                     #Creating a string of the shifted index values
       

       print "Ciphertext is:",output
       return output
       
       
    else:
       print "Please restart the program and enter a string with atleast 32 characters"
       
       sys.exit(0)   
   

def tamper(inpt):
 l = map(int, ''.join([bin(ord(i)).lstrip('0b').rjust(8,'0') for i in inpt])) # Converting Ciphertext into an array of bits, each character is of 8 bits
 strr = ''.join(map(str, l)) 
 print "The BitString of the Encrypted text before Tamper is:",strr #Printing the bitstring
 for i in range(0,256):                                         # Bitflipping the 1st 256 array indices
   
    if l[i]==1:
       l[i]=0
    else:   
       l[i]=1
 
 str2=''.join(map(str,  l))
 print "Bit string of the Encrypted text after Tamper is:",str2
 s = "".join(chr(int("".join(map(str,l[i:i+8])),2)) for i in range(0,len(l),8)) # Converting the Bit array back into a character string
 print "The Tampered Ciphertext is:",s

 
 

 
 
          


    

def decrypt(inpd,keyd,directiond):
    
    data = []
    if directiond == 'right':
        for i in inpd:                     
          if i.strip() and i in strs:                 
              data.append(strs[(strs.index(i) - keyd) % 26])    
          elif i.strip() and i in strs2:
             data.append(strs2[(strs2.index(i) - keyd) % 26])
          else:
            data.append(i)           
      
    else:
        for i in inpd:                     
          if i.strip() and i in strs:                 
              data.append(strs[(strs.index(i) + keyd) % 26])    
          elif i.strip() and i in strs2:
             data.append(strs2[(strs2.index(i) + keyd) % 26])
          else:
            data.append(i)  
        



    output = ''.join(data)
    print "Plaintext is:",output
    return output


def doubleencrypt(inp2,key1,direction1,key2,direction2):
    
    
    data = []  #array created to deal with spaces in plaintext 
    data2 = []
    
    if direction1 == 'right':
       for i in inp2:                     
         if i.strip() and i in strs:                 
          data.append(strs[(strs.index(i) + key1) % 26]) # Modulo 26 is used to wrap around the 26 alphabets    
         elif i.strip() and i in strs2:
             data.append(strs2[(strs2.index(i) + key1) % 26])
         else:
          data.append(i)           
      
    elif direction1 == 'left':                           
       for i in inp2:                     
         if i.strip() and i in strs:                 
          data.append(strs[(strs.index(i) - key1) % 26])    
         elif i.strip() and i in strs2:
             data.append(strs2[(strs2.index(i) - key1) % 26])
         else:
          data.append(i)
       

    output1 = ''.join(data)
   
    if direction2 == 'right':
       for i in output1:                     
        if i.strip() and i in strs:                 
         data2.append(strs[(strs.index(i) + key2) % 26]) # Modulo 26 is used to wrap around the 26 alphabets    
        elif i.strip() and i in strs2:
             data2.append(strs2[(strs2.index(i) + key2) % 26])
        else:
         data2.append(i)           
      

    elif direction2 == 'left':                           
       for i in output1:                     
         if i.strip() and i in strs:                 
            data2.append(strs[(strs.index(i) - key2) % 26])    
         elif i.strip() and i in strs2:
             data2.append(strs2[(strs2.index(i) - key2) % 26])
         else:
            data2.append(i)
            
       
    output = ''.join(data2)   

    print "Two round Encrypted Ciphertext is",output
    return output
   
def doubledecrypt(inp2d,key1d,direction1d,key2d,direction2d):
    
    
    data = []  #array created to deal with spaces in plaintext 
    data2 = []
    
    if direction1d == 'right':
       for i in inp2d:                     
         if i.strip() and i in strs:                 
          data.append(strs[(strs.index(i) - key1d) % 26]) # Modulo 26 is used to wrap around the 26 alphabets    
         elif i.strip() and i in strs2:
             data.append(strs2[(strs2.index(i) - key1d) % 26])
         else:
          data.append(i)           
      
    elif direction1d == 'left':                           
       for i in inp2d:                     
         if i.strip() and i in strs:                 
          data.append(strs[(strs.index(i) + key1d) % 26])    
         elif i.strip() and i in strs2:
             data.append(strs2[(strs2.index(i) + key1d) % 26])
         else:
          data.append(i)
       

    output1 = ''.join(data)
   
    if direction2d == 'right':
       for i in output1:                     
        if i.strip() and i in strs:                 
         data2.append(strs[(strs.index(i) - key2d) % 26]) # Modulo 26 is used to wrap around the 26 alphabets    
        elif i.strip() and i in strs2:
             data2.append(strs2[(strs2.index(i) - key2d) % 26])
        else:
         data2.append(i)           
      

    elif direction2d == 'left':                           
       for i in output1:                     
         if i.strip() and i in strs:                 
            data2.append(strs[(strs.index(i) + key2d) % 26])    
         elif i.strip() and i in strs2:
             data2.append(strs2[(strs2.index(i) + key2d) % 26])
         else:
            data2.append(i)
            
       
    output = ''.join(data2)   

    print "Two round Decrypted Plaintext is",output
    return output       
  


main()                # Main function is called here

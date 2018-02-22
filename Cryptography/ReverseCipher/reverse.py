''' The Reverse Cipher is a simple encryption method 
 that encrypts a message by printing it in reverse
 order.
'''
userMessage = input("Enter a message you would like to encrypt using the Reverse Cipher: ")
userMessageEncrypted = ''
print("Good, You\'ve entered: ", userMessage)

i = len(userMessage) - 1
while i>= 0:
	userMessageEncrypted = userMessageEncrypted + userMessage[i]
	i = i - 1
print("Using Reverse Cipher Encryption, your message becomes: ", userMessageEncrypted)

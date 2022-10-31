#############################################################################
## 									   ##
##	Title : Caesar Cipher 						   ## 	
##									   ##
##	Author : Ernest Odhiambo Elnino					   ##
##									   ##
##	Github : https://github.com/ProtocolWhisperer01 		   ##
#############################################################################

# User a is expected to pick a mode between Encryption (1) or Decryption (2)

mode = (input("\nThis is a simple caesar cipher for encryption/decryption. Pick a mode 1 or 2 : ")) 

try:
	mode = int(mode)
	
	if mode == 1:
		message = input("Enter a phrase for encoding : ")
		key_pos = int(input("Enter a key for the encoding : "))
		print("Your encrypted is as below: \n")
	
		for i in message:
	
			if i.isupper(): 
				diff = ord(i) - ord('A')
				new_diff = (diff + key_pos) % 26
				new_pos = new_diff + ord('A')
				print(chr(new_pos), end="")
			 
			elif i.islower():
				diff = ord(i) - ord('a')
				new_diff = (diff + key_pos) % 26
				new_pos = new_diff + ord('a')
				print(chr(new_pos), end="")	
		
			elif i.isdigit():
				diff = ord(i) - ord('0')
				new_diff = (diff + key_pos) % 10
				new_pos = new_diff + ord('0')
				print(chr(new_pos), end="")
			else:
		
				print(i, end="")
	elif mode == 2:		
		message = input("Enter a phrase for decoding : ")
		key_pos = int(input("Enter a key for the decoding : "))
		print("Your decrypted is as below: \n")
	
		for i in message:
	
			if i.isupper(): 
				diff = ord(i) + ord('A')
				new_diff = (diff - key_pos) % 26
				new_pos = new_diff - ord('A')
				print(chr(new_pos), end="")
			 
			elif i.islower():
				diff = ord(i) + ord('a')
				new_diff = (diff - key_pos) % 26
				new_pos = new_diff - ord('a')
				print(chr(new_pos), end="")	
		
			elif i.isdigit():
				diff = ord(i) + ord('0')
				new_diff = (diff - key_pos) % 10
				new_pos = new_diff - ord('0')
				print(chr(new_pos), end="")
			else:
		
				print(i, end="")

	else:
		print("Pick 1 or 2, I dont have all day. 😅️")
except:
	print("💀️ Enter a number, will you!? 😐️")

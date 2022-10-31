message = input("Enter a phrase for encoding : ")

try:
	key_pos = int(input("Enter a key for the encoding : "))
	
	print("Your encrypted is as below: \n\n")
	
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

except:

	print("enter a number, will you!? 😐️")

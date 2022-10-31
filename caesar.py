message = input("Enter a phrase for encoding : ")

try:
	key_pos = int(input("Enter a key for the encoding : "))
	
	for i in message:
	
		if i.isupper(): 

			diff = ord(i) - ord('A')
		
			new_diff = (diff + key_pos) % 26
		
			new_pos = new_diff + ord('A')
	
			 


		elif i.islower():

			diff = ord(i) - ord('a')
		
			new_diff = (diff + key_pos) % 26
		
			new_pos = new_diff + ord('a')

		elif i.isdigit():
			
			diff = ord(i) - ord('0')
		
			new_diff = (diff + key_pos) % 10
		
			new_pos = new_diff + ord('0')

		else:
			

	print(chr(new_pos), end="")

except:

	print("enter a number, will you!? 😐️")

message = input("Enter a phrase for encoding : ")

try:
	key_pos = int(input("Enter a key for the encoding : "))
	
	for i in message:

		diff = ord(i) - ord('A')
		
		new_diff = (diff + key_pos) % 26
		
		new_pos = new_diff + ord('A')
	
		print(chr(new_pos), end="") 
except:

	print("enter a number, will you!? 😐️")

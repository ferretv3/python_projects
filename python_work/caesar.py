MAX_KEY_SIZE = 26

def get_mode():
	while True:
		print("Do you wish to encrypt or decrypt or brute force a message?: ")
		mode = input().lower()
		if mode in "encrypt e decrypt d brute b".split():
			return mode[0]
		else:
			print("Enter either 'encrypt' or 'e' or 'decrypt' or 'd' or 'brute' or 'b'.")

def get_message():	
	print("Enter your message: ")
	return input()
	
def get_key():
	key = 0
	while True:
		print("Enter the key number (1-%s): " % (MAX_KEY_SIZE))
		key = int(input())
		if (key >= 1 and key <= MAX_KEY_SIZE):
			return key

def get_translated_message(mode, message, key):
	if mode[0] == 'd':
		key = -key
	translated = ''
	
	for symbol in message:
		if symbol.isalpha():
			num = ord(symbol)
			num += key
			
			if symbol.isupper():
				if num > ord('Z'):
					num -= 26
				elif num < ord('A'):
					num += 26
			elif symbol.islower():
				if num > ord('z'):
					num -= 26
				elif num < ord('a'):
					num += 26
					
			translated += chr(num)
		else:
			translated += symbol
	return translated

mode = get_mode()
message = get_message()
if mode[0] != 'b':
    key = get_key()

print("Your translated text is: ")
if mode[0] != 'b':
	print(get_translated_message(mode, message, key).upper().replace(" ", ""))
else:
	for key in range(1, MAX_KEY_SIZE + 1):
		print(get_translated_message('decrypt', message, key).upper().replace(" ", ""))
	


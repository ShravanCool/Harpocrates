from RSA03 import encrypt,decrypt
from steg03 import StegEncrypt,StegDecrypt

def main():

	message = "Hi There!!!"
	cipher = encrypt(message)
	print(cipher)
	StegEncrypt("tiger.png", cipher, "enc_tiger.png")

	clear_cipher = StegDecrypt("enc_tiger.png")
	res = decrypt(clear_cipher)

	print(res)

if __name__=="__main__":
	main()
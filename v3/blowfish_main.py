from steg03 import StegEncrypt,StegDecrypt
from blowfish import Blowfish

def main():

	pt = "Hi There!!!"
	print(pt)
	blowfish = Blowfish("dsadasdasda", pt)
	ct = blowfish.encrypt(pt)
	print(ct)
	StegEncrypt("tiger.png", ct, "enc_tiger.png")

	ct = StegDecrypt("enc_tiger.png")
	pt = blowfish.decrypt(ct)
	print(pt)

main()
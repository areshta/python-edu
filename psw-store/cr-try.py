from Crypto.Cipher import AES
from Crypto import Random

skey = "some_key"*3
print (skey[0:16])
key = str.encode(skey[0:16])
textForCoding = """This is some super text for coding.
Excelent solution!"""
iv = key

#iv = Random.new().read(AES.block_size)
cipher = AES.new(key, AES.MODE_CFB, key)
msg = cipher.encrypt(str.encode(textForCoding))



print(msg)
cipher = AES.new(key, AES.MODE_CFB, key)
dec = cipher.decrypt(msg).decode()
print (dec)

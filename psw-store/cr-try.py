from Crypto.Cipher import AES
from Crypto import Random

key = b'Sixteen byte key'
iv = key
#iv = Random.new().read(AES.block_size)
cipher = AES.new(key, AES.MODE_CFB, iv)
msg = cipher.encrypt(b'Attack at dawn')



print(msg)
cipher = AES.new(key, AES.MODE_CFB, iv)
dec = cipher.decrypt(msg)
print (dec)

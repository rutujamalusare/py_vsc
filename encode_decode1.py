"""import base64
encoded = base64.b64encode(b'Hello its string for Encoding and Decoding...')
print(encoded)

data = base64.b64decode(encoded)
print(data)"""

"""import bz2
data =bz2.compress("Donec rhoncus quis sapien sit amet molestie. Fusce scelerisque vel auguenec ullamcorper. Nam rutrum pretium placerat. Aliquam vel tristique lorem,sit amet cursus ante. In interdum laoreet mi, sit amet ultrices puruspulvinar a. Nam gravida euismod magna, non varius justo tincidunt feugiat.Aliquam pharetra lacus non risus vehicula rutrum. Maecenas aliquam leofelis. Pellentesque semper nunc sit amet nibh ullamcorper, ac elementumdolor luctus. Curabitur lacinia mi ornare consectetur vestibulum.")
print(data)"""
#print(data.bz2.compress())

import binascii
encoded=binascii.b2a_hex(b'hello python')
decoded=binascii.a2b_hex(encoded)
print(encoded)
print(decoded)



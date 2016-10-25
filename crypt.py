import hashlib, bas64
from os import urandom

#hash obfusciation makes md5 look like sha etc

#Written by Filip Kälebo (flipchan)
#Copyright (C) 1989, 1991 Free Software Foundation, Inc.  
#51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA
#Everyone is permitted to copy and distribute verbatim copies
#of this license document, but changing it is not allowed.


#from this file import * , md5('ur password')

#make md5 look like sha256
#sha256 = 64, md5 = 16, = 48
def md5(password):
        h = hashlib.new('md5')
        h.update(password)
        password = h.hexdigest()
        password = str(password) + str(base64.b64encode(os.urandom(48)))
        #first 16 char is the md5
        return password

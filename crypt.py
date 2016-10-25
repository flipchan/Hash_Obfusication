import hashlib, bas64
from os import urandom

#hash obfusciation makes md5 look like sha etc

#Written by Filip Kälebo (flipchan)
'''
Copyright (C) 2016  Filip Kälebo (flipchan)

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

'''
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

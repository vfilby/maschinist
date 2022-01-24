#!/usr/bin/env PYTHON
import pybinn

data = pybinn.dumps({'hello':"world", 'id':12})
print(data)
# b'\xe2\x16\x02\x02id \x0c\x05hello\xa0\x05world\x00'


data = b'\xe2\x16\x02\x02id \x0c\x05hello\xa0\x05world\x00 '
obj = pybinn.loads(data)
print(obj)
# {'id': 12, 'hello': 'world'}

data = b'\x89\xad__ni_internal\x81\xa6source\xa5other\xa6author\xaeSpecial Author\xa7comment\xd9dSo many comments... so much to say.. I mean... you gotta go out there and give 110%....  every time.\xaadeviceType\xa4LOOP\xa5modes\x96\xaaSpecial FX\xacStabs & Hits\xa8Surround\xa5Synth\xaaTambourine\xacTempo-synced\xa4name\xa8metadata\xa5tempo\xcb\x00\x00\x00\x00\x00\x00\x00\x00\xa5types\x92\x91\xa5Drums\x91\xa7Texture\xa6vendor\xaeAwesome Vendor'

#obj = pybinn.loads(data)
#print(obj)

s = "So many comments... so much to say.. I mean... you gotta go out there and give 110%....  every time."
data = pybinn.dumps(s)
print(data)
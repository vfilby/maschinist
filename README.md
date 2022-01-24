# Maschinist

Here I am attempting to build a system to automatically tag loops and one-shot
.wav samples for use in Maschine.

So far it looks like Maschine uses Generic Embedded Objects from the ID3v2 
media tagging standard.  Some flavours of XML seems to work (older standard 
perhaps) but examples taken from my maschine library have a different format
using a binary encoding that is partially decipherable.

Here is the GEOB portion of ID3v2 extracted from a sample that was tagged with
test data to try to work out the underlying encoding:

* Content Type: Loop
* Types: Drums, Texture
* Character: Special FX, Stabs & Hits, Surround, Synth, Tambourine, Tempo-synced
* Properties:
	* Vendor: Awesome Vendor
	* Author: Special Author
	* Comment: So many comments... so much to say.. I mean... you gotta go out there and give 110%....  every time.

```
{
	'GEOB:com.native-instruments.nks.soundinfo': 
		GEOB( encoding=<Encoding.LATIN1: 0>, 
			  mime='', 
			  filename='', 
			  desc='com.native-instruments.nks.soundinfo', 
			  data=b'\x89\xad__ni_internal\x81\xa6source\xa5other\xa6author\xaeSpecial Author\xa7comment\xd9dSo many comments... so much to say.. I mean... you gotta go out there and give 110%....  every time.\xaadeviceType\xa4LOOP\xa5modes\x96\xaaSpecial FX\xacStabs & Hits\xa8Surround\xa5Synth\xaaTambourine\xacTempo-synced\xa4name\xa8metadata\xa5tempo\xcb\x00\x00\x00\x00\x00\x00\x00\x00\xa5types\x92\x91\xa5Drums\x91\xa7Texture\xa6vendor\xaeAwesome Vendor'
		), 
	'GEOB:com.native-instruments.nisound.soundinfo': 
		GEOB(encoding=<Encoding.LATIN1: 0>, 
			 mime='', 
			 filename='', 
			 desc='com.native-instruments.nisound.soundinfo', 
			 data=b'\x02\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00m\x00e\x00t\x00a\x00d\x00a\x00t\x00a\x00\x0e\x00\x00\x00S\x00p\x00e\x00c\x00i\x00a\x00l\x00 \x00A\x00u\x00t\x00h\x00o\x00r\x00\x0e\x00\x00\x00A\x00w\x00e\x00s\x00o\x00m\x00e\x00 \x00V\x00e\x00n\x00d\x00o\x00r\x00d\x00\x00\x00S\x00o\x00 \x00m\x00a\x00n\x00y\x00 \x00c\x00o\x00m\x00m\x00e\x00n\x00t\x00s\x00.\x00.\x00.\x00 \x00s\x00o\x00 \x00m\x00u\x00c\x00h\x00 \x00t\x00o\x00 \x00s\x00a\x00y\x00.\x00.\x00 \x00I\x00 \x00m\x00e\x00a\x00n\x00.\x00.\x00.\x00 \x00y\x00o\x00u\x00 \x00g\x00o\x00t\x00t\x00a\x00 \x00g\x00o\x00 \x00o\x00u\x00t\x00 \x00t\x00h\x00e\x00r\x00e\x00 \x00a\x00n\x00d\x00 \x00g\x00i\x00v\x00e\x00 \x001\x001\x000\x00%\x00.\x00.\x00.\x00.\x00 \x00 \x00e\x00v\x00e\x00r\x00y\x00 \x00t\x00i\x00m\x00e\x00.\x00\x00\x00\x00\x00\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x0c\x00\x00\x00\\\x00.\x00S\x00p\x00e\x00c\x00i\x00a\x00l\x00 \x00F\x00X\x00\x0e\x00\x00\x00\\\x00.\x00S\x00t\x00a\x00b\x00s\x00 \x00&\x00 \x00H\x00i\x00t\x00s\x00\n\x00\x00\x00\\\x00.\x00S\x00u\x00r\x00r\x00o\x00u\x00n\x00d\x00\x07\x00\x00\x00\\\x00.\x00S\x00y\x00n\x00t\x00h\x00\x0c\x00\x00\x00\\\x00.\x00T\x00a\x00m\x00b\x00o\x00u\x00r\x00i\x00n\x00e\x00\x0e\x00\x00\x00\\\x00.\x00T\x00e\x00m\x00p\x00o\x00-\x00s\x00y\x00n\x00c\x00e\x00d\x00\x07\x00\x00\x00\\\x00:\x00D\x00r\x00u\x00m\x00s\x00\t\x00\x00\x00\\\x00:\x00T\x00e\x00x\x00t\x00u\x00r\x00e\x00\x00\x00\x00\x00\x07\x00\x00\x00\x07\x00\x00\x00\\\x00@\x00c\x00o\x00l\x00o\x00r\x00\x01\x00\x00\x000\x00\x11\x00\x00\x00\\\x00@\x00d\x00e\x00v\x00i\x00c\x00e\x00t\x00y\x00p\x00e\x00f\x00l\x00a\x00g\x00s\x00\x01\x00\x00\x008\x00\x0b\x00\x00\x00\\\x00@\x00s\x00o\x00u\x00n\x00d\x00t\x00y\x00p\x00e\x00\x01\x00\x00\x000\x00\x07\x00\x00\x00\\\x00@\x00t\x00e\x00m\x00p\x00o\x00\x01\x00\x00\x000\x00\x06\x00\x00\x00\\\x00@\x00v\x00e\x00r\x00l\x00\x06\x00\x00\x001\x00.\x007\x00.\x001\x004\x00\x06\x00\x00\x00\\\x00@\x00v\x00e\x00r\x00m\x00\x06\x00\x00\x001\x00.\x007\x00.\x001\x004\x00\x07\x00\x00\x00\\\x00@\x00v\x00i\x00s\x00i\x00b\x00\x01\x00\x00\x000\x00'
		)
}
```

## Breaking Down the Binary Format

```
\x89\xad__ni_internal\x81\xa6source\xa5other\xa6author\xaeSpecial Author\xa7comment\xd9dSo many comments... so much to say.. I mean... you gotta go out there and give 110%....  every time.\xaadeviceType\xa4LOOP\xa5modes\x96\xaaSpecial FX\xacStabs & Hits\xa8Surround\xa5Synth\xaaTambourine\xacTempo-synced\xa4name\xa8metadata\xa5tempo\xcb\x00\x00\x00\x00\x00\x00\x00\x00\xa5types\x92\x91\xa5Drums\x91\xa7Texture\xa6vendor\xaeAwesome Vendor
```

### Text values
One common pattern seems to be that textual sections are preceded by a single 
byte where the first four bits are constant `0x1010` (10) and the next four bits
represent the length of the value.

For example:

`\xad__ni_internal`

`0xAD` = `0b10101101` which yields `0b1010` and `0b1101` (10 and 13).  10 appears to be
a constant of some sort and 13 is the length of `__ni_internal`

We see this many times in this sample:

* `\xa6source` `0xA6` -> `0b1010` and `0b0110` (10 and 6)
* `\xa5other` `0xA5` -> `0b1010` and `0b0101` (10 and 5)
* `\xa6author` `0xA6` -> 0b1010 and `0b0110` (10 and 6)
* `\xaeSpecial Author` `0xAE` -> `0b1010` and `0b1110` (10 and 14)
* `\xa7comment` `0xA7` -> `0b1010` and `0b0111` (10 and 7)

One interesting this is the actual comment which is much longer than the 16 
characters that can be accounted for in 4 bits. The comment is preceded by two
bytes:

`\xd9dSo many comments... so much to say.. I mean... you gotta go out there and give 110%....  every time.`

* `0xD9` -> `0b11011001`
* `d` or `0x64` -> `0b01100100` or 100, which is the length of the comment text.

For contrast in a previous test I used 'TestComment' as the comment text and
the tag included:

`\xabTestComment`

`0xAB` -> `0b1010` and `0b1011`  (10 and 11)

So it seems like there is some special case where strings longer than 16 
characters have an additional marker.



```
\x89\xad__ni_internal\x81\xa6source\xa5other\xa6author\xaeSpecial Author\xa7comment\xd9dSo many comments... so much to say.. I mean... you gotta go out there and give 110%....  every time.\xaadeviceType\xa4LOOP\xa5modes\x96\xaaSpecial FX\xacStabs & Hits\xa8Surround\xa5Synth\xaaTambourine\xacTempo-synced\xa4name\xa8metadata\xa5tempo\xcb\x00\x00\x00\x00\x00\x00\x00\x00\xa5types\x92\x91\xa5Drums\x91\xa7Texture\xa6vendor\xaeAwesome Vendor
```

## Possible Off the Shelf Solutions?

Could be the BINN format? https://github.com/liteserver/binn/blob/master/spec.md

* `0xD9` -> `0b11011001`
* `d` or `0x64` -> `0b01100100` or 100, which is the length of the comment text.


110 11001 01100100

### BSON

Nope. Document size prefix is missing


### Smile

https://github.com/FasterXML/smile-format-specification/blob/master/smile-specification.md

Nope: the magic byte sequence for Smile isn't present here.


## MessagePack

```python
{
	b'__ni_internal': {
			b'source': b'other'
	}, 
	b'author': b'Special Author', 
	b'comment': b'So many comments... so much to say.. I mean... you gotta go out there and give 110%....  every time.', 
	b'deviceType': b'LOOP', 
	b'modes': [b'Special FX', b'Stabs & Hits', b'Surround', b'Synth', b'Tambourine', b'Tempo-synced'], 
	b'name': b'metadata', 
	b'tempo': 0.0, 
	b'types': [
		[b'Drums'], [b'Texture']
	], 
	b'vendor': b'Awesome Vendor'
}
```

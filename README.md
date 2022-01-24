# Maschinist

Here I am attempting to build a system to automatically tag loops and one-shot
.wav samples for use in Maschine.

## Spelunking

[Hex Fiend](https://hexfiend.com) (or any other good hex editor/viewer) is a
great tool for starting to dig into this.

### Clue #1: Importing a sample that was pretagged.

I imported a sample that was from Loopmasters and was surprised to see that
it came with tags.  Also there was a Maschine error message that noted some
values were invalid and needed to be converted.

Opening that sample in our fiendly hex editor revealed the following data 
embedded in the sample"

```
ID3 ì   ID3     	bGEOB   X     com.native-instruments.soundinfo <?xml version="1.0" encoding="UTF-8" standalone="no" ?>
<soundinfo version="400">

  <properties>
	<name>TE_Cymbal_1</name>
  </properties>

  <banks>
	<bank>Loopmasters</bank>
  </banks>

  <attributes>
	<attribute>
	  <value>Percussion</value>
	  <user-set>GB.Type</user-set>
	</attribute>
	<attribute>
	  <value>Pop LM</value>
	  <user-set>GB.Type</user-set>
	</attribute>
  </attributes>

</soundinfo>
```

After a bit of digging through the ID3 standards it looks like Maschine uses 
Generic Embedded Objects from the ID3v2 media tagging standard.  

#### Trying to reverse the process

I imported a junk sample into my Maschine library and added the following
metadata. Here is the GEOB portion of ID3v2 extracted from a sample that was
tagged with test data to try to work out the underlying encoding:

* Content Type: Loop
* Types: Drums, Texture
* Character: Special FX, Stabs & Hits, Surround, Synth, Tambourine, Tempo-synced
* Properties:
	* Vendor: Awesome Vendor
	* Author: Special Author
	* Comment: So many comments... so much to say.. I mean... you gotta go out there and give 110%....  every time.
	
While I could see the data in the hex editor I wanted to access it 
programmatically.  I tried a few libraries and I can't recall which, but I know
that [mutagen](https://mutagen.readthedocs.io/en/latest/index.html) was the only one that did what I needed:

```
Python 3.9.9 | packaged by conda-forge | (main, Dec 20 2021, 02:41:06) 
[Clang 11.1.0 ] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import mutagen
>>> mutagen.File("/Volumes/Data Puddle/Sample Library/Test/Test Bank/metadata.wav")
{'GEOB:com.native-instruments.nks.soundinfo': GEOB(encoding=<Encoding.LATIN1: 0>, mime='', filename='', desc='com.native-instruments.nks.soundinfo', data=b'\x88\xad__ni_internal\x81\xa6source\xa5other\xa6author\xaaTestAuthor\xa7comment\xabTestComment\xa5modes\x94\xa8Acoustic\xa8Additive\xa4Airy\xa6Analog\xa4name\xa8metadata\xa5tempo\xcb\x00\x00\x00\x00\x00\x00\x00\x00\xa5types\x93\x91\xa8Ambience\x91\xa4Bass\x91\xa5Drums\xa6vendor\xaaTestVendor'), 'GEOB:com.native-instruments.nisound.soundinfo': GEOB(encoding=<Encoding.LATIN1: 0>, mime='', filename='', desc='com.native-instruments.nisound.soundinfo', data=b'\x02\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00m\x00e\x00t\x00a\x00d\x00a\x00t\x00a\x00\n\x00\x00\x00T\x00e\x00s\x00t\x00A\x00u\x00t\x00h\x00o\x00r\x00\n\x00\x00\x00T\x00e\x00s\x00t\x00V\x00e\x00n\x00d\x00o\x00r\x00\x0b\x00\x00\x00T\x00e\x00s\x00t\x00C\x00o\x00m\x00m\x00e\x00n\x00t\x00\x00\x00\x00\x00\xff\xff\xff\xff\xff\xff\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x07\x00\x00\x00\n\x00\x00\x00\\\x00.\x00A\x00c\x00o\x00u\x00s\x00t\x00i\x00c\x00\n\x00\x00\x00\\\x00.\x00A\x00d\x00d\x00i\x00t\x00i\x00v\x00e\x00\x06\x00\x00\x00\\\x00.\x00A\x00i\x00r\x00y\x00\x08\x00\x00\x00\\\x00.\x00A\x00n\x00a\x00l\x00o\x00g\x00\n\x00\x00\x00\\\x00:\x00A\x00m\x00b\x00i\x00e\x00n\x00c\x00e\x00\x06\x00\x00\x00\\\x00:\x00B\x00a\x00s\x00s\x00\x07\x00\x00\x00\\\x00:\x00D\x00r\x00u\x00m\x00s\x00\x00\x00\x00\x00\x07\x00\x00\x00\x07\x00\x00\x00\\\x00@\x00c\x00o\x00l\x00o\x00r\x00\x01\x00\x00\x000\x00\x11\x00\x00\x00\\\x00@\x00d\x00e\x00v\x00i\x00c\x00e\x00t\x00y\x00p\x00e\x00f\x00l\x00a\x00g\x00s\x00\x01\x00\x00\x000\x00\x0b\x00\x00\x00\\\x00@\x00s\x00o\x00u\x00n\x00d\x00t\x00y\x00p\x00e\x00\x01\x00\x00\x000\x00\x07\x00\x00\x00\\\x00@\x00t\x00e\x00m\x00p\x00o\x00\x01\x00\x00\x000\x00\x06\x00\x00\x00\\\x00@\x00v\x00e\x00r\x00l\x00\x06\x00\x00\x001\x00.\x007\x00.\x001\x004\x00\x06\x00\x00\x00\\\x00@\x00v\x00e\x00r\x00m\x00\x06\x00\x00\x001\x00.\x007\x00.\x001\x004\x00\x07\x00\x00\x00\\\x00@\x00v\x00i\x00s\x00i\x00b\x00\x01\x00\x00\x000\x00')}
>>> 
```

And the objects formatted:

```python
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

Sadly no easily readable XML, but a somewhat decipherable binary encoding.
Perhaps the XML was an older standard used by Native Instruments?

#### Breaking Down the first GEOB

```
\x89\xad__ni_internal\x81\xa6source\xa5other\xa6author\xaeSpecial Author\xa7comment\xd9dSo many comments... so much to say.. I mean... you gotta go out there and give 110%....  every time.\xaadeviceType\xa4LOOP\xa5modes\x96\xaaSpecial FX\xacStabs & Hits\xa8Surround\xa5Synth\xaaTambourine\xacTempo-synced\xa4name\xa8metadata\xa5tempo\xcb\x00\x00\x00\x00\x00\x00\x00\x00\xa5types\x92\x91\xa5Drums\x91\xa7Texture\xa6vendor\xaeAwesome Vendor
```

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

*Possible off the shelf/default encoders?*

At this point I have a partial understanding of the encoding, so let's see if
we can find a serialization scheme that fits. 

* [Binn](https://github.com/liteserver/binn/blob/master/spec.md):  format kinda fits, but some parts just don't seem to work and I couldn't decode the binary data with a Binn deserializer...  so likely nope.
* [BSON](https://en.wikipedia.org/wiki/BSON): This one's easy...  the document size prefix is missing.. Nope.
* [Smile](https://github.com/FasterXML/smile-format-specification/blob/master/smile-specification.md) The magic byte sequence for Smile isn't present here... Nope.
* [MessagePack](https://github.com/msgpack/msgpack/blob/master/spec.md) Very promising, looks like a good match.

Let's try to work with it:

```
>>> import msgpack
>>> packed = b'\x89\xad__ni_internal\x81\xa6source\xa5other\xa6author\xaeSpecial Author\xa7comment\xd9dSo many comments... so much to say.. I mean... you gotta go out there and give 110%....  every time.\xaadeviceType\xa4LOOP\xa5modes\x96\xaaSpecial FX\xacStabs & Hits\xa8Surround\xa5Synth\xaaTambourine\xacTempo-synced\xa4name\xa8metadata\xa5tempo\xcb\x00\x00\x00\x00\x00\x00\x00\x00\xa5types\x92\x91\xa5Drums\x91\xa7Texture\xa6vendor\xaeAwesome Vendor'
>>> unpacked = msgpack.unpackb(packed)
>>> unpacked
{b'__ni_internal': {b'source': b'other'}, b'author': b'Special Author', b'comment': b'So many comments... so much to say.. I mean... you gotta go out there and give 110%....  every time.', b'deviceType': b'LOOP', b'modes': [b'Special FX', b'Stabs & Hits', b'Surround', b'Synth', b'Tambourine', b'Tempo-synced'], b'name': b'metadata', b'tempo': 0.0, b'types': [[b'Drums'], [b'Texture']], b'vendor': b'Awesome Vendor'}
>>> packed2 = msgpack.packb(unpacked)
>>> packed == packed2
False
>>> packed
b'\x89\xad__ni_internal\x81\xa6source\xa5other\xa6author\xaeSpecial Author\xa7comment\xd9dSo many comments... so much to say.. I mean... you gotta go out there and give 110%....  every time.\xaadeviceType\xa4LOOP\xa5modes\x96\xaaSpecial FX\xacStabs & Hits\xa8Surround\xa5Synth\xaaTambourine\xacTempo-synced\xa4name\xa8metadata\xa5tempo\xcb\x00\x00\x00\x00\x00\x00\x00\x00\xa5types\x92\x91\xa5Drums\x91\xa7Texture\xa6vendor\xaeAwesome Vendor'
>>> packed2
b'\x89\xad__ni_internal\x81\xa6source\xa5other\xa6author\xaeSpecial Author\xa7comment\xda\x00dSo many comments... so much to say.. I mean... you gotta go out there and give 110%....  every time.\xaadeviceType\xa4LOOP\xa5modes\x96\xaaSpecial FX\xacStabs & Hits\xa8Surround\xa5Synth\xaaTambourine\xacTempo-synced\xa4name\xa8metadata\xa5tempo\xcb\x00\x00\x00\x00\x00\x00\x00\x00\xa5types\x92\x91\xa5Drums\x91\xa7Texture\xa6vendor\xaeAwesome Vendor'
```

Not perfect... but very close.  

The only difference is The encoding of the comment. The original was 
`\xd9dSo many comments... ` and the reencoded version is 
`\xda\x00dSo many comments... `. Looking at the msgpack spec the only difference
is that the re-encoded version used two bytes to represent the string length
instead of one.

As per the [msgpack spec on strings](https://github.com/msgpack/msgpack/blob/master/spec.md#str-format-family):

```
str 8 stores a byte array whose length is upto (2^8)-1 bytes:
+--------+--------+========+
|  0xd9  |YYYYYYYY|  data  |
+--------+--------+========+

str 16 stores a byte array whose length is upto (2^16)-1 bytes:
+--------+--------+--------+========+
|  0xda  |ZZZZZZZZ|ZZZZZZZZ|  data  |
+--------+--------+--------+========+
```

I think we have a winner.

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

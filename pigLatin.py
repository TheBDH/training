s = raw_input("translate this into pig latin: ")
while s != "":
	words = s.split()
	translated = ""
	vowels = ["a", "e", "i", "o", "u"]
	for word in words:
		if word[0] not in vowels:
			if word[1] not in vowels:
				translated += word[2:] + word[:1] + "ay "
			else:
				translated += word[1:] + word[0] + "ay "
		else:
			translated += word + "way "
	print translated
	s = raw_input("translate this into pig latin: ")
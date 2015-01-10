sequence = "abcdefghijklmnopqrstuvwxyz"

def replace_character_at_position(string, position, character):
	return string[:position] + character + string[position + 1:]

def unique_list(seq):
    seen = set()
    return [x for x in seq if x not in seen and not seen.add(x)]

def create_new_quote(quote):
	for each_character in replace_sequence:
		if each_character != ".":
			quote = quote.replace(sequence[replace_sequence.index(each_character)], each_character)
	return quote

def cleanup_sequence(quote):
	new_sequence = sequence
	for i in range(len(sequence)):
		if sequence[i] not in original_quote:
			new_sequence = new_sequence[:i - 1] + new_sequence[i:]
	return new_sequence

def discovered_characters_list(replace_sequence):
	return unique_list([sequence[replace_sequence.index(x)] for x in replace_sequence if x != '.'])

def discoverable_words(wordlist, replace_sequence):
	return_list = []
	for each_word in wordlist:
		for each_letter in discovered_characters_list(replace_sequence):
			if each_word.count(each_letter) > 0:
				return_list.append(each_word)
	return return_list

def sort_wordlist(wordlist, replace_sequence):
	wordlist = discoverable_words(wordlist, replace_sequence)
	discovered_characters = discovered_characters_list(replace_sequence)
	for i in range(len(wordlist)):
		for j in range(i, len(wordlist)):
			for k in range(len(discovered_characters)):
				if wordlist[j].index(discovered_characters[k]) < wordlist[i].index(discovered_characters[k]):
					temp = wordlist[i]
					wordlist[i] = wordlist[j]
					wordlist[j] = temp
	return wordlist

# original_quote = raw_input("Enter Quote: ")
original_quote = "hfglohk oa bfmt rfhjnrowt gf vtcrt fd bohj glch hfg lcwohk chp fvohofha cg cyy"
# replace = raw_input("Replace with (x, y): ").split(',')
replace = "k,g".split(',')

sequence = cleanup_sequence(original_quote)
replace_sequence = sequence
for i in range(len(sequence)):
	replace_sequence = replace_character_at_position(replace_sequence, i, '.')
replace_sequence = replace_character_at_position(replace_sequence, sequence.index(replace[0]), replace[1])
print original_quote

quote_words = sort_wordlist(original_quote.split(" "), replace_sequence)

# f=open("words\words"+str(s.index(sch))+"x"+str(ssize)+".txt", "r")
# for line in f:
# 	ch=line[npos-1:npos]
# 	if ((ch==nch)):
# 		print(line)

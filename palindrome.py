import string

def p(s):
	s = s.translate(string.maketrans("",""), string.punctuation) # strips punctuation
	s = s.replace(" ", "") # strips out all whitespaces

	if len(s) == 1 or len(s) == 0: # 1 to account for odd-number length words, 0 to acount for even-length words
		return True

	if s[0] != s[-1]: # if first letter doesn't match last letter in current string, not a palindrome, so return False
		return False

	else:
		return p(s[1:-1])

# Write a function that takes a string as a parameter and returns True if the string is a palindrome, False otherwise. Remember that a string is a palindrome if it is spelled the same both forward and backward. for example: radar is a palindrome. for bonus points palindromes can also be phrases, but you need to remove the spaces and punctuation before checking.
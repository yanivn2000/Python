#Write is polindrome function
#ABNNBA - True
#AMMJK - False
#AAB|BAA
#12344321

def is_polindrome(word):
    """Checks if the word is polindrome"""
    left_pos = 0
    right_pos = len(word) - 1

    while right_pos >= left_pos:
        if not word[left_pos] == word[right_pos]:
            return False
        left_pos += 1
        right_pos -= 1
    return True


print(is_polindrome("ABNNBA"))
print(is_polindrome("AMMJK"))


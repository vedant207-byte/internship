def is_anagram_sorted(str1, str2):
    return sorted(str1) == sorted(str2)

print(is_anagram_sorted("listen", "silent"))  
print(is_anagram_sorted("hello", "world"))    

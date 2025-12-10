def are_anagrams(s1: str, s2: str) -> bool:
    return sorted(s1) == sorted(s2)

print(are_anagrams("listen", "silent")) 
print(are_anagrams("hello", "world"))   
print(are_anagrams("race", "care"))     

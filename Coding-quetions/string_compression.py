#Write a function that takes a string and compresses consecutive repeating characters.
def compress_string(s: str) -> str:
    if not s: 
        return ""
    
    result = []
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            result.append(s[i-1] + str(count))
            count = 1
    
    result.append(s[-1] + str(count))
    
    return "".join(result)


print(compress_string("aaabbcddd"))  
print(compress_string("abcd"))       
print(compress_string(""))          

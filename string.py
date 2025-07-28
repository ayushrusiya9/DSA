text = "   hEllo, my name is aYush rusiya!! i loVe pYthOn prOgramming.   "

# 1. Whitespace remove
print(text.strip())
print(text.lstrip())
print(text.rstrip())

# 2. Case conversion
print(text.lower())
print(text.upper())

# 3. Capitalization
print(text.capitalize())
print(text.title())

# 4. Count method
print(text.lower().count("python"))

# 5. Check methods
print(text.isalpha())
print(text.isalnum())
print(text.isspace())

# 6. Replace method
print(text.replace("aYush rusiya", "Ayush R."))

# 7. Split & Join
words = text.split()
print(words)
print("-".join(words))

# 8. Startswith & Endswith
print(text.strip().startswith("hEllo"))
print(text.strip().endswith("."))

# 9. Find & Index
print(text.find("love"))
print(text.lower().index("love"))

# 10. Format string
name = "Ayush"
lang = "Python"
print(f"My name is {name} and I love {lang} programming.")
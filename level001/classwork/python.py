text="my name is lasha"

if text.isalnum():
    print("text is all num")
elif text.isalpha():
    print("text is alpha")
elif text.islower():
    print("text is lower")
elif text.isidentifier():
    print("text is identifier")
else:
    print("text is neither")
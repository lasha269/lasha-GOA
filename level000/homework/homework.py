for i in range(1, 31):
    if i % 2 == 0 and i % 3 == 0:
        print("Double")
    elif i % 2 == 0:
        print("Even")
    elif i % 3 == 0:
        print("Triple")
    else:
        print("Other")







n = 36
count = 0

for i in range(1, n):
    if n % i == 0:
        print(i)
        count += 1

if count > 8:
    print("ბევრი გამყოფი აქვს")
else:
    print("ცოტა გამყოფია")








text = "Python Programming language"

print(text.count("g"))
print(text.find("Programming"))

if text.count("g") > 2:
    print("ბევრია")
else:
    print("ცოტაა")








username = "Lasha2026"

if username.isupper() and username.isalnum():
    print("სწორი ფორმატია")
else:
    print("შეცდომაა")








code_str = "12345"

if code_str.isdigit() and code_str.isdecimal():
    print("მხოლოდ რიცხვებია")
else:
    print("შეიცავს სხვა სიმბოლოებს")









word = "hello"

if word.islower() and word.isalpha():
    print("იდენტურია")
else:
    print("ყურადღება მიაქციე რეგისტრს")
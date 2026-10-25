colors = ["red", "green", "blue", "yellow"]

if len(colors) > 4:
    print("-".join(colors))
elif len(colors) < 4:
    print(" ".join(colors))
else:
    print(": ".join(colors))








students = ["ანასტასია", "გიორგი", "ლუკა", "ნიკა", "მარიამი", "დაჩი"]

if len(students) > 5:
    print(",".join(name.upper() for name in students))
else:
    print("-".join(students))











products = "პურის,რძე,კვერცხი,ყველი,კარაქი".split(",")

for product in products:
    print(product.upper())








sentence = "პითონი არის ძალიან მარტივი და ძლიერი ენა"

words = sentence.split(" ")

for word in words:
    print(word, len(word))














file = "my_report_final_v2.docx"

name, extension = file.rsplit(".", 1)

print(name)
print(extension)








path = "/home/user/projects/website/index.html"

folder, filename = path.rsplit("/", 1)

print(folder)
print(filename)








user_id = "7"

print(user_id.zfill(4))





file_number = "15"

print(file_number.zfill(6))






minutes = "5"

print(minutes.zfill(2))
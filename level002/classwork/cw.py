names=["nika", "gio", "lasha" , "mari", "leo"]

if len(names)>5:
    result=" ".join(names)
elif len(names)<5:
    result="-".join(names)
else:
    result=",".join(names)

print(result)





text="ვაშლი,ბანანი,ფორთოხალი,მსხალი"

fruits=text.split(",")

for fruit in fruits:
    print(fruit)






adress="C:/Users/Admin/Documents/Python/main.py"

file_name=adress.rsplit("/",1)
print(file_name)





number="42"

result=number.zfill(5)
print(result)






raw_data = "   ###admin--- , ---moderator### , ---user_guest###   "

step1=raw_data.strip()

step2=step1.split(",")

print(step2)

for item in step2:
    clean_item=item.lstrip(" #").rstrip("#-")
    print(clean_item)
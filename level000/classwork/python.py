"""1) შექმენი იმეილის შემამოწმებელი ფუნქცია (emailChecker) რომელმაც უნდა შეამოწმოს რომ:
იმეილის სიგრძე არის 5ზე მეტი
იმეილში არის "@" სიმბოლო მხოლოდ ერთხელ
იმეილი ბოლოვდება "gmail.com"-ით"""

email="lasha@123@gmail.com"

def email_checker(email):
    if len(email)-10 and email.count("@")==1 and email.endswith("gmail.com"):
        return "email is correct"
    else:
        return "email is incorrect"
print(email_checker(email))
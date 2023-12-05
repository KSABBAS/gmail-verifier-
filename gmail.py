email=input("enter the email : ").split("@")
con=False
for i in email:
    for l in i:
        if l==".":
            email.remove(i)
            email.extend(i.split("."))
            break
if email[1]=="gmail" and email[2]=="com":
    con=True
print(con)
days = ["mon","tue","wed","thur","fri"]


print("mon" in days)
days.append("sun")
print(days)
days.reverse()
print(days)

days = ("mon","tue","wed","thur","fri")

print(days)

# dic

nico = {
  "name" : "nico",
  "age" : 29,
  "korean" : True,
  "fav_food" : ["kimchi", "Sashimi"]
}
nico["handsome"] = True
print(nico)
# 1.3
print(len("hoge"))
age = "18"
age_n = int(age)
print(type(age_n))
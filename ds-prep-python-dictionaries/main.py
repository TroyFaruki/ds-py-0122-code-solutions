person = {
  "first_name" : "Troy",
  "last_name" : "Faruki",
  "hobby" : "Code"
}
print(person)
first_name= person["first_name"]
last_name = person.get("last_name")
middle_name = person.get("middle_name")
print(first_name, middle_name, last_name)
person["job"]= "adjuster"
print(person)
person["hobby"] = "reading"
print(person)
person.pop("last_name")
print(person)

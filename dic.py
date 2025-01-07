# d={"name":"sindhu","age":"19","name1":"sindhu"}
# print(d)
# print(d["age"])

# d={"name":"sindhu","age":"19","name1":"sindhu"}
# print(d)
# print(len(d))

# d={"name":"sindhu","age":"19","name1":["sindhu","sindhuja"]}
# print(d)
# d["college"]="MEC"
# print(d)
# d.update({"place":"namakkal"})
# print(d)

# d={"name":"sindhu","age":"19","place":"namakkal"}
# print(d)
# d.clear()
# print(d)

# d={"name":"sindhu","age":"19","place":"namakkal"}
# print(d)
# a=d.copy()
# print(a)
# ##get method              
# d.get("age")
# print(d)

# d={"name":"sindhu","age":"19","place":"namakkal"}
# a=d.items()
# print(a)
# a=d.keys()
# print(a)
# d.pop("age")
# print(a)

##pop items
# d={"name":"sindhu","age":"19","place":"namakkal"}
# print(d)
# d.popitem()
# print(d)

##set default
d={"name":"sindhu","age":"19","place":"namakkal"}
a=d.setdefault("frnd","pp")
print(d)

##update
# d={"name":"sindhu","age":"19","place":"namakkal"}
# d.update({"car":"altroz"})
# print(d)

##values
# d={"name":"sindhu","age":"19","place":"namakkal"}
# a=d.values()
# print(a)
# a=d.values()
# d["CRH"]="pk"
# print(a)

##loop dict (key names)
# d={"name":"sindhu","age":"19","place":"namakkal"}
# print(d)
# for i in d:
#     print(i)

# ##values
# d={"name":"sindhu","age":"19","place":"namakkal"}
# for i in d:
#     print(d[i])

##using values
# d={"name":"sindhu","age":"19","place":"namakkal"}
# for i in d.values():
#     print(i)

##using keys
# d={"name":"sindhu","age":"19","place":"namakkal"}
# for i in d.keys():
#     print(i)

##using items
# d={"name":"sindhu","age":"19","place":"namakkal"}
# for i,j in d.items():
#     print(i,j)

##remove
# d={"name":"sindhu","age":"19","place":"namakkal"}
# del d["age"]
# print(d)

##clear
# d={"name":"sindhu","age":"19","place":"namakkal"}
# print(d)
# d.clear()
# print(d)

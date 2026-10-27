# stores many items
ages = [20,38,26,32,87,23,3,]#list
names = ["Ayana","Jack","Rick","Moha","Ben","Eliud"]
# functions
ages.append(22)#adds 22
# ages.clear() this removes everything
# ages.sort()# arranges in ascending order
# ages.reverse()#arranges in descending order
print(ages)

# names.sort()
print(names)

joan_count = names.count("joan")# counts how many joan are in the list
print(joan_count)

# print(len(names))#counts names
# print(len(ages))#counts ages
#
# #search coding challenges eg hacker rank
#
# # retrieve an element
# print(ages[0])
# print(ages[5])
#
# print(names[0])
# print(names[-1])#negative is python specific
# print(names[-2])
#
# print(names[-5:])#slicing list
# print(ages[3:])#from 3 to end
# print(ages[:3])#from 0-2
# print(ages[3:5])#3,4

#set(used to remove duplucates
scores = {88,78,88,65,77,78}
print(scores)

# tuple(is immutable meaning it can never change)
weekdays =("monday","tuesday","wednesday","thursday","friday","saturday")
print(weekdays[-4])

#dictionary
person ={"name" : "jack","age" : 88,"weight" : 76,"height" : 1.78}
print(person["name"])


people =[{"name":"adrian","age": 24},
         {"name":"moris","age": 30},
         {"name":"hellen","age": 15},
         ]
print(people[0]["name"])
# big 0 notation/algorithms

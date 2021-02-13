'''
practice - Dictionary
* unordered
* changeable
* no indexing
* keys should be immutable type
* if tuple contains any mutable object directly/indirectly it cannot be used as a key
'''

teams = {"India":["Virat","Dhoni","Rohit"], "England":["Root","Stokes","Buttler"], "Australia":["Finch","Warner","Smith"]}
print(teams)

'''
----------------------- Accessing elements -----------------------------------------------------

print(teams["India"])
#Use the key to print the corresponding values
#  print(teams[0])   -> KeyError as 0 is not a key 
------------------------------------------------------------------------------------------------
'''

'''
----------------------- Adding elements to dictionary ------------------------------------------

teams["SouthAfrica"] = ["ABD","Steyn","Kallis"]
print(teams)
teams["India"].append("Sachin")
print(teams)
#since the value is a list, all operations performed on a list can also be performed here on the value


Ind_players = teams.get("India")
print(Ind_players)
#to get the value corresponding to a key
#while using get method if key is not present it returns None
#while using square brackets if key is not present, it returns KeyError
------------------------------------------------------------------------------------------------
'''

print("India" in teams)
#to check the presence of a key in a dictionary

print(len(teams))
#Returns the number of key value pairs in dictionary

'''
----------------------- Removing items from dictionary -----------------------------------------


ele = teams.pop("England")
print(ele)   		#Has the values corresponding to the deleted key
print(teams)
ele = teams.popitem()	#Removes the last inserted key:value pair   
print(ele)   		#Stores the popped key:value 
print(teams)
del(teams["India"])
print(teams)

teams.clear()  #Empties the dictionary
print(teams)
------------------------------------------------------------------------------------------------
'''

'''
----------------------- Copying dictionary -----------------------------------------------------

t = teams      			#shallow copy
print(t)
t["India"].append("Kumble")
print(teams)
print(t)

u = dict(teams)   		#shallow copy
u["England"].append("Cook")
print(teams)
print(u)

v = teams.copy()   		#shallow copy
v["India"].remove("Rohit")
print(v)
print(teams)

import copy

w = copy.deepcopy(teams)    	#deep copy
w["England"].remove("Root")
print(w)
print(teams)
------------------------------------------------------------------------------------------------
'''

'''
----------------------- Nested Dictionary ------------------------------------------------------

teams = {"India":{"Batsmen":"Virat","Bowler":"Kumble"}, "England":{"Batsmen":"Buttler","Bowler":"Anderson"}}
print(teams["India"]["Batsmen"])
teams["India"]["Wicket-keeper"] = "Dhoni"
print(teams)
print(teams.get("India"))
print(teams["India"].get("Wicket-keeper"))
print(teams.get("Batsmen"))   #Prints None as Batsmen is not key of teams, but it is key of elements of teams
------------------------------------------------------------------------------------------------
'''

'''
----------------------- Dictionary method ------------------------------------------------------

print(teams.keys())
#Prints all the keys in the dictionary

print(teams.values())
#Prints all the values in the dictionary

print(teams.items())
#Prints all key:Value pairs in the dictionary

team = {"India":{"Batsmen":"Virat","Bowler":"Kumble"}, "England":{"Batsmen":"Buttler","Bowler":"Anderson"}}
print(team.items())

print(sorted(teams))
#Returns the keys of the dictionary in sorted order
------------------------------------------------------------------------------------------------
'''

'''
----------------------- Dictionary comprehension -----------------------------------------------
squares = {x:x*x for x in range(6)}
print(squares)
------------------------------------------------------------------------------------------------
'''

'''
----------------------- update elements of Dictionary ------------------------------------------

teams = {"India":{"Batsmen":"Virat","Bowler":"Kumble"}, "England":{"Batsmen":"Buttler","Bowler":"Anderson"}}
teams["India"].update({"Wicket-keeper":"Dhoni"})
print(teams)
------------------------------------------------------------------------------------------------
'''

'''
----------------------- Ordered Dictionary ------------------------------------------
# Order is  preserved

from collections import OrderedDict
od = OrderedDict() 
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4
print(od)
print(od.keys())

print(reversed(od))   	#lazy evaluation
for i in reversed(od):
	print(i+":"+str(od[i]))
print(od)
------------------------------------------------------------------------------------------------
'''

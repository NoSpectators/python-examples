print ""
f = open("crime_rates.csv","r")
a = f.read()
crime_data_split = a.split("\n") #first split at newline character
print "INITIAL LIST FROM CSV"
print crime_data_split #creates a list of cities, data

print ""

final_list = []
for row in crime_data_split:
    row = row.split(",") #now split at comma, creates a list of lists
    final_list.append(row)
print "NOW A LIST OF LISTS"
print final_list

print ""

final_list.pop(-1)
print final_list



print ""
"""
cities = ['Albuquerque,749', 'Anaheim,371', 'Anchorage,828', 'Arlington,503', 'Atlanta,1379']
final_list=[]
for row in cities:
    row = row.split(",")
    final_list.append(row)
print final_list

for row in final_list:
    print row[0], int(row[1])"""

#project 6 cs112
import csv 

data2010 = {}
myFile = open('2010.csv','rt')
myReader = csv.reader(myFile)
for row in myReader:
	if row[0] != '.State':
		data2010[row[0][1:]] = row[1], row[2], row[3] 
myFile.close()
#print data2010
#print ""

data2011 = {}
myFile = open('2011.csv','rt')
myReader = csv.reader(myFile)
for row in myReader:
	if row[0] != '.State':
		data2011[row[0][1:]] = row[1], row[2], row[3] 
myFile.close()
#print data2011
#print ""

data2012 = {}
myFile = open('2012.csv','rt')
myReader = csv.reader(myFile)
for row in myReader:
	if row[0] != '.State':
		data2012[row[0][1:]] = row[1], row[2], row[3] 
myFile.close()
#print data2012
#print ""

data2013 = {}
myFile = open('2013.csv','rt')
myReader = csv.reader(myFile)
for row in myReader:
	if row[0] != '.State':
		data2013[row[0][1:]] = row[1], row[2], row[3] 
myFile.close()
#print data2013

def getCensus(year, state):
	if year == 2010:
		census_data = (state, data2010[state][0])
	if year == 2011:
		census_data = (state, data2011[state][0])
	if year == 2012:
		census_data = (state, data2012[state][0])
	if year == 2013:
		census_data = (state, data2013[state][0])
	return census_data
	
def getEstimatesBase(year, state):
	if year == 2010:
		estimates_base = (state, data2010[state][1])
	if year == 2011:
		estimates_base = (state, data2011[state][1])
	if year == 2012:
		estimates_base = (state, data2012[state][1])
	if year == 2013:
		estimates_base = (state, data2013[state][1])
	return estimates_base
	
def getYear(year, state):
	if year == 2010:
		get_year = (state, data2010[state][2])
	if year == 2011:
		get_year = (state, data2011[state][2])
	if year == 2012:
		get_year = (state, data2012[state][2])
	if year == 2013:
		get_year = (state, data2013[state][2])
	return get_year 
	
print getCensus(2010, "Alabama")
print getCensus(2011, "Alabama")
print getCensus(2012, "Alabama")
print getCensus(2013, "Alabama")
print ""
print getEstimatesBase(2010, "Alabama")
print getEstimatesBase(2011, "Alabama")
print getEstimatesBase(2012, "Alabama")
print getEstimatesBase(2013, "Alabama")
print ""
print getYear(2010, "Alabama")
print getYear(2011, "Alabama")
print getYear(2012, "Alabama")
print getYear(2013, "Alabama")






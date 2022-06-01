from datetime import datetime

def isOldEnough(birthdate,dateTest):
	try:
		d1 = datetime.strptime(birthdate, "%Y/%m/%d")
		d2 = datetime.strptime(dateTest, "%Y/%m/%d")
	except :
		raise Exception("DateFormatException")
	diff= d2.year - d1.year
	if(diff<0):
		raise Exception("DateException")
	else:
		return (diff > 18)

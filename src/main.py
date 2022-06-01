from datetime import datetime

class DateException(Exception):
	pass


def isOldEnough(birthdate,dateTest):
	d1 = datetime.strptime(birthdate, "%Y/%m/%d")
	d2 = datetime.strptime(dateTest, "%Y/%m/%d")
	diff= d2.year - d1.year
	if(diff<0):
		raise DateException
	else:
		return (diff > 18)

def main():
	try:
		print(isOldEnough("2000/01/01","2003/01/01"))#False
	except Exception as err:#
		print(err)#
	try:#
		print(isOldEnough("2000/01/01","2020/01/01"))#True	
	except Exception as err:#
		print(err)#
	try:#
		print(isOldEnough("2000/01/01","1940/01/01"))#raise
	except Exception as err:#
		print(err)#
	try:#
		print(isOldEnough("2000-01-01","2000-01-01"))#raise
	except Exception as err:
		print(err)
		

if __name__ == '__main__':
	main()
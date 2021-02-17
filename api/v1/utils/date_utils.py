from datetime import datetime

def is_valid_date(dateString,format):
	try:
		date = datetime.strptime(dateString, format)
		return True
	except:
		return False

def is_same_date(dateString1,dateString2,format):
	try:
		date1 = datetime.strptime(dateString1, format)
		date2 = datetime.strptime(dateString2, format)
		if date1 == date2:
			return True
		return False
	except:
		return None
from datetime import datetime

def is_valid_date(dateString,format):
	try:
		date = datetime.strptime(dateString, format)
		return True
	except:
		return False

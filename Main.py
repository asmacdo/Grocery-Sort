todays_list = []
todays_sorted_list = []
checked_list = []
master_list = [x.strip('\n') for x in open("listsave.txt").readlines()]


# #	This Function gets a list of items from the user and puts them into a list

def get_items():

	item = raw_input("Add item to list or \ntype 'finished' if finished \n> ")
	if 'finished' not in item:
		todays_list.append(item)
		get_items()
	elif 'finish' in item:
		print "Today's list is: ", todays_list
	else:
		print "There has been an unknown error."
		
		
# #	This function will compare items from today's list to the master list,
# #	and sort them accordingly. It will place items not on the master list at the end.	
		
def sort_todays_items():
	
	
	for item in todays_list:
		if item in master_list:
			position = master_list.index(item)
			todays_sorted_list.insert(position, item)
			
		elif item not in master_list:
			todays_sorted_list.append(item)
			
		else:
			print "Unknown Error."
	
	print "Today's list is: ", todays_sorted_list
	
	
# #	This function sorts todays items in the order the user checks them off,
# #	and makes a new list, including new items from today.	
	
def check_items():
	
	while len(todays_sorted_list) > 0:

		item = raw_input("Item checked: ")
		
		if item in todays_sorted_list:
			todays_sorted_list.remove(item)
			checked_list.append(item)
			print item, "; check!"
			
		elif item not in todays_sorted_list:
			print "Item not on list"
		
	if len(todays_sorted_list) == 0:
		print "Items were checked in this order: ", checked_list

	else:
		print "check_items error"


## This function adds items checked today to the master list
## If the items aren't already on the master list, it will add them
## Immediately after the previously checked item

def fix_master_list():
	
	count = 0
	
	for item in checked_list:
		
		if item in master_list:
			count = master_list.index(item)
			
		elif item not in master_list and count == 0:
			master_list.insert(count, item)
			
		elif item not in master_list and count != 0:
			master_list.insert(count + 1, item)
	
	target = open("listsave.txt", 'w')		
	target.writelines( "%s\n" % item for item in master_list )

	
get_items()
sort_todays_items()
check_items()
fix_master_list()
print master_list

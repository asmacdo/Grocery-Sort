todays_list = []
todays_sorted_list = []
master_list = [x.strip('\n') for x in open("listsave.txt").readlines()]
checked_list = []
print "master_list is: ", master_list


def fix_master_list():
	
	count = 0
	while count <= len(checked_list):
		if checked_list[count] in master_list:
			count += 1
		elif checked_list[count] not in master_list:
			
			
	target = open("listsave.txt", "w")
	target.write("\n".join(str(x) for x in master_list))
	
##	This function sorts todays items in the order the user checks them off,
##	and makes a new list, including new items from today.	
	
def check_items():

	item = raw_input("Item checked: ")
	
	if item in todays_list:
		todays_list.remove(item)
		checked_list.append(item)
		print item, "; check!"
		
	else:
		print "Item not on list"
		
	if len(todays_sorted_list) == 0:
		print "Items were checked in this order: ", checked_list
		##fix_master_list()
	else:
		check_items()
		
	
##	This function will compare items from today's list to the master list,
##	and sort them accordingly. It will place items not on the master list at the end.	
		
def sort_todays_items():
	
	while 0 < len(todays_list):
		if todays_list[0] in master_list:
			position = master_list.index(todays_list[0])
			todays_sorted_list.insert(position, todays_list.pop(0))
			return todays_sorted_list
		elif todays_list[0] not in master_list:
			todays_sorted_list.append(todays_list.pop(0))
			return todays_sorted_list
		else:
			print "Unknown Error."
	print "Today's list is: ", todays_sorted_list
	check_items()

	
##	This Function gets a list of items from the user and puts them into a list

def get_items():

	item = raw_input("Add item to list or \ntype 'finished' if finished \n> ")
	if 'finished' not in item:
		todays_list.append(item)
		get_items()
	elif 'finish' in item:
		print "Today's list is: ", todays_list
		return todays_list
	else:
		print "There has been an unknown error."
	sort_todays_items()
		

	
get_items()
sort_todays_items()
check_items()
print master_list

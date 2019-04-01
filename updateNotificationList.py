import csv
import sys

new_list = []
with open('streamer_list.csv', 'r') as f:
  reader = csv.reader(f)
  your_list = list(reader)
try:
	new_list = your_list[0][:]
except:
	pass


def read_file():
	with open('streamer_list.csv', 'r') as r:
		reader = csv.reader(r)
		for row in reader:
			return(row)
	
def write_file(list):
	with open('streamer_list.csv', 'w', newline='') as w:
		thewriter = csv.writer(w)
		thewriter.writerow(list)
		
def add_streamer():
	append_streamer = []
	while True:
		add_streamer = input('Enter the username of the streamer you want to get notified to: ')
		if add_streamer != 'exit':
			append_streamer.append(add_streamer)
			print(append_streamer)
		else:
			new_list.extend(append_streamer)
			write_file(new_list)
			print(new_list)
			break
		print('Type \'exit\' to stop adding')
	main()

def remove_streamers():
	print('Your current list:')
	print(new_list)
	while True:
		remove_streamer = input('Username of streamer you want to remove: ')
		if remove_streamer != 'exit':
			new_list.remove(remove_streamer)
		else:
			write_file(new_list)
			break
		print(new_list)
		print('Type \'exit\' to stop removing')
	main()

def main():
	print('Current streamers which will trigger a notification: ')
	print(read_file())
	print('\n\n')
	print('1: Add to list\n2: Remove from list\n\nPress any other key to exit program')
	user_input = input()
	
	if user_input == '1':
		add_streamer()
	elif user_input == '2':
		remove_streamers()
	else:
		sys.exit()

main()
data = open("all.csv", 'r')

for line in data:
	line = line.strip()
	line = line.split(",")
	if line[0] == "docket_no" or line[-1] == "True":
		continue
	offenses = line[1]


	


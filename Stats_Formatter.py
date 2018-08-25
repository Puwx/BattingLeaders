def statParse(statObject):
	rank = statObject[0]
	player,team = statObject[1].split('•')
	value = statObject[2].strip()
	return (rank,player,team,value)


def baseballStats():
	try:
		import bs4 as bs
		import requests
		import os
		import time
		import Stats_Formatter as SF

	except ImportError:
		print('You need the BeautifulSoup and requests library to run this script.')

	_URL = r'https://www.baseball-reference.com/leagues/MLB/2018-batting-leaders.shtml'
	urlReq = requests.get(_URL).text
	soupBase = bs.BeautifulSoup(urlReq,'lxml')

	outText = open(os.path.join(os.getcwd(),'BaseballLeaders.txt'),'w')
	outText.write('Batting Leaders for: {} \n'.format(time.strftime('%d/%m/%Y')))

	_stats  = [
				'On-Base%',
				'Batting Average',
				'Home Runs'
			  ]

	for table in soupBase.find_all('table'):
		stat = table.find('caption',class_ = 'poptip').text
		if stat in _stats:
			outText.write(stat+'\n')
			for row in table.find_all('tr'):
				data = row.find_all('td')
				fullstat = [dat.text for dat in data]
				if fullstat[0] == '':
					fullstat[0] = _Rank
				_Rank = fullstat[0]
				formRow = SF.statParse(fullstat)
				outText.write('Rank: {} - Player:{} - Team:{} - Stat: {} \n'.format(
																				formRow[0],
																				formRow[1],
																				formRow[2],
																				formRow[3]))
			outText.write('-'*60+'\n')
	outText.close()

	print('The statistics have been written to the file: {}'.format(
																	os.path.join(os.getcwd(),'BaseballLeaders.txt'))




				
					



baseballStats()
import urllib, json, math
url = "https://rsbuddy.com/exchange/summary.json"
items = []
response = urllib.urlopen(url)
data = json.loads(response.read())
nat = data['561']['sell_average']
#print nat
for item in data:
	name = data[item]['name']
	alchPrice = math.trunc(0.6*(data[item]['sp'])) #confirmed by devs alch price is trunc(0.6*Shop price) 
	price = data[item]['sell_average']
	profit = alchPrice-(price + nat)
	#print ''.join(message)
	if (profit > -15 and price > 0):
		message = (name, " buy for: ", str(price), " and Gain/Lose = ", str(profit)) #more efficient to have it here
		print ''.join(message)
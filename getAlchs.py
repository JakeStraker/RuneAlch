import urllib, json, math
url = "https://rsbuddy.com/exchange/summary.json"
items = []
response = urllib.urlopen(url)
data = json.loads(response.read())
nat = data['561']['sell_average']
#print nat
for item in data:
	name = data[item]['name']
	alchPrice = math.trunc(0.6*(data[item]['sp']))
	price = data[item]['sell_average']
	profit = alchPrice-(price + nat)
	message = (name, " buy for: ", str(price), " and Gain/Lose = ", str(profit))
	#print ''.join(message)
	if (profit > -15 and price > 0):
		print ''.join(message)
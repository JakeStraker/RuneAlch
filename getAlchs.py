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
	message = (name, " Alchs for ", str(alchPrice), " bought for: ", str(price))
	#print ''.join(message)
	if ((alchPrice-(price + nat)) > -15 and price > 0):
		print ''.join(message)
from bs4 import BeautifulSoup
import requests
import json
import sys

def scrape_data(currency, decimals = 4):
	r = requests.get("https://coinmarketcap.com/currencies/" + currency)
	soup = BeautifulSoup(r.text, 'html.parser')

	# scrap price of the asset
	price = soup.find(type="application/ld+json")
	price = price.text.split(',')[-2]
	price = price.split(':')[1]

	# scrap other data
	other_data = soup.findAll("div", {"class": "statsValue"})
	mcap = other_data[0].text[1:]
	fully_diluted_mcap = other_data[1].text[1:]
	volume = other_data[2].text[1:]
	vol_mcap_ratio = other_data[3].text
	circulating_supply = other_data[4].text.split(' ')[0]

	# insert data into dictionary
	data = dict()
	data['price'] = round(float(price), decimals)
	data['mcap'] = mcap
	data['fully_diluted_mcap'] = fully_diluted_mcap
	data['volume'] = volume
	data['vol_mcap_ratio'] = vol_mcap_ratio
	data['circulating_supply'] = circulating_supply

	# print data
	print(
		currency, "\n",
		"price:                        ", data['price'], "\n",
		"market cap:                   ", data['mcap'], "\n",
		"fully diluted mcap:           ", data['fully_diluted_mcap'], "\n",
		"volume:                       ", data['volume'],"\n",
		"volume-market cap ratio:      ", data['vol_mcap_ratio'], "\n",
		"circulating supply:           ", data['circulating_supply'], "\n",
	)

	# convert data to float
	data['price'] = price
	data['mcap'] = float(mcap.replace(',',''))
	data['fully_diluted_mcap'] = float(fully_diluted_mcap.replace(',',''))
	data['volume'] = float(volume.replace(',',''))
	data['vol_mcap_ratio'] = float(vol_mcap_ratio)
	data['circulating_supply'] = float(circulating_supply.replace(',',''))

	return data


if __name__ == "__main__":
	try:
		scrape_data(sys.argv[1])
	except:
		print("invalid cryptocurrency")










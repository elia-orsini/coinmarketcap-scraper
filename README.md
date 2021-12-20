# coinmarketcap-scraper
A scraper for CoinMarketCap. It returns the most important data about any cryptocurrency listed.

The scraper is still in development. Future plans include the creation of a RESTful API to query the price of crypto assets.

## usage
`cd` into the cloned directory and install the requirements in this way: <br /><br />
`pip3 install -r requirements.txt`
<br /><br />
With the requirements installed, run on your terminal: <br /><br />
`python3 scraper.py [NAME CRYPTOCURRENCY]`
#
#### example
`python3 scraper.py bitcoin`<br /><br />
*this will print out:* 
```
bitcoin
   price:                         61432.3433 
   market cap:                    1,158,894,617,469 
   fully diluted mcap:            1,290,079,209,174 
   volume:                        32,081,608,518 
   volume-market cap ratio:       0.02768 
   circulating supply:            18,864,568.00
```


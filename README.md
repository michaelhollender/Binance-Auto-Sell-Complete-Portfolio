# Sell All Crypto Holdings on Binance for USDT

## Description
This Binance trading bot sells all of your Crypto holdings in the event that you need to liquify your portfolio quickly.




## READ BEFORE USE
MUST Store API Keys as Environment Variables or directly add your API keys to this bot
To store your API keys as environment variable:
   
  On Windows: <br>
  set binance_api=your_api_key_here
  set binance_secret=your_api_secret_here


  On Linux: <br>
  export binance_api=your_api_key_here
  export binance_secret=your_api_secret_here

  To added your API Keys directly to this Bot(NOT RECOMMENDED!!!): <br>
  Lines 11-12: <br>
  api_key = your_api_key_here <br>
  api_secret = your_api_secret_here <br><br>

This bot will sell all of your Crypto Holdings on Binance unless the Coin is added to the following code, then the added Crypto will be skipped during the sale:

Lines 43-45: <br>
for asset, amount in assets.items(): <br>
      if asset in ["USDT", "BUSD", "BNB"]: #  skip stablecoins <br>
            continue

## 💥 Disclaimer

All investment strategies and investments involve risk of loss. 
**Nothing contained in this program, scripts, code or repository should be construed as investment advice.**
Any reference to an investment's past or potential performance is not, 
and should not be construed as, a recommendation or as a guarantee of 
any specific outcome or profit.
By using this program you accept all liabilities, and that no claims can be made against the developers or others connected with the program.

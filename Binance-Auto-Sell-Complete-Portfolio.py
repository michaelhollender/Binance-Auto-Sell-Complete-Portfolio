import os
import pandas as pd
from binance.client import Client
from dotenv import load_dotenv
from decimal import Decimal, ROUND_DOWN

# Load environement variables
load_dotenv()

# Intialize Binance client
api_key = os.environ.get("binance_api")
api_secret = os.environ.get("binance_secret")
client = Client(api_key, api_secret, tld='us') # use testnet if testing


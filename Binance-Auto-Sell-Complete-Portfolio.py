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

def gather_nonzero_assets():
    """Fetch portfolio balances > 0."""
    account = client.get_account()
    balances = account.get("balances", [])

    df = pd.DataFrame(balances, columns=["asset", "free"]).set_index("asset")
    df["free"] = df["free"].astype(float)

    return {asset: amount for asset, amount in df["free"].items() if amount > 0.0}

def adjust_quantity(symbol, quantity):
    """"Adjust quantity to Binance lot size rules."""
    info = client.get_symbol_info(symbol)
    if not info:
        return None
    
    for f in info["filters"]:
        if f["filterType"] == "LOT_SIZE":
            step_size = Decimal(f["stepSize"])
            qty = (Decimal(str(quantity)) // step_size) * step_size
            return float(qty.quantize(step_size, rounding=ROUND_DOWN))
    
    return float(quantity)



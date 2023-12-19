import login_2
from fyers_apiv3 import fyersModel
import unix_time as ut


# Initialize the FyersModel instance with your client_id, access_token, and enable async mode
fyers = fyersModel.FyersModel(client_id=login_2.client_id, token=login_2.access_token(
), is_async=False, log_path="fyers_log")


# ================== Order related functions ===================


def place_order():

    data = {
        "symbol": "NSE:IDEA-EQ",
        "qty": 1,
        "type": 2,
        "side": 1,
        "productType": "INTRADAY",
        "limitPrice": 0,
        "stopPrice": 0,
        "validity": "DAY",
        "disclosedQty": 0,
        "offlineOrder": False,
    }
    return fyers.place_order(data=data)

print(place_order())



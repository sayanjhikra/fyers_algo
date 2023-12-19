import login_2
from fyers_apiv3 import fyersModel
import unix_time as ut


fyers = fyersModel.FyersModel(client_id=login_2.client_id, token=login_2.access_token(
), is_async=False, log_path="fyers_log")


# ********=============== Data related functions ====================******

# FNO_symbol = "{Ex}: {Ex_UnderlyingSymbol}{YY}{M}{dd}{Strike}{Opt_Type}"
# max range days for 1,2,3,5,10,15,20,30,60,120,240min = 100days, 1Day t_frame = 365days


def get_data(c_symbol, c_timeFrame, c_endTime, c_startTime):

    data = {"symbol": "NSE:"+c_symbol, "resolution": str(c_timeFrame), "date_format": "0",
            "range_from": str(c_startTime), "range_to": str(c_endTime), "cont_flag": "1"}
    candles = fyers.history(data)
    return candles['candles']


def get_candle_data(c_symbol="NIFTY50-INDEX", c_timeFrame=15, r_days=250):
    loop_rotation = 0
    remind_days = 0
    candles = []
    d_limit = 100

    if r_days > d_limit:
        loop_rotation = int(r_days / d_limit)
        c_endTime = ut.unixTimeStamp()  # - (0*24*3600)
        c_startTime = c_endTime - (d_limit*24*3600)
        
        for p in range(loop_rotation):
            r_candles = get_data(c_symbol, c_timeFrame, c_endTime, c_startTime)
            r_candles.reverse()
            candles.extend(r_candles)
            c_endTime = c_startTime
            c_startTime = c_endTime - (d_limit*24*3600)

        d_remain = r_days % d_limit
        if d_remain  > 0:
            c_startTime = c_endTime - (remind_days*24*3600)
            r_candles = get_data(c_symbol, c_timeFrame, c_endTime, c_startTime)
            r_candles.reverse()
            candles.extend(r_candles)

        candles.reverse()
    else:
        c_endTime = ut.unixTimeStamp()
        c_startTime = c_endTime - (r_days*24*3600)

        candles = get_data(c_symbol, c_timeFrame, c_endTime, c_startTime)

    return candles


# candles = get_candle_data()
# for candle in candles:
#     candle[0] = ut.ut_dt(candle[0])
#     print(candle)

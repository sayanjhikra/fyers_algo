import unix_time as ut
import data_lib as dlib
import fy_library as flib


symbol_name = "NIFTY50"
symbol_type = "INDEX"
d_symbol = symbol_name+"-"+symbol_type
d_timeFrame = 15
range_days = 1200


candles = flib.get_candle_data(d_symbol, d_timeFrame, range_days)

f_name = symbol_name+"-"+str(d_timeFrame)+"-"+str(range_days)+"days"
dlib.store_data(f_name, candles)

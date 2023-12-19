import csv
import fy_library as flib

def store_data (csv_file_name,data):
    #data must be given in list type
    with open("db/"+csv_file_name+".csv", "w") as f:
        csv_writer = csv.writer(f)
        for candle in data:
            csv_writer.writerow(candle)


def read_data (csv_file_name):
    with open("db/"+csv_file_name+".csv", "r") as data:
        csv_files = csv.reader(data)
        candles = []
        for lines in csv_files:
            if len(lines):
                p_list = list(map(float, lines))
                p_list[0] = int(p_list[0])
                p_list[5] = int(p_list[5])
                candles.append(p_list)
    return candles

# ==========to store data===========

# symbol_name = "NIFTY50"
# symbol_type = "INDEX"
# d_symbol = symbol_name+"-"+symbol_type
# d_timeFrame = 15
# range_days = 1200
# f_name = symbol_name+"-"+str(d_timeFrame)+"-"+str(range_days)+"days"

# candles = flib.get_candle_data(d_symbol, d_timeFrame, range_days)
# store_data(f_name, candles)
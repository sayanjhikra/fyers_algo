import fy_library as flib
import data_lib as dlib
import unix_time as ut
# import os
# ['timeStamp','o','h','l','c','V','c_color','[s/r_zone,z1,z2]',]

# import db_connect as db
# mycol = db.mydb['support']
# mycol_1 = db.mydb['resistance']
# rec = {"type": 'support',
#     "name": [1,2,3,[5,6,7,8]]}
# for x in mycol.find({"type": "support"}):
#   print(type(x))

def find_sr(candles):
    for x in range(len(candles)-1):
        candles[x][0] = ut.ut_dt(candles[x][0])
        if candles[x][6] == 'green' and candles[x+1][6] == 'red' and candles[x][0][3]!=15:
            candles[x].insert(7, ['r_zone', candles[x][4], candles[x][2]
                              if candles[x][2] > candles[x+1][2] else candles[x+1][2]])
            # rec = {"type": candles[x][7][0],
            #        "time": candles[x][0],
            #        "z1": candles[x][7][1],
            #        "z2": candles[x][7][2]
            #        }
            # mycol_1.insert_one(rec)
            

        elif candles[x][6] == 'red' and candles[x+1][6] == 'green'and candles[x][0][3]!=15:
            candles[x].insert(7, ['s_zone', candles[x][4], candles[x][3]
                              if candles[x][3] < candles[x+1][3] else candles[x+1][3]])
        else:
            candles[x].insert(7, [''])
        print(candles[x])
    return candles


def add_candle_color(candles):
    for x in range(len(candles)):
        if candles[x][1] > candles[x][4]:
            candles[x].insert(6, 'red')
        else:
            candles[x].insert(6, 'green')
    return candles

# def find_trend(candles):

# def sma(candles, rang):







d_candle = dlib.read_data("NIFTY50-15-1200days")

candles = add_candle_color(d_candle)

for candle in candles:
    candle[0] = ut.ut_dt(candle[0])
    print(candle)

print(len(d_candle))






    

from fyers_apiv3.FyersWebsocket import data_ws
import login_2


def onmessage(message):

    # print("Response:", message)

    # print(message['symbol'])
    if message['symbol'] == "NSE:NIFTY50-INDEX" and message['ltp'] > 19350:
        print(message['ltp'])
    else:
        print('down')
  

    # if message['symbol'] == "NSE:NIFTY50-INDEX" and message['ltp'] > 19300:
    #     data_type = "SymbolUpdate"
    #     symbols_to_unsubscribe = ["NSE:NIFTY50-INDEX", "NSE:NIFTYBANK-INDEX"]
    #     fyers.unsubscribe(symbols=symbols_to_unsubscribe, data_type=data_type)


def onerror(message):
    print("Error:", message)


def onclose(message):
    print("Connection closed:", message)


def onopen():
    data_type = "SymbolUpdate"
    # data_type = "DepthUpdate"

    symbols = ["NSE:NIFTY50-INDEX"]
    # symbols = ["NSE:NIFTY50-INDEX", "NSE:NIFTYBANK-INDEX"]
    fyers.subscribe(symbols=symbols, data_type=data_type)

    fyers.keep_running()


fyers = data_ws.FyersDataSocket(
    access_token=login_2.access_token(),
    log_path="fyers_log",
    litemode=False,
    write_to_file=False,
    reconnect=True,
    on_connect=onopen,
    on_close=onclose,
    on_error=onerror,
    on_message=onmessage
)

fyers.connect()

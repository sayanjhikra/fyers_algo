from fyers_apiv3 import fyersModel
import datetime
import os
import pyautogui as pt
import pyperclip
import webbrowser
import user 

client_id = user.client_id
secret_key = user.secret_key
fyres_pin = user.fyres_pin



def get_access_token():
    session = fyersModel.SessionModel(
        client_id=client_id,
        secret_key=secret_key,
        redirect_uri='http://127.0.0.1:5000/login',
        response_type="code",
        grant_type="authorization_code"
    )

    webbrowser.open(session.generate_authcode())
    pt.sleep(4.5)    # wait for grnarate auth code
    pt.hotkey('ctrl', 'l')
    pt.sleep(.1)
    pt.hotkey('ctrl', 'c')
    url = str(pyperclip.paste())
    pt.hotkey('ctrl', 'w')
    pt.hotkey('alt', 'tab')
    auth_code = url.split("&auth_code=")[1].split("&state=")[0]

    session.set_token(auth_code)
    a_token = session.generate_token()
    access_token = a_token["access_token"]
    return access_token


today = str(datetime.date.today())
# Previous_Date = datetime.datetime.today() - datetime.timedelta(days=1)
# previousday = str(Previous_Date).split(" ")[0]


def fyres_pin_login(pin):
    webbrowser.open('https://login.fyers.in/')
    pt.sleep(2)
    for x in fyres_pin:
        pt.press(x)
    pt.press('enter')
    pt.sleep(.5)
    pt.hotkey('ctrl', 'w')


def access_token():
    if os.path.exists("accessToken/"+today+".txt"):
        token_txt = open("accessToken/"+today+".txt", "r")
        return token_txt.read()

    else:
        for item in os.listdir("accessToken/"):
            if item.endswith(".txt"):
                os.remove("accessToken/"+item)

        token = open("accessToken/"+today+".txt", "a")
        try:
            token.write(get_access_token())
        except:
            fyres_pin_login(fyres_pin)
            token.write(get_access_token())
            pass

        token.close()
        token_txt = open("accessToken/"+today+".txt", "r")
        return token_txt.read()


# print(access_token())
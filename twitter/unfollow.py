from twython import Twython
import configparser

config = configparser.RawConfigParser()
config.read('enter.tw')
APP_KEY=config.get('MINEKRAFT','API_KEY')
APP_SECRET=config.get('MINEKRAFT','API_SECRET')
OAUTH_TOKEN=config.get('MINEKRAFT','ACCESS_KEY')
OAUTH_TOKEN_SECRET=config.get('MINEKRAFT','ACCESS_SECRET')
tw =Twython(APP_KEY, APP_SECRET,OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

vec = tw.get_home_timeline()
for i in vec:
    print(i)


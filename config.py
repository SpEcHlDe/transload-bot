import os

class Config(object):
	token = os.environ.get("TG_BOT_TOKEN", "")#"1116352147:AAFCW2thgkhzv0N6pkNDTBAU6Q88RkUGzIg"
	host_url = os.environ.get("HOST_URL", "")#"https://rapeed-leech.herokuapp.com"

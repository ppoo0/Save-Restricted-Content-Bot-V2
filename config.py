# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "21103068"))
API_HASH = getenv("API_HASH", "633ab5bfab52d8763ffc6da7a9b2294a")
BOT_TOKEN = getenv("BOT_TOKEN", "")
OWNER_ID = list(map(int, getenv("OWNER_ID", "6268938019").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://telegram-bot:ydk4Nf7BxRREklv9@test.1r1ni.mongodb.net/?retryWrites=true&w=majority&appName=test")
LOG_GROUP = getenv("LOG_GROUP", "-1002208385419")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002036282115"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "0"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "500"))
WEBSITE_URL = getenv("WEBSITE_URL", "upshrink.com")
AD_API = getenv("AD_API", "39048a8ec854a66dcb05453b3d5deca90abeb533")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", None)
INSTA_COOKIES = getenv("INSTA_COOKIES", None)

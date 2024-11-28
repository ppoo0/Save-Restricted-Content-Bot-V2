# devgaganin
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "29754529"))
API_HASH = getenv("API_HASH", "dd54732e78650479ac4fb0e173fe4759")
BOT_TOKEN = getenv("BOT_TOKEN", "7309382995:AAFUSvQDbEuCgK3oKHPspvE24JVukYv-70A")
OWNER_ID = int(getenv("OWNER_ID", "6268938019"))
MONGODB_CONNECTION_STRING = getenv("MONGO_DB", "mongodb+srv://test-bot:wS6CdEdQIbgEavqE@test.9bg9n.mongodb.net/?retryWrites=true&w=majority&appName=test")
LOG_GROUP = int(getenv("LOG_GROUP", "-1002208385419"))
FORCESUB = getenv("FORCESUB", "neetumamvoca")
DEFAULT_SESSION = getenv("DEFAULT_SESSION", "BQHGBKEAC_tL55DMPW4lcBsNSYaMMl_AF916_PaYhVzfEQnty_C7jsLXGG8bIzFNoMgUumzCWP0o-3onJ21iQmxL15IBr10ehDF3XkCBWX9xgvmKjS0J06wiv78iJoP0bKzmwgUJCKEf-ALLmHvu98wb1MyWqEl43xSG52r7_yvIknwEY1gNkvwa5OVY_NtQzqkIqzDyacnM0FrKk4lybBwoTRYCALWdryv4y_YjSC8LOBfmM7L6cSOrkQpcKbQqHRvRFe9J1lKtH9EkCd48sJTk-E3nGd7TrtkahjeOP1FiacQKiNr-ponWDp_CCeDESgJlAfgjUfk8C3_oUc-fWoWkpnwZSAAAAAHATApSAA") # this is jkust to help if you dont want to force your bot user to login or if they not interested

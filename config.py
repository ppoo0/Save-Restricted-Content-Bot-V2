# devgaganin
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "23328567"))
API_HASH = getenv("API_HASH", "8eef6df76083087af5fe2d6fef73debe")
BOT_TOKEN = getenv("BOT_TOKEN", "7524865501:AAEeOuoaQATrXujou4sZlzwdiS9fMDQyqkA")
OWNER_ID = int(getenv("OWNER_ID", "6268938019"))
MONGODB_CONNECTION_STRING = getenv("MONGO_DB", "mongodb+srv://telegram-bot:ydk4Nf7BxRREklv9@test.1r1ni.mongodb.net/?retryWrites=true&w=majority&appName=test")
LOG_GROUP = int(getenv("LOG_GROUP", "-1002208385419"))
FORCESUB = getenv("FORCESUB", "neetumamvoca")
DEFAULT_SESSION = getenv("DEFAULT_SESSION", "") # this is jkust to help if you dont want to force your bot user to login or if they not interested

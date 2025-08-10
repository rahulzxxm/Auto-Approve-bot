
from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "22609670"))
    API_HASH = getenv("API_HASH", "3506d8474ad1f4f5e79b7c52a5c3e88d")
    BOT_TOKEN = getenv("BOT_TOKEN", "7680901418:AAGoc-69uZG_V7TAgre5ssBKK17ZRgRMfo4")
    FSUB = getenv("FSUB", "Tigerxy09")
    CHID = int(getenv("CHID", "-1002215906991"))
    SUDO = list(map(int, getenv("SUDO", "5881684718 123456789").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://californiamaverick38:Rahul#99@cluster0.6pmjjah.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    
cfg = Config()

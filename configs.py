from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "26744850"))
    API_HASH = getenv("API_HASH", "6ec3f450bb9e9ab23f050dbafe6acbb6")
    BOT_TOKEN = getenv("BOT_TOKEN", "6547420147:AAED2CrXzH-rlrM3i56Nvl9Tvkj-QP31ppc")
    FSUB = getenv("FSUB", "LegendBotz")
    CHID = int(getenv("CHID", "-1001590951427"))
    SUDO = list(map(int, getenv("SUDO").split()))
    MONGO_URI = getenv("MONGO_URI", "")
    
cfg = Config()

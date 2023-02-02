import os
import logging
class Config:                                                                   
    API_ID = int(os.environ.get("API_ID", "23560088"))
    API_HASH = os.environ.get("API_HASH", "999c01704d5c417749a98f4b8785fe88")       
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5885915327:AAFP59AofxBWAszWyhKndr-NX_N-7Fg82VA")
    BOT_SESSION = os.environ.get("BOT_SESSION", "forwardbot")
    OWNER_ID = os.environ.get("OWNER_ID", "5695317827")                             
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://amit:amit@cluster0.skr2tgu.mongodb.net/?retryWrites=true&w=majority")  
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluste0")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Data')
    SESSION = os.environ.get("SESSION", "BQC-ieht_wMEV-SngrcBn_FzwI-YJjuzHr6dsMV1zUQUSAahrkNuQtjMpA9GppEnsHkntrWkg3paqp8MA-aC7rkKSkQ4XvIlO7LuSOV9mNYhYZhjWvxxXC2qZwUOb3I5vR73wa9Lq9dVDLi0upyWa06CTaExMkU4fXvmHA0rzBb3pzC49POnhvDzF0yaIoVUszbzbP3tuSJwdLnNL3xDMzECFlmlCEOMPJ5xC4GlQAIpKd-wsHM-G55mpWXQjp3eeVfZj4b8L2IYEQsjsSeDcTr76YaFTt_RVFZgYAu2kUinPR7IZO1RQnGcHC1Boj5NpRi5lwsJKGlJQWplqFw6p9pHAAAAAVN3p0MA")   
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001512978679"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "fordaranbot")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)

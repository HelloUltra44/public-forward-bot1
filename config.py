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
    SESSION = os.environ.get("SESSION", "BQFnf5gAFQiTJU1THN9bnj6orWqzYYnVtBRjIbTO1gUJdrI6uqteopn0pvNV9Y0U2t9Yhs1xJvO8Aa5KYbG5q7RDcdWeQq2RYGl8RQt59MCUHzViUEGTN3XtacbavhXIBlRYjM-LF2KOCIhLoko1jBr583GAHIp-Z0IRXl3gSYftG47vljY8tWCGDzRTO-fkc5Hs2hGUOpRMt3ic2pIja5Ko_99iOSzDWYkeftP2zU8O6ffeF2O_9GwODXpgYIm94oQutA1XjyxhLS9lN2ZtO6itzT01juvNZUFn-lUE5wbYRbY-FomYW7hk8Kozzy5sPkEggBOMnTy22054KZpJCPdxBWTDJgAAAAFTd6dDAA")   
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001512978679"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "fordaranbot")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)

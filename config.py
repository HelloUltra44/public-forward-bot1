import os
import logging
class Config:                                                                   
    API_ID = int(os.environ.get("API_ID", "23560088"))
    API_HASH = os.environ.get("API_HASH", "999c01704d5c417749a98f4b8785fe88")       
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5896381925:AAEhvUfE7QTElvyi_00Geagz4Wttw_OC908")
    BOT_SESSION = os.environ.get("BOT_SESSION", "forwardbot")
    OWNER_ID = os.environ.get("OWNER_ID", "5410723702")                             
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://amit:amit@cluster0.fdlnmlh.mongodb.net/?retryWrites=true&w=majority")  
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluste0")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Data')
    SESSION = os.environ.get("SESSION", "BQCWmGI1a9zqqIg9kgUQ6ZoAShV53TcpPw0YRM2zPjfaCacWXa4H7FXgDPbktV9-YE-DV3O5iyqSpbNGDDQsny0ieHHlQkWmskf_tNBI3OCfCFy5wi6K2YB2duy64tDEcz3TTpSClc8XFRIiIHTdygFguDa9ro4aWFfuW07JQCNYjCPwdsgOf7SpdbCh_VAPGAWEfPHAZC2r9ChQ72E35FpohpT5QG3ag10bMAOkTG5HU5xtVpUjx2rmWk7nOgBbEX3q18501ZJVTYlYBHEZeioF0ogFGi7rck7G8wgyOkHkxj6MgZhnQMPn6R1s3tM6XgWkj_lWW0_p2GLTNhdN5vUKAAAAAUKBF3YA")   
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001615615101"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "fordaranbot")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)

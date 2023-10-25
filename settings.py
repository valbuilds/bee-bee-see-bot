# import modules
import os
from dotenv import load_dotenv

load_dotenv()
import json

# import other files
import logging
from logging.config import dictConfig

# make config accessible
cfile = open("config.json")
cdata = json.load(cfile)


# access config using this
class Config:
    # enable debug version
    debug: bool = True
    # token
    token: str = os.getenv("token")

    # debug-specific config
    class Debug:
        guildid: int = cdata["debug"]["guildid"]
        suggestionchannelid: int = cdata["debug"]["suggestionchannelid"]

    # main-specific config
    class Main:
        guildid: int = cdata["main"]["guildid"]
        suggestionchannelid: int = cdata["main"]["suggestionchannelid"]


# logging stuff
loggingconfig = {
    "version": 1,
    "disabled_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(levelname)-10s - %(asctime)s - %(module)-15s : %(message)s"
        },
        "standard": {"format": "%(levelname)-10s - %(name)-15s : %(message)s"},
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "standard",
        },
        "console2": {
            "level": "WARNING",
            "class": "logging.StreamHandler",
            "formatter": "standard",
        },
        "file": {
            "level": "INFO",
            "class": "logging.FileHandler",
            "filename": "logs/infos.log",
            "mode": "w",
            "formatter": "verbose",
        },
    },
    "loggers": {
        "bot": {"handlers": ["console"], "level": "INFO", "propagate": False},
        "discord": {
            "handlers": ["console2", "file"],
            "level": "INFO",
            "propagate": False,
        },
    },
}

dictConfig(loggingconfig)

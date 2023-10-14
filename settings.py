import os
import json
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv('token')

class Config:
    file = open('config/main.json')
    data = json.load(file)

    prefix = data['prefix']

    main_guild_id = data['main_guild_id']
    bloopers_channel = data['bloopers_channel']
    suggestions_channel = data['suggestions_channel']
    home_guild_id = data['home_guild_id']
    home_suggestions_channel = data['home_suggestions_channel']
import requests


# This function essentially retrieves all information from the teamplanner json
def get_tft_data():
    url = "https://raw.communitydragon.org/latest/plugins/rcp-be-lol-game-data/global/default/v1/tftchampions-teamplanner.json"
    res = requests.get(url)
    return res.json()

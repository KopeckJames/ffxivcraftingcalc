import datetime










url = "https://universalis.app/api/v2/extra/stats/trade-volume?"
world = input("What world are you searching in? (ie Gilgamesh, Siren, Cactaur...)")
dcName = input("What Data Center? (ie Aether, Dynamis, Light)")
item = input("What is the item id from the list?")
start_time = input("What is the start time in miliseconds since the UNIX Epoch?")
end_time = input("What is the time in miliseconds since the unix epoch is over. curren = -1")
universalis_url = f"{url}world={world}&dcName={dcName}&to={end_time}"

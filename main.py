from services.traffic_api import TrafficAPI
from services.map_manager import MapManager

api = TrafficAPI()
map_manager = MapManager()

api.get_data()
map_manager.show_map()
from logger import setup_logging, get_logger
from services.dolibarr import Dolibarr
from frigate.mqtt_client import start_mqtt_client

setup_logging()

logger = get_logger("MAIN FRIGATE")
dolibarr = Dolibarr(
    host="http://10.24.24.23/api/index.php/equipmentsapi",
    entrypoint_get_camera_list="cameras?sortfield=t.rowid&sortorder=ASC&limit=100",
    entrypoint_push_event="autovisionhistorys",
    api_key="e779gEMqf747hTYA1lv7R7BC4ToyAisD",
)

if __name__ == "__main__":
    start_mqtt_client()

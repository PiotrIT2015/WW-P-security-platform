import re

DEFAULT_WINDOW_WIDTH = 1200
DEFAULT_WINDOW_HEIGHT = 800

APP_NAME = "WW-P Security Platform"

TORNADO_PORT = 8889

MYSQL_PORT = 3306

IP_ADDRESS_RE = re.compile(
    r"^(?=.*[^\.]$)((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.?){4}$"
)

MASK_BINARY_RE = re.compile(
    r"^1*0*$"
)
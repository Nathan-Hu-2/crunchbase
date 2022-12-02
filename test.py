from fake_useragent import UserAgent

from stem import Signal
from stem.control import Controller
def switchIP():
    with Controller.from_port(port = 3000) as controller:
        controller.authenticate()
        controller.signal(Signal.NEWNYM)

def delay() -> None:
    time.sleep(random.uniform(2, 7))
    return None
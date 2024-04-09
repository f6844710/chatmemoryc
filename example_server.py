import logging
from chatmemoryc.server import ChatMemoryServer

ANTHROPIC_APIKEY = "sk-ant-**************************************************"

logger = logging.getLogger()
logger.setLevel(logging.INFO)
log_format = logging.Formatter("%(asctime)s %(levelname)8s %(message)s")
streamHandler = logging.StreamHandler()
streamHandler.setFormatter(log_format)
logger.addHandler(streamHandler)

logger.info("starting sever...")

server = ChatMemoryServer(api_key=ANTHROPIC_APIKEY)
server.start()

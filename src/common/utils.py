import requests
import logging
from django.conf import settings

logger = logging.getLogger('dev.'+__name__)


def send_msg_to_broker(msg, topic=None):
    """
    send msg (as first param in args) to crossbar in specific topic
    """
    topic = topic or settings.CROSSBAR['topic']

    try:
        r = requests.post(settings.CROSSBAR['url'], json={"topic": topic, "args": [msg]},
                          timeout=settings.CROSSBAR['timeout'])
        r.raise_for_status()
    except Exception as e:
        logger.debug('failed to send to broker: {0}'.format(e))

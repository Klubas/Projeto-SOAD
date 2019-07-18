import logging
import sys

__LOG_LEVEL__ = logging.DEBUG
__LOG_STREAM__ = sys.stderr

logging.basicConfig(stream=__LOG_STREAM__, level=__LOG_LEVEL__)
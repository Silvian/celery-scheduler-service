import celery
import logging

logger = logging.getLogger(__name__)


@celery.task()
def print_hello_world_task():
    logger.info("Hello World")

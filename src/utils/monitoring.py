"""
Monitoring and logging utilities.
"""

import functools
import logging
import time
from typing import Any, Callable
from prometheus_client import Counter, Gauge, Histogram

# Prometheus metrics
REQUEST_COUNT = Counter('request_count', 'Number of requests', ['agent'])
ERROR_COUNT = Counter('error_count', 'Number of errors', ['agent'])
PROCESSING_TIME = Histogram('processing_time_seconds', 'Time spent processing', ['agent'])
ACTIVE_REQUESTS = Gauge('active_requests', 'Number of active requests', ['agent'])

def monitor(func: Callable) -> Callable:
    """Decorator for monitoring agent functions.
    
    Args:
        func: Function to monitor
        
    Returns:
        Wrapped function with monitoring
    """
    @functools.wraps(func)
    async def wrapper(self, *args, **kwargs):
        agent_name = self.__class__.__name__
        
        REQUEST_COUNT.labels(agent=agent_name).inc()
        ACTIVE_REQUESTS.labels(agent=agent_name).inc()
        
        start_time = time.time()
        try:
            result = await func(self, *args, **kwargs)
            return result
        except Exception as e:
            ERROR_COUNT.labels(agent=agent_name).inc()
            raise
        finally:
            PROCESSING_TIME.labels(agent=agent_name).observe(time.time() - start_time)
            ACTIVE_REQUESTS.labels(agent=agent_name).dec()
            
    return wrapper

def setup_logging(level: str = "INFO"):
    """Setup logging configuration.
    
    Args:
        level: Logging level
    """
    logging.basicConfig(
        level=level,
        format='%(asctime)s [%(levelname)s] %(name)s: %(message)s',
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler('app.log')
        ]
    )
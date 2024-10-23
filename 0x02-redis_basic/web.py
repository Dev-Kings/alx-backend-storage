#!/usr/bin/env python3
""" Redis Module """

from functools import wraps
import redis
import requests
from typing import Callable

# Initialize Redis client
redis_client = redis.Redis()

def count_requests(method: Callable) -> Callable:
    """Decorator that counts how many times a URL was accessed and caches its content."""
    @wraps(method)
    def wrapper(url: str) -> str:
        """ Wrapper function for decorator logic """
        # Increment the count for the URL
        redis_client.incr(f"count:{url}")
        
        # Check if the HTML is cached
        cached_html = redis_client.get(f"cached:{url}")
        if cached_html:
            return cached_html.decode('utf-8')  # Return cached content
        
        # Fetch the HTML content and cache it with a 10-second expiration
        html = method(url)
        redis_client.setex(f"cached:{url}", 10, html)
        return html

    return wrapper

@count_requests
def get_page(url: str) -> str:
    """Obtain the HTML content of a URL"""
    try:
        req = requests.get(url)
        req.raise_for_status()  # Raise HTTPError for bad responses
        return req.text
    except requests.RequestException as e:
        # Handle potential network or HTTP errors
        return f"Error: {e}"



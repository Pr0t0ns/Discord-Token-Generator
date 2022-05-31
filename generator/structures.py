import threading
import time
import random
from itertools import cycle
from http.client import HTTPSConnection


class Proxy:
    def __init__(self, proxy):
        hostname, port = proxy.split(":", 1)
        self.hostname = hostname
        self.port = int(port)
        self.hostname_to_connection = {}

    def get_connection(self, hostname, **kwargs) -> HTTPSConnection:
        hostname = hostname.lower()

        if hostname in self.hostname_to_connection:
            return self.hostname_to_connection[hostname]
        else:
            conn = HTTPSConnection(self.hostname, self.port, **kwargs)
            conn.set_tunnel(hostname, 443)
            self.hostname_to_connection[hostname] = conn
            return conn

class ProxyHandler:
    def __init__(self, pool, proxy):
        self.pool = pool
        self.proxy = proxy
    
    def __enter__(self):
        return self.proxy

    def __exit__(self, err, *_):
        if not err:
            self.pool.alive.append(self.proxy)

class ProxyPool:
    def __init__(self, proxies):
        random.shuffle(proxies)
        self.proxy_iter = cycle(proxies)
        self.alive = []
        self.lock = threading.Lock()

    def __next__(self) -> Proxy:
        with self.lock:
            if self.alive:
                proxy = self.alive.pop()
            else:
                proxy = Proxy(next(self.proxy_iter))
            return ProxyHandler(self, proxy)

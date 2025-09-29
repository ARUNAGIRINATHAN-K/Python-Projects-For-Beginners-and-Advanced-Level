import time

class TokenBucket:
    def __init__(self, rate, capacity):
        self.rate = rate
        self.capacity = capacity
        self.tokens = capacity
        self.last_refill = time.time()

    def allow_request(self):
        now = time.time()
        elapsed = now - self.last_refill
        refill = elapsed * self.rate
        self.tokens = min(self.capacity, self.tokens + refill)
        self.last_refill = now

        if self.tokens >= 1:
            self.tokens -= 1
            return True
        return False

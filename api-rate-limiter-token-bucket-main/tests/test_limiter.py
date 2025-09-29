import unittest
import time
from app.limiter import TokenBucket

class TestTokenBucket(unittest.TestCase):

    def test_allow_request_within_limit(self):
        bucket = TokenBucket(rate=2, capacity=5)
        allowed = [bucket.allow_request() for _ in range(5)]
        self.assertTrue(all(allowed))  # All 5 should be allowed

    def test_request_exceeds_capacity(self):
        bucket = TokenBucket(rate=1, capacity=3)
        [bucket.allow_request() for _ in range(3)]
        self.assertFalse(bucket.allow_request())  # 4th should be blocked

    def test_refill_after_wait(self):
        bucket = TokenBucket(rate=1, capacity=2)
        [bucket.allow_request() for _ in range(2)]
        time.sleep(2)  # Wait to allow refill
        self.assertTrue(bucket.allow_request())  # Should be allowed again

if __name__ == '__main__':
    unittest.main()

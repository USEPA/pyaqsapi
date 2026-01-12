"""Unit tests for TokenBucketRateLimiter."""

import time
import threading

import pytest

from pyaqsapi.helperfunctions import TokenBucketRateLimiter, RATE_LIMIT_CALLS, RATE_LIMIT_PERIOD


def test_rate_limiter_basic_functionality():
    """Test that rate limiter enforces minimum interval between calls."""
    limiter = TokenBucketRateLimiter(calls=10, period=60)
    
    start_time = time.time()
    limiter.acquire()
    first_call_time = time.time()
    
    limiter.acquire()
    second_call_time = time.time()
    
    # Should have waited at least 6 seconds (60/10) between calls
    elapsed = second_call_time - first_call_time
    assert elapsed >= 5.9, f"Expected at least 6 seconds, got {elapsed}"  # Allow small margin for timing


def test_rate_limiter_multiple_calls():
    """Test that rate limiter properly spaces multiple calls."""
    limiter = TokenBucketRateLimiter(calls=5, period=10)  # 5 calls per 10 seconds = 2 seconds per call
    
    times = []
    for _ in range(3):
        limiter.acquire()
        times.append(time.time())
    
    # Check intervals between calls
    interval1 = times[1] - times[0]
    interval2 = times[2] - times[1]
    
    # Each interval should be approximately 2 seconds (allow 0.1s margin)
    assert interval1 >= 1.9, f"First interval should be ~2s, got {interval1}"
    assert interval2 >= 1.9, f"Second interval should be ~2s, got {interval2}"


def test_rate_limiter_thread_safety():
    """Test that rate limiter is thread-safe."""
    limiter = TokenBucketRateLimiter(calls=10, period=10)  # 10 calls per 10 seconds = 1 second per call
    
    call_times = []
    lock = threading.Lock()
    
    def make_call():
        limiter.acquire()
        with lock:
            call_times.append(time.time())
    
    # Create 5 threads that all try to make calls simultaneously
    threads = [threading.Thread(target=make_call) for _ in range(5)]
    
    start_time = time.time()
    for thread in threads:
        thread.start()
    
    for thread in threads:
        thread.join()
    
    end_time = time.time()
    
    # All calls should complete, and they should be spaced out
    assert len(call_times) == 5
    # Total time should be at least 4 seconds (5 calls with 1s intervals)
    assert (end_time - start_time) >= 3.9, f"Expected at least 4 seconds for 5 calls, got {end_time - start_time}"


def test_rate_limiter_default_values():
    """Test that rate limiter uses correct default values."""
    limiter = TokenBucketRateLimiter()
    
    assert limiter.calls == RATE_LIMIT_CALLS
    assert limiter.period == RATE_LIMIT_PERIOD
    assert limiter.min_interval == RATE_LIMIT_PERIOD / RATE_LIMIT_CALLS


def test_rate_limiter_first_call_immediate():
    """Test that first call doesn't wait."""
    limiter = TokenBucketRateLimiter(calls=10, period=60)
    
    start_time = time.time()
    limiter.acquire()
    elapsed = time.time() - start_time
    
    # First call should be immediate (less than 0.1 seconds)
    assert elapsed < 0.1, f"First call should be immediate, took {elapsed} seconds"


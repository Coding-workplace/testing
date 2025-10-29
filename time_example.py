import time, timeit
# Performance Measurement

def test_fun():
    print("Hello, World")

# naive way
start = time.perf_counter()
test_fun()
end = time.perf_counter()
print(f"Elapsed: {end - start:.6f}s")

# Better way to use timeit for testing
test_times = timeit.repeat(test_fun, repeat=5, number=10000)
print(f"Best test time: {min(test_times):.6f} seconds")
print(f"Averate test time: {sum(test_times)/len(test_times):.6f} seconds")
print(f"Worst test time: {max(test_times):.6f} seconds")


# Retry with exponential backoff using monotonic
max_wait = 30.0
deadline = time.monotonic() + max_wait
attempt = 0
while True:
    attempt += 1
    try:
        # do_network_call()
        break
    except Exception: #TransientError:
        if time.monotonic() >= deadline:
            raise
        wait = min(2 ** attempt, 5.0)
        time.sleep(wait)

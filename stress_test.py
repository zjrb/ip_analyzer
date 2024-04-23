from ip_address import ip_address
import time
import random

address_counter = ip_address()

results = "\n\n\nResults of the tests"


def test_20_million_inserts() -> str:
    start = time.time()
    for i in range(20000000):
        address_counter.requestHandled(str(i))
    return f"\n20 million inserts runs in {time.time()-start}"


def test_get_100_time() -> str:
    start = time.time()
    address_counter.top100()
    return f"\nGet top 100 runs in {time.time()-start}"


def test_get_100_accuracy() -> str:
    tests = [str(i) for i in range(100, 200)]
    for test in tests:
        for i in range((int(test) + 1) - 100):
            address_counter.requestHandled(test)

    actual = address_counter.top100()
    assert tests[::-1] == actual
    return f"\nTests match the actual for test 100"


def test_insert_1000_on_existing_address() -> str:
    start = time.time()
    for i in range(1000):
        address_counter.requestHandled("1")
    assert max(address_counter.heap) == 1001
    return f"\n1k inserts on existing address runs in {time.time()-start}"


def test_random_inserts() -> str:
    start = time.time()
    insert_dict = {}
    number_of_inserts = 10000
    for i in range(10000, 20000):
        key = str(i)
        random_int = random.randint(0, 10)
        number_of_inserts += random_int
        for j in range(random_int):
            address_counter.requestHandled(key)
        insert_dict[key] = random_int
    result = f"\n{number_of_inserts} random inserts ran in {time.time()-start}"
    for key in insert_dict:
        assert insert_dict[key] + 1 == address_counter.address_to_count[key]

    return result


def test_single_insert() -> str:
    start = time.time()
    address_counter.requestHandled("1000")
    return f"\nSingle Insert ran in {time.time()-start}"


def test_clear() -> str:
    start = time.time()
    address_counter.clear()
    result = f"\nClear ran in {time.time()-start}"

    assert len(address_counter.heap) == 0
    assert len(address_counter.address_to_count) == 0
    assert len(address_counter.count_to_address) == 0
    return result


results += test_20_million_inserts()
results += test_get_100_time()

results += test_get_100_accuracy()

results += test_insert_1000_on_existing_address()
results += test_get_100_time()

results += test_random_inserts()
results += test_get_100_time()

address_counter.print_top_100()
results += test_single_insert()
results += test_clear()

print(results)

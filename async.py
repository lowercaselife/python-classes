#!/usr/bin/env python3
import asyncio
import random
from time import perf_counter
from typing import List

async def async_generator() -> float:
    """Generates random numbers asynchronously."""
    for _ in range(10):
        await asyncio.sleep(1)  # simulate I/O operation
        yield random.random()

async def async_comprehension() -> List[float]:
    """Collect random numbers using async comprehension."""
    return [i async for i in async_generator()]

async def measure_runtime() -> float:
    """Measure the runtime of running four async comprehensions in parallel."""
    start_time = perf_counter()
    tasks = [asyncio.create_task(async_comprehension()) for _ in range(4)]
    await asyncio.gather(*tasks)
    elapsed_time = perf_counter() - start_time
    return elapsed_time

# Running the measure_runtime function to print the result
if __name__ == "__main__":
    runtime = asyncio.run(measure_runtime())
    print(f"Runtime for four parallel comprehensions: {runtime:.2f} seconds")

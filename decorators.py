import functools
import time
import asyncio

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        func(*args, **kwargs)
        finish_time = time.perf_counter()

        print(
            f'''
            Function {func.__name__!r}
            executed in 
            {(finish_time-start_time)}
            '''
        )
    return wrapper


def async_timer(func):
    async def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = await func(*args, **kwargs)
        finish_time = time.perf_counter()
        print(
            f'''
            Function {func.__name__!r}
            executed in 
            {(finish_time-start_time)}
            '''
        )
        return result
    return wrapper


async def slow_operation():
    await asyncio.sleep(1)
    print("Slow operation complete.") 
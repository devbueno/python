import asyncio

async def task1():
    print("Starting task 1...")
    await asyncio.sleep(2)  # Simulate a long-running task
    print("Task 1 completed.")

async def task2():
    print("Starting task 2...")
    await asyncio.sleep(1)  # Simulate another long-running task
    print("Task 2 completed.")

async def main():
    await asyncio.gather(task1(), task2())

asyncio.run(main())

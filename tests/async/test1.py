import asyncio

async def delayed_hi(seconds: int):
    await asyncio.sleep(seconds)
    print(f"Hi after {seconds}")

async def main():
    await asyncio.gather(
        delayed_hi(1),
        delayed_hi(5)
    )

asyncio.run(main())
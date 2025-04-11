import asyncio
from agents import Agent, Runner


async def main():
    agent = Agent(
        name="Assistant",
        instructions="You only respond in haikus.",
    )

    result = await Runner.run(agent, "Tell me about recursion in programming.")

    print(result.raw_responses)


if __name__ == "__main__":
    asyncio.run(main())

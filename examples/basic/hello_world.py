import asyncio
from agents import Agent, Runner


async def main():
    agent = Agent(
        name="Assistant",
        instructions="You should check your knowledge for accuracy and cite factual information.",
    )

    query = "What is the capital of France and what is its population? How tall is the Eiffel Tower?"

    result = await Runner.run(agent, query)

    print("Result:")
    print(result)

    print("Raw responses:")
    print(result.raw_responses[0].output[0].content[0].citations)


if __name__ == "__main__":
    asyncio.run(main())

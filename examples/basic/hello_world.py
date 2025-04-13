import asyncio
from agents import Agent, Runner


async def main():
    agent = Agent(
        name="Assistant",
        instructions="You should check your knowledge for accuracy and cite factual information.",
    )

    query = "What is the color of the sky?"

    result = await Runner.run(agent, query)

    for message in result.raw_responses[0].output:
        combined_text = ""
        for item in message.content:
            combined_text += item.text
            citations = getattr(item, "citations", None)
            if citations:
                for citation in citations:
                    combined_text += f" [{citation.document_title}]"

    print("Response:", combined_text.strip())


if __name__ == "__main__":
    asyncio.run(main())

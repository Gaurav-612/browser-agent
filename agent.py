from langchain_openai import ChatOpenAI
from browser_use import Agent, Browser
from dotenv import load_dotenv
import os
load_dotenv()

import asyncio
browser = Browser()
llm = ChatOpenAI(model="gpt-4o")
decipher_username = os.environ.get("DECIPHER_USERNAME")
decipher_password = os.environ.get("DECIPHER_PASSWORD")

async def main():
    async with await browser.new_context() as context:
        agent = Agent(
            task="Open decipher.dev.limbik.com",
            llm=llm,
            browser_context=context  # Use persistent context
        )

        # Run the agent
        await agent.run()

        # Pass the context to the next agent
        login_agent = Agent(
            task=f"Login with username={decipher_username} and password={decipher_password}",
            llm=llm,
            browser_context=context
        )

        await login_agent.run()

        # Run a forecast
        forecast_agent = Agent(
            task="Enter a message 'The earth is round' in the input box and click the arrow button to forecast",
            llm=llm,
            browser_context=context
        )

        await forecast_agent.run()

        # record a forecast
        screenshot_agent = Agent(
            task="Wait for the running forecast to complete, and save the believabilty and virality scores of the latest forecasted message",
            llm=llm,
            browser_context=context
        )

        await screenshot_agent.run()

        # await browser.close()
    # Manually close the browser
    await browser.close()

asyncio.run(main())
from browser_use import Agent, ChatGoogle, Browser
from dotenv import load_dotenv
import asyncio

# Connect to your existing Chrome browser
browser = Browser(
    executable_path='C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
    user_data_dir='%LOCALAPPDATA%\\Google\\Chrome\\User Data',
    profile_directory='Default',
)

load_dotenv()

async def main():
    llm = ChatGoogle(model="gemini-2.5-flash")
    task = "Find the latest news about the weather in podili"
    agent = Agent(task=task, llm=llm, browser=browser)

    result = await agent.run()
    print(result)

    browser.close()

if __name__ == "__main__":
    asyncio.run(main())

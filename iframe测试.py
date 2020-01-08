import asyncio
from pyppeteer import launch

async def main():
    path = r"E:\download\chrome-win32\chrome-win32\chrome.exe"
    browser = await launch(executablePath=path,headless=False)
    page = await browser.newPage()
    await page.goto('https://www.taobao.com/')
    await asyncio.sleep(3)
    frame = page.frames
    await browser.close()

    # for i in enumerate(frame):
    #     print(frame[i].name)
    #     print(frame[i].url)
    print(frame[0].title())

asyncio.get_event_loop().run_until_complete(main())
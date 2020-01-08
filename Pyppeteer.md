# pyppeteer安装

```shell script
python3 -m pip install pyppeteer
```

# 简单使用
```python
import asyncio
from pyppeteer import launch

async def main():
    browser = await launch()
    page = await browser.newPage()
    await page.goto('http://example.com')

    await browser.close()

asyncio.get_event_loop().run_until_complete(main())
```

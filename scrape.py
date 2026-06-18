#!/usr/bin/env python3
import sys, argparse, asyncio
from pathlib import Path

async def main():
    parser = argparse.ArgumentParser(description='Simple Firecrawl alternative using Playwright')
    parser.add_argument('url', help='URL to fetch')
    parser.add_argument('--selector', help='CSS selector to extract inner HTML', default=None)
    args = parser.parse_args()
    from playwright.async_api import async_playwright
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto(args.url, wait_until='networkidle')
        if args.selector:
            content = await page.inner_html(args.selector)
        else:
            content = await page.content()
        print(content)
        await browser.close()

if __name__ == '__main__':
    asyncio.run(main())

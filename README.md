# Simple Firecrawl Alternative

This repository provides a lightweight Python script that uses Playwright to fetch web pages, render JavaScript, and extract the HTML content. It mimics the core functionality of Firecrawl without requiring a paid service.

## Features
- Headless Chromium rendering via Playwright.
- Optional CSS selector extraction.
- Simple CLI interface.

## Usage
```bash
python scrape.py <url> [--selector "css_selector"]
```

## Installation
```bash
pip install playwright
playwright install chromium
```

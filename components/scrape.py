from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://langchain-ai.github.io/langgraph/tutorials/introduction/")
    print(page.content())
    browser.close()
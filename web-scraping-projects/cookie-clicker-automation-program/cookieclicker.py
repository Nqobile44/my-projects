from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Record the start time of the program to calculate elapsed time later
main_starting_time = time.time()

# Set up Edge browser options to keep the browser window open after the script finishes
edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option(name="detach", value=True)

# Initialize the Edge WebDriver and open the Cookie Clicker game
driver = webdriver.Edge(edge_options)
driver.get(url="https://orteil.dashnet.org/experiments/cookie/")

# Locate the cookie element on the webpage
cookie = driver.find_element(by=By.XPATH, value='//*[@id="cookie"]')

def buy_item(item: str):
    """
    Buys the most expensive item that the user can afford.
    Args:
        item (str): The name of the item to buy.
    """
    # Find the item in the store and click it to purchase
    item_element = driver.find_element(by=By.CSS_SELECTOR, value=f"#store #buy{item}")
    item_element.click()

    # Check if 500 seconds have elapsed since the start of the program
    if abs(int(main_starting_time - time.time())) <= 500:
        # Continue clicking the cookie if the time is within the limit
        cookie_clicker()
    else:
        # Print the cookies per second (CPS) rate when the program ends
        cookies_per_sec = driver.find_element(by=By.ID, value="cps")
        print(cookies_per_sec.text)

def checker():
    """
    Checks the available money and determines which items can be afforded.
    Purchases the most expensive affordable item.
    """
    # Get the current amount of cookies (money) available
    money = driver.find_element(by=By.ID, value="money")
    # Get the prices of all items in the store
    item_prices = driver.find_elements(by=By.CSS_SELECTOR, value="#store div b")
    list_text = [element.text.split("-") for element in item_prices]
    list_text.pop()  # Remove the last element (it may not be an item)

    affordable_items = []
    money = money.text
    # Handle commas in the money string for proper comparison
    if "," in money:
        money = money.replace(",", "")
    for item in list_text:
        # Handle commas in the item prices for proper comparison
        if "," in item[1]:
            correct_price = item[1].replace(",", "")
            item.remove(item[1])
            item.append(correct_price.strip())
        # Check if the item is affordable
        if float(item[1]) <= float(money):
            affordable_items.append(item)

    # Find the most expensive affordable item
    expensive_item = None
    num = 0
    for item in affordable_items:
        price = int(item[1].strip())
        if price > num:
            num = price
            expensive_item = item[0].strip()

    # Buy the most expensive affordable item
    buy_item(item=expensive_item)

def cookie_clicker():
    """
    Simulates clicking the cookie for 10 seconds, then checks and buys items.
    """
    # Record the start time of the cookie-clicking session
    start_time = time.time()
    while abs(int(start_time - time.time())) <= 10:
        # Click the cookie continuously for 10 seconds
        cookie.click()

    # After 10 seconds, check for affordable items and purchase
    checker()

# Start the cookie-clicking process
cookie_clicker()

# Close the browser window after the program finishes
driver.quit()


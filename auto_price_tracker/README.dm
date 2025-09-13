# Auto Price Tracker

## Project Overview
Auto Price Tracker is a Python automation script that monitors product prices on Amazon. It helps users get notified immediately when a product reaches a desired target price.

## Key Features
- Reads product details (URL, product name, target price) from a JSON file.
- Monitors multiple products including AirPods, PS5, iPhone 16, and MateBook.
- Sends an email notification to the user when the product price meets or goes below the target price.
- Runs automatically in the background using Python’s `time` module with a delay of 600,000 seconds between checks.

## How It Works
1. The JSON file contains all the product information needed for tracking.
2. The script iterates through each product URL and checks the current price on Amazon.
3. If the current price is less than or equal to the target price, the script sends an email alert.
4. After completing the check for all products, the script waits 600,000 seconds before running again.

## Setup Instructions
1. Clone or download the repository.
2. Ensure Python 3.x is installed.
3. Install required libraries:
```bash
pip install requests beautifulsoup4 requests email json os smtplib

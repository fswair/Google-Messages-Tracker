from selenium import webdriver
from pysondb.db import getDb
import time
from bs4 import BeautifulSoup as Soup

def main():
    db = getDb("./database/db.json")
    
    driver = webdriver.Firefox()

    driver.get("https://messages.google.com/web/")
    print("[opening] Google Messages Web page is opening...")
    print("[waiting] Please login to the Google Messages Web page.")

    input("[waiting] Press enter after you've scanned the QR code...")

    print("[opened] Google Messages Web successfully logged in.")
    print("[running] Polling messages...")

    page_source = driver.page_source

    def poll_messages(page_source: str):
        bs = Soup(page_source, 'html.parser')

        items = bs.select("mws-conversation-list-item")

        messages = []

        for item in items:
            sender = item.select_one("span[data-e2e-conversation-name]")
            message = item.select_one("span.ng-star-inserted")
            
            messages.append({
                "sender": sender.text,
                "message": message.text
            })
        print(f"[polled] {len(messages)} messages parsed successfully.")
        return messages


    messages = poll_messages(page_source)
    i=0
    while True:
        i += 1
        print(f"[polling] Polling by {i} times...")
        for message in messages[::-1]:
            res = db.getByQuery({"message": message["message"], "sender": message["sender"]})
            if res:
                ...
            else:
                message.update({"added_date": time.time()})
                db.add(message)
                time.sleep(0.1)
                print(f"[added] New message from {message['sender']} added to the database.")
                print(f"[added] Message: {message['message'][:100]}...")
        time.sleep(3)
        messages = poll_messages(driver.page_source)
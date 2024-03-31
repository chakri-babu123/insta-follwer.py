import time
import random
from instabot import Bot
from instabot.api import APIError

def send_follow_requests(username, password, follower_limit):
    bot = Bot()
    try:
        bot.login(username=username, password=password)
    except APIError as e:
        print("Failed to log in:", e)
        return

    try:
        followers = bot.get_user_followers(bot.user_id)
    except APIError as e:
        print("Failed to fetch followers:", e)
        bot.logout()
        return

    count = 0
    for follower in followers[:follower_limit]:
        try:
            bot.send_follow_request(user_id=follower)
            count += 1
            print(f"Sent follow request to user {count}/{follower_limit}")
            # Introduce a random delay between actions
            delay = random.uniform(10, 60)  # Random delay between 10 and 60 seconds
            time.sleep(delay)
        except APIError as e:
            print(f"Failed to send follow request to user {follower}: {e}")

    bot.logout()
    print("Follow requests sent successfully.")

if __name__ == "__main__":
    username = input("Enter your Instagram username: ")
    password = input("Enter your Instagram password: ")
    follower_limit = int(input("Enter the number of followers to send follow requests to: "))

    send_follow_requests(username, password, follower_limit)

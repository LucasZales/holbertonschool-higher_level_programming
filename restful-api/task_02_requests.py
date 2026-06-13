#!/usr/bin/python3
import csv
import requests

URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_and_print_posts():

    response = requests.get(URL)
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        posts = response.json()

        for post in posts:
            print(post['title'])


fetch_and_print_posts()


def fetch_and_save_posts():

    response = requests.get(URL)
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        posts = response.json()

        info = []
        for post in posts:
            info.append({
                "id": post["id"],
                "title": post["title"],
                "body": post["body"]
            })

        with open("posts.csv", "w", newline="") as csvfile:
            fieldnames = ["id", "title", "body"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(info)

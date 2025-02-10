import csv

from ping3 import ping


hosts = ["yandex.ru",
         "google.com",
         "github.com",
         "stackoverflow.com",
         "youtube.com",
         "duckduckgo.com",
         "wildberris.ru",
         "ozon.ru",
         "aliexpress.ru",
         "forest-home.ru"]

with open("pings.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, ["Address", "rtt (ms)"])
    writer.writeheader()

    for host in hosts:
        rtt = ping(host)
        if rtt is not None:
            writer.writerow({"Address": host, "rtt (ms)": rtt * 1000})
        else:
            writer.writerow(({"Address": host, "rtt (ms)": "timeout"}))

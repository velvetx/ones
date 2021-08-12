import requests
from multiprocessing import Pool
from os import cpu_count
from random import randint


class Requester:
    def __init__(self):
        self.results_of_requests = []
        self.user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) ' \
                          'Chrome/92.0.4476.0 Safari/537.36'

    def get_request(self):
        url = f'https://vkfaces.com/vk/users/{randint(100,600)}/{randint(0,99)}/{randint(0,99)}'
        return requests.get(url, headers={'User-Agent': self.user_agent}).text

    def starting_processing(self, pages_count):
        with Pool(cpu_count()) as pool:
            for _ in range(int(pages_count / 70) + 1):
                self.results_of_requests.append(pool.apply_async(self.get_request).get())
        return self.results_of_requests


import re
import sys
import csv
import time
import json
import vk_api
import requests


WORD_RE = re.compile(r'[А-яA-z]+')


def printProgress(iteration, total, decimals=2, len_=50):
    filledLength = int(round(len_ * iteration / float(total)))
    percents = round(100.00 * (iteration / float(total)), decimals)
    bar = '#' * filledLength + '-' * (len_ - filledLength)
    sys.stdout.write(' [%s] %s%s \r' % (bar, percents, '%'))
    if iteration == total:
        sys.stdout.write('\n')
    sys.stdout.flush()


def get_all_words(api, part=200):
    count = api.method('messages.get', count=1, out=1)[0]
    offset = 0
    words = {}

    while offset < count:
        printProgress(offset + 1, count)
        try:
            vk_msgs = api.method('messages.get', count=part,
                                 offset=offset, out=1)[1:]
            for msg in vk_msgs:
                for word in WORD_RE.findall(msg['body']):
                    word = word.lower()
                    words[word] = words.setdefault(word, 0) + 1
            offset += part
        except (vk_api.ApiError,
                requests.exceptions.ConnectionError,
                requests.exceptions.ReadTimeout) as e:
            time.sleep(3)

    printProgress(count, count)

    return words


api = vk_api.Api()

words = get_all_words(api)
words = sorted(words.items(), key=lambda p: p[1], reverse=True)

with open('words.json', 'w', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['word', 'count'])

    for pair in words:
        writer.writerow(pair)

import argparse
import json
import os

import requests

parser = argparse.ArgumentParser(
    description='This utility allows to download or create downloading links '
                'for files and dirs from Yandex.Disk via public link')
parser.add_argument("-d", default=False, action='store_const', const=True,
                    help='Wget downloading files if you pointed flag')
parser.add_argument("--url", required=True, help='Paste download link from Yandex.Disk here')


def get_link(public_key):
    request_for_link = requests.get("https://cloud-api.yandex.net/v1/disk/public/resources/download",
                                    params={"public_key": public_key, "fields": "href"},
                                    )
    json_to_dict = json.loads(request_for_link.text)
    return json_to_dict['href']


if __name__ == '__main__':
    params = parser.parse_args()
    link = get_link(params.url)
    if params.d:
        os.system(f'wget {link}')
    else:
        print(link)

import argparse
import json
import subprocess

import requests

parser = argparse.ArgumentParser(
    description='This utility allows to download or create downloading links '
                'for files and dirs from Yandex.Disk via public link')
parser.add_argument("-d", default=False, action='store_const', const=True,
                    help='Wget downloading files if you pointed flag')
parser.add_argument("-o", type=str, help='Path to store output file')
parser.add_argument("--url", required=True, help='Paste download link from Yandex.Disk here')


def get_link(public_key):
    response = requests.get("https://cloud-api.yandex.net/v1/disk/public/resources/download",
                            params={"public_key": public_key, "fields": "href"},
                            )
    while response.status_code != requests.codes.OK:
        print("Couldn't receive link for this query")
        response = requests.get("https://cloud-api.yandex.net/v1/disk/public/resources/download",
                                params={"public_key": public_key, "fields": "href"},
                                )

    content = json.loads(response.content)
    return content['href']


if __name__ == '__main__':
    params = parser.parse_args()
    link = get_link(params.url)
    if params.d:
        subprocess.run(['wget', '-O', f'{params.o}', f'{link}'])
    else:
        print(link)

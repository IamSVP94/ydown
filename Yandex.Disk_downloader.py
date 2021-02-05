import sys,argparse,requests,json,os

def get_params():
    parser = argparse.ArgumentParser(description='This utility allows download files and dirs from Yandex.Disk.')
    parser.add_argument("-d", default=False, action='store_const', const=True,
                        help='Wget downloading files if you pointed flag')
    parser.add_argument("--url", required=True, help='Paste download link from Yandex.Disk here')
    params = parser.parse_args(sys.argv[1:])
    return params


def get_link(public_key):
    request_for_link = requests.get("https://cloud-api.yandex.net/v1/disk/public/resources/download",
                                    params={"public_key": public_key, "fields": "href"},
                                    )
    json_to_dict = json.loads(request_for_link.text)
    return json_to_dict['href']


if __name__ == '__main__':
    params = get_params()
    link = get_link(params.url)
    if params.d:
        os.system(f'wget {link}')
    else:
        print(link)

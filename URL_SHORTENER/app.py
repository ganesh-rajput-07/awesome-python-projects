from urllib.parse import urlencode
from urllib.request import urlopen
import sys

def short_url(url):
    request_url = f'http://tinyurl.com/api-create.php?{urlencode({"url": url})}'
    with urlopen(request_url) as response:
        return response.read().decode('utf-8')

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <url1> <url2> ...")
        return
    for url in sys.argv[1:]:
        print(short_url(url))

if __name__ == '__main__':
    main()

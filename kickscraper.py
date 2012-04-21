from bs4 import BeautifulSoup
import urllib2
import sys

def usage():
    sys.stderr.write("kickscraper.py <url>\n")

def get_backers_and_dollars(url):
    html_doc = urllib2.urlopen(url).read()
    soup = BeautifulSoup(html_doc)

    money_raised_div = soup.find(id='moneyraised')
    headers = money_raised_div.find_all('h5')
    backers = headers[0].div.string
    dollars = headers[1].div.string
    return (backers, dollars)

def print_backers_and_dollars(url):
    print 'Backers: %s Dollars: %s' % get_backers_and_dollars(url)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        usage()
        sys.exit(1)

    print_backers_and_dollars(sys.argv[1])

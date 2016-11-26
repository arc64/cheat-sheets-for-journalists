# Go here for a nice tutorial
# https://github.com/maxharlow/tutorials/blob/master/opencorporates-api/README.md

import sys
import unicodecsv as csv
import json
import requests

## This script just does this:
## https://api.opencorporates.com/v0.4/companies/search?jurisdiction_code=pk
## To run script open a terminal and type:
## python ./open-corporates-api.py [two letter country code] [page to start from] [some api key]
## https://en.wikipedia.org/wiki/ISO_3166-1
## For example, for Pakistan:
## python ./open-corporates-api.py pk 1 ''
## It will write to a .csv file, with headers, beginning with the country code, ending in the page number
## or with an API key
## python ./open-corporates-api.py pk 1 somekey

def get_companies(companies):
    results =[]
    for item in companies:
        company = item['company']
        a_company = {
            'name': company['name'],
            'type': company['company_type'],
            'registry_url': company['registry_url'],
            'current_status': company['current_status'],
            'company_type': company['company_type'],
            'registry_url': company['registry_url'],
            'incorporated': company['incorporation_date'],
            'address': company['registered_address_in_full'],
            'opencorporates_url': company['opencorporates_url']
        }
        results.append(a_company)

    return results

def to_file(results, write_header, filename):
    with open(filename, 'a') as csvfile:
        header = results[0].keys()
        writer = csv.DictWriter(csvfile, header, encoding='utf-8')
        if write_header:
            writer.writeheader()
        writer.writerows(results)

def get_total_pages(url):
    response = requests.get(url)
    if response.status_code == 200:
        data = json.loads(response.text)
        pages = data['results']['total_pages']
        return pages
    else:
        print('Error: ' + str(response.status_code))
        print(response.text)

    return 1

def lookup(country, start_from, key):
    is_first_result = False
    count = int(start_from)
    page_num = int(start_from)
    total_pages = 0
    total_results = 0
    api_key = ''

    if key:
        api_key = '&api_token=' + key + '&per_page=100'

    filename = str(country) + '-company-details-' + str(page_num) +'.csv'
    base_url = 'https://api.opencorporates.com/v0.4/companies/search?&jurisdiction_code=' + country + api_key

    total_pages = get_total_pages(base_url)

    # get all the pages
    while count <= total_pages:
        url = base_url + '&page=' + str(count)
        print url
        page_of_companies = []
        response = requests.get(url)

        if response.status_code == 200:
            data = json.loads(response.text)

            if count == page_num:
                is_first_result = True
                print 'Total pages: ' + str(total_pages)
                print 'Total companies: ' + str(data['results']['total_count'])
            else:
                is_first_result = False


            # get one page of results
            page_of_companies = get_companies(data['results']['companies'])

            # write to file one page of results
            to_file(page_of_companies, is_first_result, filename)
            total_results += len(page_of_companies)
        else:
            print('Error: ' + str(response.status_code))
            print(str(response.content))

        print 'Page of results:  ' + str(count)
        print 'Results so far:   ' + str(total_results)
        print '- - - - - - - - - - - - - - - - - - - - - - -'

        count += 1

    print '--------------------------------------'
    print 'Results started from page: ' + str(page_num)
    print 'Companies for country: ' + country
    print 'Companies gathered: ' + str(total_results)
    print 'results in file: ' + str(country) +'-company-details-' + str(page_num) + '.csv'


lookup(sys.argv[1], sys.argv[2], sys.argv[3])


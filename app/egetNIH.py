# PERL SOURCES
# https://www.ncbi.nlm.nih.gov/books/NBK25498/#chapter3.ELink__ESearch
# https://www.ncbi.nlm.nih.gov/books/NBK25501/


import requests
def egetNIH():
    db = 'pubmed'
    query = 'asthma[mesh]+AND+leukotrienes[mesh]+AND+2009[pdat]'

    # Assemble the esearch URL
    base = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/'
    url = f'{base}esearch.fcgi?db={db}&term={query}&usehistory=y'

    # Post the esearch URL
    response = requests.get(url)
    output = response.text

    # Parse WebEnv and QueryKey
    web = output.split('<WebEnv>')[1].split('</WebEnv>')[0]
    key = output.split('<QueryKey>')[1].split('</QueryKey>')[0]

    # Include this code for ESearch-ESummary
    # Assemble the esummary URL
    url = f'{base}esummary.fcgi?db={db}&query_key={key}&WebEnv={web}'

    # Post the esummary URL
    docsums_response = requests.get(url)
    docsums = docsums_response.text
    print(docsums)

    # Include this code for ESearch-EFetch
    # Assemble the efetch URL
    url = f'{base}efetch.fcgi?db={db}&query_key={key}&WebEnv={web}'
    url += '&rettype=abstract&retmode=text'

    # Post the efetch URL
    data_response = requests.get(url)
    data = data_response.text
    print(data)
    return data
egetNIH()

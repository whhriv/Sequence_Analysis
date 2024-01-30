# PERL SOURCES
# https://www.ncbi.nlm.nih.gov/books/NBK25498/#chapter3.ELink__ESearch
# https://www.ncbi.nlm.nih.gov/books/NBK25501/


import requests

# Download protein FASTA records linked to abstracts published 
# in 2009 that are indexed in MeSH for both asthma and 
# leukotrienes.

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


## HUMAN PROTEIN

# Given an input set of protein GI numbers, this script creates 
# a history set containing the members of the input set that 
# correspond to human proteins. 
#(Which of these proteins are from human?)

def protein_from_human():

    db = 'protein'
    query = 'human[orgn]'
    id_list = '194680922,50978626,28558982,9507199,6678417'

    # Assemble the epost URL
    base = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/'
    url = f'{base}epost.fcgi?db={db}&id={id_list}'

    # Post the epost URL
    response = requests.get(url)
    output = response.text

    # Parse WebEnv and QueryKey
    web = output.split('<WebEnv>')[1].split('</WebEnv>')[0]
    key = output.split('<QueryKey>')[1].split('</QueryKey>')[0]

    # Assemble the esearch URL
    term = f'%23{key}+AND+{query}'
    url = f'{base}esearch.fcgi?db={db}&term={term}'
    url += f'&WebEnv={web}&usehistory=y'

    # Post esearch URL
    limited_response = requests.get(url)
    limited = limited_response.text

    print(limited)
protein_from_human()



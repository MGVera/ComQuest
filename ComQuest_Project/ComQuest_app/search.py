import json
import urllib, urllib2
import os

gsearch_API_KEY = os.environ.get('gsearch_API_KEY')

def run_query(search_terms):
	root_url = 'https://www.googleapis.com/customsearch/v1?parameters'
	source = 'Web'
	results_per_page = 10
	offset = 0
	query = "'{0}'".format(search_terms)
	
	query = urllib.quote(query)
	search_url = "{0}{1}?$format=json&$top={2}&$skip={3}&Query={4}".format(
					root_url,
					source, 
					results_per_page,
					offset,
					query)
	username = ''
	password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()

	password_mgr.add_password(None, search_url, username, gsearch_API_KEY)

	results = []

	try:
		handler = urllib2.HTTPBasicAuthHandler(password_mgr)
		opener = urllib2.build_opener(handler)
		urllib2.install_opener(opener)

		response = urllib2.urlopen(search_url).read()
		json_response = json.loads(response)

		for result in json_response['d']['results']:
			results.append({
				'title': result['Title'],
				'link': result['Url'],
				'summary': result['Description']})

	except urllib2.URLError as e:
		print search_url
		print "Error when querying the Google API: ", e

	return results
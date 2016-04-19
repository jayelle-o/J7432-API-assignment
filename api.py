import urllib2, json, urllib

response = urllib2.urlopen('http://openstates.org/api/v1/bills/?apikey=1f366e0712bd4ad6b079afe3bb993434&state=mo&search_window=session&fields=sponsors,title').read()

bills = json.loads(response)

for bill in bills:

    #print bill
    #print bill.keys()

    # This is the processing piece I mentioned in the assignment description. To include
    # a bill ID (which has spaces in it)through a URL in Python, you need to do this first.
    
    encoded_title = urllib.unquote(bill['title']).encode('utf-8')
    #formated_title = encoded_title
    
    encoded_sponsors = urllib.quote(bill['sponsors'][0]['name']).replace("%2C%20"," ")
    
    
    print encoded_title, encoded_sponsors
   
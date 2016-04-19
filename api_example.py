import urllib2, json, urllib

response = urllib2.urlopen('http://openstates.org/api/v1/bills/?apikey=1f366e0712bd4ad6b079afe3bb993434&state=mo&search_window=session').read()

bills = json.loads(response)

for bill in bills:

    # This is the processing piece I mentioned in the assignment description. To include
    # a bill ID (which has spaces in it)through a URL in Python, you need to do this first.
    #encoded_title = urllib.quote(bill['title'])
    encoded_id = urllib.quote(bill['bill_id'])  
    #print encoded_title, encoded_id

    #make a new url to search bill detail:
    new_url = "http://openstates.org/api/v1/bills/mo/2016/" + encoded_id + "/?apikey=1f366e0712bd4ad6b079afe3bb993434"
    #print new_url

    new_response = urllib2.urlopen(new_url).read()
    #print new_response

    bill_detail = json.loads(new_response)
    
    encoded_title = urllib.unquote(bill_detail['title']).encode('utf-8')
    encoded_sponsor = urllib.quote(bill_detail['sponsors'][0]['name'])
    
    
    print encoded_title, encoded_sponsor



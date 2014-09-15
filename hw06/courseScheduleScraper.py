import urllib
import urllib2

url = 'https://weblprod1.wheatonma.edu/PROD/bzcrschd.P_ListSection'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
values = {'subject_sch' : '%',
          'foundation_sch' : '%',
          'division_sch' : '%',
          'area_sch' : '%',
          'intmajor_sch' : '%',
          'schedule_beginterm' : '201620'}
headers = { 'User-Agent' : user_agent }

data = urllib.urlencode(values)
req = urllib2.Request(url, data, headers)
response = urllib2.urlopen(req)
the_page = response.read()
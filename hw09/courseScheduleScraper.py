import requests, time

def main():
    dataValues = {
        'intmajor_sch' : '%',
        'area_sch' : '%',
        'area_cat' : '%',
        'submit_btn' : 'Search Schedule',
        'subject_sch' : '%',
        'subject_cat' : '%',
        'foundation_sch' : '%',
        'schedule_beginterm' : '201510',
        'intmajor_cat' : '%',
        'division_sch' : '%',
        'foundation_cat' : '%',
        'crse_numb' : '%',
        'division_cat' : '%',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36',
        'Cookie': '_ga=GA1.2.99013180.1410794952; session=eyJyZWNlbnQiOlsiMTNxMHdjcDEiXX0.BviaPw.QJ5xAWB91r8I21WDad6uYYk6xPw',

    }

    years = xrange(2010, 2016, 1)
    semesters = xrange(10, 30, 10)

    fileNumber = 0

    for year in years:
        for semester in semesters:
            dataValues['schedule_beginterm'] = str(year) + str(semester)
            r = requests.post('https://weblprod1.wheatonma.edu/PROD/bzcrschd.P_OpenDoor', data=dataValues, headers=headers)
            if r.status_code == 200:
                with open('temp-ScrapedPages/testing' + str(fileNumber) + '.html', 'w') as outFile:
                    outFile.write(r.content)

            fileNumber += 1

if __name__ == '__main__':
    main()
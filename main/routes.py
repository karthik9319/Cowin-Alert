import requests
import datetime

day_limit = 10
today = datetime.datetime.today()
date_list = [today + datetime.timedelta(x) for x in range(day_limit)]
date_str_frm = [x.strftime("%d-%m-%Y") for x in date_list]

pincode = "721301"


for date in date_str_frm:
    output = []
    base_url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={}&date={}".format(
        pincode, date)
    headers = {
        'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"}

    response = requests.get(base_url, headers=headers)
    if response.status_code == 200:
        result = response.json()
        centers = result['centers']
        for center in centers:
            sessions = center['sessions']
            for session in sessions:
                res = {
                    'name': center['name'],
                    'block_name':center['block_name'],
                    'age_limit':session['min_age_limit'],
                    'vaccine_type':session['vaccine'] ,
                    'date':session['date'],
                    'available_capacity':session['available_capacity']
                }          
                print(res)

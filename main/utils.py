import datetime
import requests
from fake_useragent import UserAgent
import json
import pandas as pd
from pprint import pprint

class UserDetails():
    def __init__(self, 
                 daterange: int,
                 state: str,
                 district: str,
                 region: str,
                 pincode: str):
        
        self.daterange = daterange
        self.state = state
        self.district = district
        self.region = region
        self.pincode = pincode
        


# def district_mapper(district):
    




def day_list(numdays):
    today = datetime.datetime.today()
    date_list = [today + datetime.timedelta(x) for x in range(numdays)]
    date_str_frm = [x.strftime("%d-%m-%Y") for x in date_list]
    return date_str_frm

# temp_user_agent = UserAgent()
# browser_header = {'User-Agent': temp_user_agent.random}

def available_check(days, pincode, flag):
    output = []
    date_str_frm = day_list(days)
    for date in date_str_frm:
        #     base_url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id={}&date={}".format(
        # district_id, date)
            base_url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={}&date={}".format(
        pincode, date)
            headers = {
        'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"}
            response = requests.get(base_url, headers=headers)
            if response.status_code == 200:
                # if (response.ok) and ('centers' in json.loads(response.text)):
                #     resp_json = json.loads(response.text)['centers']
                #     if resp_json is not None:
                #         df = pd.DataFrame(resp_json)
                #         print(df)
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
                            'pincode': center['pincode'],
                            'available_capacity':session['available_capacity'],
                            'fee_type': center['fee_type'],
                            # 'hospital_name': center['hospital_name'],
                            'district_name': center['district_name'],
                            'state_name':center['state_name']
                            
                        }          
                        output.append(res)
                        
        
    return output


def format_output(output):
    name = []
    block_name = []
    age_limit = []
    vaccine_type = []
    date = []
    pincode = []
    available_capacity = []
    fee_type = []
    hospital_name = []
    district_name = []
    state_name = []
    for item in range(len(output)):
        name.append(output[item]['name'])
        block_name.append(output[item]['block_name'])
        age_limit.append(output[item]['age_limit'])
        vaccine_type.append(output[item]['vaccine_type'])
        date.append(output[item]['date'])
        pincode.append(output[item]['pincode'])
        available_capacity.append(output[item]['available_capacity'])
        fee_type.append(output[item]['fee_type'])
        # hospital_name.append(output[item]['hospital_name'])
        district_name.append(output[item]['district_name'])
        state_name.append(output[item]['state_name'])
        
    if len(name) > 0:    
        new_df = pd.DataFrame()
        
        new_df['state_name'] = state_name
        new_df['district_name'] = district_name
        new_df['Pincode'] = pincode
        new_df['Date'] = date
        
        new_df['Center Name'] = name
        new_df['Block Name'] = block_name
        new_df['Age Limit'] = age_limit
        # new_df['hospital_name'] = hospital_name
        new_df['Vaccine Type'] = vaccine_type
        
        
        new_df['Available Capacity'] = available_capacity
        new_df['Fee Type'] = fee_type
        
        
        

    # new_df.reset_index(inplace=True, drop=True)
    else:
        new_df = "Sorry No data available"
        
    return new_df
        
        
# def pretty_print(dataframe):
    
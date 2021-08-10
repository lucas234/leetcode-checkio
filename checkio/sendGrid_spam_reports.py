# coding=utf-8
# auther：Liul5
# date：2019/4/26 13:08
# tools：PyCharm
# Python：2.7.15
# https://py.checkio.org/en/mission/sendgrid-daily-spam/
# https://github.com/sendgrid/sendgrid-python/blob/master/USAGE.md#api-keys

import sendgrid
import json
from datetime import datetime
from datetime import timedelta

# need to register and get the key https://app.sendgrid.com
API_KEY = 'your api key'

sg = sendgrid.SendGridAPIClient(apikey=API_KEY)


def how_spammed(str_date):
    end_time = datetime.strptime(str_date, '%Y-%m-%d')
    start_time = end_time + timedelta(days=1)
    response = sg.client.suppression.spam_reports.get(query_params={
    'end_time':int(end_time.timestamp()),
    'start_time': int(start_time.timestamp())
    })
    data = json.loads(response.body)
    return len(data)
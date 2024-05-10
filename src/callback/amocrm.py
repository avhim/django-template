import requests

AMOCRM_BASE_URL = "https://travellab.amocrm.ru"
AMOCRM_LEADS_URL = "/api/v4/leads" # method post

AMOCRM_PIPELINES = {
    "корпоративные" :6637726,
    "автобусные": 911767,
    "авиа": 5676265,
    "визы": 7214690,
}


def amocrm_send_lead(msg):
    json = {
        "name": msg.name,
        "phone": msg.phone,
        "url": msg.url,
        "created_by": 0,
        "pipeline_id": AMOCRM_PIPELINES["корпоративные"],
    }
    r = requests.post(AMOCRM_BASE_URL+AMOCRM_LEADS_URL, json=json)
    r.status_code
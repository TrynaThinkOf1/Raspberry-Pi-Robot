import requests as rq

def report_error(error):
    rq.get('http://192.168.50.77:5000/report_error', params={'error':error})
    print(f"{error} was reported to site")

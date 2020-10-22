import json
import requests
import process_function

api_get = requests.get("https://api.github.com/repos/mitre/cti/contents/enterprise-attack/attack-pattern")
# html_link = requests.get("https://github.com/mitre/cti/tree/master/enterprise-attack/attack-pattern")
def screener():
    ret = []
    for item in api_get.json():
        url = item['download_url']
        # url_example = "https://github.com/mitre/cti/blob/master/enterprise-attack/attack-pattern/attack-pattern--0042a9f5-f053-4769-b3ef-9ad018dfa298.json"

        req = requests.get(url).json()
        fields = ["id", "objects[0].name", "objects[0].kill_chain_phases"]
        result = process_function.f(json.dumps(req), fields)
        print(result)
        ret.append(result)
    return ret

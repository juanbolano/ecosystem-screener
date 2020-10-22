import process_function


a = '{ \
    "guid": "1234", \
    "content": { \
        "type": "text/html", \
        "title": "Challenge 1", \
        "entities": ["1.2.3.4", "wannacry", "malware.com"], \
        "link": { \
            "type": "text/html", \
            "title": "Challenge 1", \
            "href": { \
                "type": "text/html", \
                "parent": "Challenge 1", \
                "entities": ["1.2.3.4", "wannacry", "malware.com"] \
            } \
        } \
    }, \
    "score": 74, \
    "entities": ["1.2.3.4", "wannacry", { \
                    "name": "mitre-attack", \
                    "external_id": "T1055.011", \
                    "url": "https://attack.mitre.org/techniques/T1055/011" \
                }], \
    "time": 1574879179 \
}'

b = ["guid", "testNotExists", "entities[1]", "content.entities", "content.link.href.parent", "entities[2].name", "content.link.href.testNotExists", "content.entities[0]", "score", "score.sign"]


print(process_function.f(a, b))

import requests

url="https://data.covid19india.org/data.json"

req=requests.get(url)

data=req.json()

for i in data["statewise"]:
    print("==================================================")
    print(f"state={i["state"]}")
    print(f"active case={i["active"]}")
    print(f"death={i["deaths"]}")
    print("==================================================")

    # for j in range(len(i)):
    #     print(f"state={data["statewise"][j]["state"]}")
    #     print(f"activecase={data["statewise"][j]["active"]}")
    #     print(f"death={data["statewise"][j]["deaths"]}")

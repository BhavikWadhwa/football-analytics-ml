import requests

url = "https://canadawest.org/sports/msoc/2025-26/boxscores/20250906_3yg8.xml"
r = requests.get(url, verify=False)
print(r.status_code)
print(r.text[:500])

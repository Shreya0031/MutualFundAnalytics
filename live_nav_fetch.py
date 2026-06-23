import requests
import pandas as pd
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

scheme_codes = {
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_LargeCap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

for name, code in scheme_codes.items():

    url = f"https://api.mfapi.in/mf/{code}"

    response = requests.get(url, verify=False)

    if response.status_code == 200:
        data = response.json()

        nav_data = pd.DataFrame(data["data"])

        nav_data.to_csv(
            f"data/raw/{name}_live_nav.csv",
            index=False
        )

        print(f"{name} downloaded successfully")
    else:
        print(f"Failed for {name}")
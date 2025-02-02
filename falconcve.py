import sys
import requests

# Replace this with your actual CrowdStrike API credentials
client_id = "xxxx"
client_secret = "xxxx"

# Check if a CVE ID is provided as a command-line argument
if len(sys.argv) != 2:
    print("Usage: python script.py <CVE_ID>")
    sys.exit(1)

cve_id = sys.argv[1]

# Authentication headers
headers = {
    "Content-Type": "application/x-www-form-urlencoded",
}

# Get OAuth token
token_url = "https://api.crowdstrike.com/oauth2/token"
token_data = {
    "client_id": client_id,
    "client_secret": client_secret,
    "grant_type": "client_credentials",
}
token_response = requests.post(token_url, data=token_data, headers=headers)
access_token = token_response.json().get("access_token")

# API call to get information about a specific vulnerability by its CVE ID
vulnerability_url = f"https://api.crowdstrike.com/spotlight/queries/vulnerabilities/v1?filter=cve.id%3A%5B'{cve_id}'%5D"
headers["Authorization"] = "Bearer " + access_token
response = requests.get(vulnerability_url, headers=headers)

# Check the response
if response.status_code == 200:
    data = response.json()
    total_count = data['meta']['pagination']['total']
    
    if total_count == 0:
        print(f"The system is Not Vulnerable to {cve_id}")
    else:
        print(f"The system is Vulnerable to {cve_id}")
else:
    print(f"Error: {response.status_code}, {response.text}")

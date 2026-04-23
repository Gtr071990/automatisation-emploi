import requests

BASE_URL = "http://localhost:11434/v1"
AUTH_TOKEN = "local-model"

def get_job_listings():
    headers = {"Authorization": AUTH_TOKEN}
    response = requests.get(f"{BASE_URL}/jobs", headers=headers)
    return response.json()

if __name__ == "__main__":
    jobs = get_job_listings()
    for job in jobs:
        print(f"Title: {job['title']}, Company: {job['company']}, Location: {job['location']}")

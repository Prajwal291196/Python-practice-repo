import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_jobs():
    url = "https://remoteok.com/remote-python-jobs"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print("❌ Failed to fetch page")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    jobs = []
    print(soup.prettify())
    for row in soup.find_all("tr", class_="job"):
        title = row.find("h2")
        company = row.find("h3")
        location = row.find("div", class_="location")
        link = row.find("a", class_="preventLink")

        jobs.append({
            "title": title.get_text(strip=True) if title else "N/A",
            "company": company.get_text(strip=True) if company else "N/A",
            "location": location.get_text(strip=True) if location else "Remote",
            "link": "https://remoteok.com" + link["href"] if link else "N/A"
        })

    return jobs

if __name__ == "__main__":
    job_list = scrape_jobs()
    if job_list:
        df = pd.DataFrame(job_list)
        df.to_csv("python_jobs.csv", index=False)
        print("✅ Jobs saved to python_jobs.csv")
    else:
        print("No jobs found.")

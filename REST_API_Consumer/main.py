import requests
import sqlite3

url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
try:
    response = requests.get(url)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print("❌ Network error:", e)
except ValueError:
    print("❌ Failed to parse JSON")
except sqlite3.Error as e:
    print("❌ Database error:", e)


# ✅ Check status
if response.status_code == 200:
    data = response.json()
    print(f"🌟 Total repositories found: {data['total_count']}")
else:
    print("❌ Failed to fetch data:", response.status_code)
    
repos = data["items"]
for repo in repos:
    name = repo["name"]
    stars = repo["stargazers_count"]
    owner = repo["owner"]["login"]
    url = repo["html_url"]
    print(f"📦 {name} by {owner} - ⭐ {stars}\n🔗 {url}\n")
# ---------------- SQLITE STORAGE ----------------
conn = sqlite3.connect("repos.db")
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS repositories(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    owner TEXT,
    stars INTEGER,
    url TEXT        
)
''')
conn.commit()

for repo in repos:
    c.execute('''INSERT INTO repositories (name, owner, stars, url)
                      VALUES (?, ?, ?, ?)''',(repo["name"], repo["owner"]["login"], repo["stargazers_count"], repo["html_url"]))

conn.commit()
conn.close()
print("✅ Repository data saved to repos.db")
    

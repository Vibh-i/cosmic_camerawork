import os
import requests

# GitHub API credentials
GITHUB_TOKEN = "YOUR_GITHUB_TOKEN"
GITHUB_REPO = "cosmic-camerawork"
GITHUB_USERNAME = "YOUR_GITHUB_USERNAME"

# Landing page content
INDEX_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Cosmic Camera Work</title>
  <style>
    body {
      background: linear-gradient(to bottom, #000080, #0000FF, #0000FF, #0019FF);
      color: white;
      font-family: sans-serif;
      text-align: center;
      padding: 50px;
    }
    h1, h2 {
      margin-bottom: 20px;
    }
    .container {
      display: flex;
      justify-content: center;
      align-items: center;
      gap: 50px;
      margin-top: 50px;
    }
    .icon {
      width: 100px;
      height: 100px;
    }
  </style>
</head>
<body>
  <h1>Cosmic Camera Work</h1>
  <h2>Astrophotography</h2>
  <p>Do you want to learn how to use your phone's camera to capture the night sky? Well, look no more, cosmic camerawork will teach you to do just that!</p>
  <p>You learn from the basics from learning which settings would help you capture the best photo for that location to editing all the pics!</p>
  <div class="container">
    <img src="flashlight.png" alt="Flashlight Icon" class="icon">
    <img src="camera.png" alt="Camera Icon" class="icon">
  </div>
</body>
</html>
"""

# Create a new branch for the GitHub Pages site
branch_name = "gh-pages"

# Create the branch if it doesn't exist
response = requests.put(
    f"https://api.github.com/repos/{GITHUB_USERNAME}/{GITHUB_REPO}/git/refs",
    headers={"Authorization": f"Bearer {GITHUB_TOKEN}"},
    json={"ref": f"refs/heads/{branch_name}", "sha": "0000000000000000000000000000000000000000"}
)

if response.status_code == 201:
    print(f"Created branch {branch_name}")
else:
    print(f"Error creating branch: {response.text}")

# Create the index.html file
with open("index.html", "w") as f:
    f.write(INDEX_HTML)

# Commit and push the changes
os.system(f"git add . && git commit -m 'Initial commit' && git push origin {branch_name}")

print("Site generated and pushed to GitHub!")

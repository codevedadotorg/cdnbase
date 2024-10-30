import requests
import json
import os

def fetch_cdnjs_libraries():
    url = "https://api.cdnjs.com/libraries"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get('results', [])
    else:
        print("Failed to fetch libraries from CDNJS API.")
        return []

def create_snippets(libraries):
    snippets = {}
    for lib in libraries:
        name = lib['name']
        latest_url = lib['latest']
        
        # Create snippet structure
        snippet = {
            "prefix": name,
            "body": [
                f"<script src=\"{latest_url}\"></script>"
            ],
            "description": f"{name} latest CDN version"
        }
        
        # Add to snippets dictionary with a unique key
        snippets[name] = snippet
    
    return snippets

def save_snippets_to_file(snippets):
    # Ensure the snippets folder exists
    os.makedirs("snippets", exist_ok=True)
    
    # Save the snippets to the specified file
    file_path = "snippets/snippets.code-snippets"
    with open(file_path, "w") as f:
        json.dump(snippets, f, indent=4)
    
    print(f"Snippets saved to {file_path}")

# Fetch libraries from CDNJS
libraries = fetch_cdnjs_libraries()

# Create snippets based on library data
snippets = create_snippets(libraries)

# Save snippets to the specified file
save_snippets_to_file(snippets)

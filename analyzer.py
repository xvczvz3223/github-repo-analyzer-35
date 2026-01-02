import requests

def analyze_repository(username):
    """Fetches and summarizes repository data for a given GitHub user."""
    base_url = f"https://api.github.com/users/{username}/repos"
    
    try:
        response = requests.get(base_url)
        response.raise_for_status()
        repos = response.json()
        
        if not repos:
            print(f"No public repositories found for user: {username}")
            return

        print(f"\n--- GitHub Analysis for {username} ---")
        print(f"Total Public Repos: {len(repos)}")

        total_stars = sum(repo.get('stargazers_count', 0) for repo in repos)
        languages = set(repo.get('language') for repo in repos if repo.get('language'))

        print(f"Total Stars Received: {total_stars}")
        print(f"Languages Used: {', '.join(languages)}")
        
        print("\nTop 3 Repositories by Stars:")
        sorted_repos = sorted(repos, key=lambda x: x['stargazers_count'], reverse=True)
        for repo in sorted_repos[:3]:
            print(f"- {repo['name']} ({repo['stargazers_count']} stars)")

    except requests.exceptions.RequestException as e:
        print(f"Error connecting to GitHub API: {e}")

if __name__ == '__main__':
    user_input = input('Enter a GitHub username to analyze: ').strip()
    if user_input:
        analyze_repository(user_input)
    else:
        print('Please provide a valid username.')
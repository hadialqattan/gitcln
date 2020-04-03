"""
Create new release to trigger CD actions.
"""

from requests import post, patch
from src.pycln import __version__


def create(): 
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'token 2194977a03b490906edbbeb4ee1117058c2ae9ce',
    }

    data={
            "tag_name": __version__,
            "target_commitish": "master",
            "name": __version__,
            "body": "First gitcln release.",
            "draft": False,
            "prerelease": False,
        }

    res = post(
        "https://api.github.com/repos/HadiZakiAlQattan/gitcln/releases",
        json=data, 
        headers=headers
    )

    print(res.status_code)
    print(res.text)

if __name__ == "__main__":
    create()

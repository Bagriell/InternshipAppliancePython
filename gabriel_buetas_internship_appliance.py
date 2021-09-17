import requests
from user_agents import parse
import platform

url = "https://random-data-api.com/api/internet_stuff/random_internet_stuff"


def getOsEmoji(user_agent_raw: str) -> str:
    windows_keywords = ["Windows"]
    linux_keywords = ["Linux", "Ubuntu"]
    apple_keywords = ["Ios", "Mac OS X"]
    android_keywords = ["Android"]
    user_agent = parse(user_agent_raw)
    
    return ( 
        "\U0001F6AA" if platform.system() == "Windows" and user_agent.os.family in windows_keywords
        else "\U0001FA9F"if platform.system() != "Windows" and user_agent.os.family in windows_keywords
        else "\U0001F427" if user_agent.os.family in linux_keywords
        else "\U0001F34E" if user_agent.os.family in apple_keywords
        else "\U0001F916" if user_agent.os.family in android_keywords
        else "\U0001F937"
    )

try:
    response = requests.get(url)
    response.raise_for_status()
except requests.exceptions.HTTPError as err:
    raise SystemExit(err)
try:
    data = response.json()
    if response.status_code == 200:
        print(f"L'adresse email de l'utilisateur {data['username']} est {data['email']}. Iel utilise le système d'exploitation {getOsEmoji(data['user_agent'])}.")
    else:
        print(f"La requête à {url} a échoué: code {response.status_code}")
except:
        print(f"Format de donnée invalide - {url}") 
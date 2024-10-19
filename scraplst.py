import re
import requests

# Expression régulière pour trouver les codes CFX dans les données
cfx_code_pattern = re.compile(r'\u0006([a-z0-9]{6})')

# Fonction pour extraire les codes CFX à partir des données
def extract_cfx_codes(data):
    matches = cfx_code_pattern.findall(data)
    return [code for code in matches if code != 'locale']

# Fonction pour écrire les codes CFX dans un fichier
def write_cfx_codes_to_file(cfx_codes):
    with open('cfxCodes.txt', 'w') as file:
        file.write('\n'.join(cfx_codes))
    print('Codes CFX écrits dans le fichier cfxCodes.txt.')

# URL à partir de laquelle récupérer les données
url = 'https://servers-frontend.fivem.net/api/servers/streamRedir/'

# Fonction principale qui récupère les données et traite les codes CFX
def main():
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.text

        # Extraction des codes CFX à partir des données
        cfx_codes = extract_cfx_codes(data)

        # Affichage des codes CFX dans la console
        print('Codes CFX extraits:', cfx_codes)

        # Écriture des codes CFX dans un fichier
        write_cfx_codes_to_file(cfx_codes)
    except requests.RequestException as err:
        print('Erreur lors de la récupération des données:', err)

if __name__ == '__main__':
    main()

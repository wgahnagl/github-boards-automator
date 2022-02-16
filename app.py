import yaml
import requests 

def main():
    with open("config.yaml", "r") as file: 
        config = yaml.safe_load(file)[0]
        print(config["query"].split()) 
        query = []
        for item in config["query"].split(): 
            item = item.replace(":", "%3A")
            item = item.replace("/", "%2F")
            query.append(item)
        query = "+".join(query)
        print(query)
        board_name = config["columns"][0]["name"]
        request = requests.get('https://github.com/orgs/kubernetes/projects/49/search_results?'+ board_name +'=show&q='+ query)
        print(request.content)

main()

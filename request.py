import requests
import json

url = "https://api.github.com/graphql"
end_cursor = "Y3Vyc29yOnYyOpISzkHZmGA="

with open("graphql/query_pullrequests.graphql", "r") as file:
    body = file.read()


response = requests.post(url, json={"query": body}, auth=("iKinoo", "TOKEN"), headers={"x-ratelimit-remaining": "application/json"})

file_number = 2

print("response status code: ", response.status_code)
print(response.headers)

if response.status_code == 200:
    data = response.json()
    #data_dict = json.loads(data)
    end_cursor = data["data"]["repository"]["issues"]["pageInfo"]["endCursor"]
    with open("graphql/cursor.txt", "a") as file:
        file.write(end_cursor + "\n")
    print(end_cursor)
    with open(f"response_pr{file_number}.json", "w") as file:
        json.dump(data, file, indent=4)

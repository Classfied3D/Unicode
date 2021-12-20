import json
import unicodedata
import requests

data = {}

request = requests.get("http://www.unicode.org/Public/4.1.0/ucd/NamesList.txt").text

for line in request.split('\n'):
  split = line.split('\t')
  if (
      not len(split) == 1 and
      not split[0].startswith("@") and
      not split[1].startswith("<") and
      not split[0] == "" and
      not split[1] == "" and
      not split[1] == "*"
    ): # Don't be so sad I wrote that

    if split[1].endswith(" *"):
      split[1] = split[1][:-2]
    if split[1].endswith(")"):
      test = split[1].split("(")
      split[1] = test[0][:-1]
    
    hex = split[0]
    name = split[1]
    char = unicodedata.lookup(split[1])

    data.update(
      {
        char: {
          "hex": hex,
          "name": name
        }
      }
    )

data = json.dumps(data) # I used auto-format afterwards
with open("[FILE NAME].json", "w") as file:
  file.write(data)

import requests
import sys
import re

def createArrayLinks(content):

  links = []
  lines = content.split('<')

  for i in range(0, len(lines)):
    if (lines[i][0] == 'a'):
      if (lines[i][2] == 'h'):
        if (lines[i][3] == 'r'):
          splt = lines[i].split('">')
          link = splt[0].split('"')
          if (len(link) > 1):
            link = link[1]
            link = re.sub('\\\\', '', link)
            link = link.replace('xc3xb3', 'ó')
            links.append(link)
          else:
            link = splt[0].split("'")
            link = link[1]
            link = re.sub('\\\\', '', link)
            link = link.replace('xc3xb3', 'ó')
            links.append(link)
  return links


params = sys.argv[1:]

search_link = str(params[0])
# estado = str(params[1])

response = requests.get(search_link)

if (response.status_code == 200):
  sourceCode = str(response.content)
  sourceCodeString = str(sourceCode)

  links = createArrayLinks(sourceCodeString)

  print(links)

import requests
import sys
import re

def createArrayLinks(content):

  links = []
  lines = content.split('<')
  contLinks = 0

  for i in range(0, len(lines)):
    if (lines[i][0] == 'a'):
      if (lines[i].find('href')):
        splt = lines[i].split('">')
        link = splt[0].split('href="')
        if (len(link) > 1):
          if (link[1].find('"')):
            link = link[1].split('"')
            link = link[0]
            link = re.sub('\\\\', '', link)
            link = link.replace('xc3xb3', 'ó')
            if (not link.find('http')):
              links.append(link)
              contLinks = contLinks + 1
          else:
            link = link[1]
            link = re.sub('\\\\', '', link)
            link = link.replace('xc3xb3', 'ó')
            if (not link.find('http')):
              links.append(link)
              contLinks = contLinks + 1
        else:
          link = splt[0].split("'")
          link = link[0]
          if (link.find('"')):
            link = link.split('"')
            link = link[0]
            link = re.sub('\\\\', '', link)
            link = link.replace('xc3xb3', 'ó')
            if (not link.find('http')):
              links.append(link)
              contLinks = contLinks + 1
          else:
            link = re.sub('\\\\', '', link)
            link = link.replace('xc3xb3', 'ó')
            if (not link.find('http')):
              links.append(link)
              contLinks = contLinks + 1
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

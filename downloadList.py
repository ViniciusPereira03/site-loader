import sys
import urllib.request, urllib.parse, urllib.error
import re

def urlEncodeNonAscii(b):
    return re.sub('[\x80-\xFF]', lambda c: '%%%02x' % ord(c.group(0)), b)

def iriToUri(iri):
    parts= urllib.parse.quote(iri)
    return urllib.parse.urlunparse(
        part.encode('idna') if parti==1 else urlEncodeNonAscii(part.encode('utf-8'))
        for parti, part in enumerate(parts)
    )


params = sys.argv[1:]

link_list = str(params[0])
estado = str(params[1])

extencao = link_list.split('.')
i = len(extencao)
i = i-1
extencao = extencao[i]

print("baixando lista de {}".format(estado))

link = iriToUri(link_list)

urllib.request.urlretrieve(link, "{}.{}".format(estado, extencao))

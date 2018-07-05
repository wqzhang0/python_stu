import collections
import json

import xmltodict


def create(_data):
    return xmltodict.unparse(_data, pretty=True)


if __name__ == '__main__':
    xml_dict = xmltodict.parse("""
  <mydocument has="an attribute">
    <and>
      <many>elements</many>
      <many>more elements</many>
    </and>
    <plus a="complex">
      element as well
    </plus>
  </mydocument>
  """)
    print(json.dumps(xml_dict))
    print(xml_dict.get('mydocument'))

    odic = collections.OrderedDict()
    odic['a'] = 'va'
    odic['c'] = 'vc'
    odic['d'] = 'vd'
    odic['b'] = 'vb'
    print(create({"response":odic}))

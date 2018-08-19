from lxml import etree

def get_simpledata_from_xmlfile(path):
    tree = etree.parse(path).getroot()
    version = tree.find('version').text
    symbol = tree.find('tradingSymbol').text
    interval = tree.find('tradingInterval').text
    indicators = tree.find('indicators')
    indicatorcounter = len(indicators)
    returnvalues = {'version': version, 
                    'symbol': symbol, 
                    'interval': interval, 
                    'indicatorcounter': indicatorcounter}
    return returnvalues

def get_symbolandinterval(path):
    tree = etree.parse(path).getroot()
    symbol = tree.find('tradingSymbol').text
    interval = tree.find('tradingInterval').text
    return symbol, interval

def get_indicators_from_xmlfile(path):
    tree = etree.parse(path).getroot()
    indicators = tree.find('indicators')
    indicatorarray = []
    for indicator in indicators:
        indicatorvalues = {}
        indicatorvalues['name'] = indicator.tag
        for value in indicator:
            indicatorvalues[value.tag] = value.text
        indicatorarray.append(indicatorvalues)
    return indicatorarray


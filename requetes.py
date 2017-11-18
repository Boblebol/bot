import requests

def getList (number) :
    print ("https://api.coinmarketcap.com/v1/ticker/?limit=%s"%(str (number)))
    r = requests.get("https://api.coinmarketcap.com/v1/ticker/?limit=%s"%(str (number)))
    i = 0
    res = ""
    while i < number :
        a = r.json()[i]
        res += "%s (%s): %sUSD (%sBTC)\n"\
               %(a['name'], a['symbol'],a['price_usd'],a['price_btc'],)
        i += 1
    return res

def getListLimit (start=0, limite=100) :
    r = requests.get("https://api.coinmarketcap.com/v1/ticker/?start=%s&limit=%s"%(str (start),str(limite)))
    i = 0
    res = ""
    if limite > 1000 :
        return "Les monnaie apres la millieme du classement sont insignifiantes ..."
    while i<100:
        try :
            a = r.json()[i]
        except IndexError:
            return res
        res += "%s (%s): %sUSD (%sBTC)\n"\
               %(a['name'], a['symbol'],a['price_usd'],a['price_btc'],)
        i += 1
    return res

def search (symbol) :
    ch = 100
    a = getListLimit (0,ch)
    while a != "" :
        tab = a.split ("\n")
        for monnaie in tab:
            if monnaie.find(symbol) != -1:
                return monnaie
        a = getListLimit(ch, ch + 100)
        ch = ch + 100
    return "desolé votre monnaie est trop bas dans le top 1000"

print(search ("ETH"))

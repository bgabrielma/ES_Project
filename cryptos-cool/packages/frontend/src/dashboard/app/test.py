
def concat2(words, sep = "%20AND%20"):
    print(words)
    for word in words:  
        if word == "None":
            words.remove(word)

    print(words)

    value = sep.join(words)

    return value

print(datetime.datetime.now())
bitcoin = "btc"
ripple = "xrp"
etherium = None
# list = [str(bitcoin),str(ripple),str(etherium)]
# list = [",".join()]
search = concat2([str(bitcoin),str(ripple),str(etherium)])
# search = f"{bitcoin}%20AND%20{ripple}%20AND%20{etherium}"

print(f"http://host.docker.internal:2000/api/news?search={search}")
 

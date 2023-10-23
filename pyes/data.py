def getdata():
    with open('pyes/data.txt') as f:
        content = f.readlines()
        return content

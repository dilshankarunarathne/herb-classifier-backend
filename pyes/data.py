def getdata():
    with open('test.txt') as f:
        content = f.readlines()
        return content

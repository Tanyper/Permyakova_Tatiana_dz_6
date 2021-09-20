with open ("nginx_logs.txt","r", encoding="utf-8") as f:
    content = ((line.split()[0], line.split ()[5][1:])for line in f)
    for i in content:
        print(i)

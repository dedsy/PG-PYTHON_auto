FILE_NAME = 'anna_karenina.txt'
with open(FILE_NAME, encoding='utf-8') as f:
    print(f)
    content = f.read()
    print(content)
    content_utf_8 = content.encode()
    print(content_utf_8)
    print(content_utf_8.decode())

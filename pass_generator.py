import base64, hashlib


def get_pass(passwd, domain, salt, size=16, encoding='utf_8'):
    """
    pass: your source secret to generate a password. Don't tell any body,
        best to just keep in your mind. And Dont't forget it, or you will 
        not be able to find your passwords back along with domain and salt.
    domain: using a website name is suggested.
    salt: using a user name is suggested.
    size: default is 16. legal range: [1, 44]
    
    return: a password<str> with size of [size].
    
    Algorithm: URLSAFE_BASE64(SHA256(SHA256(passwd), domain, salt))
    NOTE: datas in the process are bytes.
    
    """
    if not domain + salt:
        print('warning: no domain or salt used.')
    h = hashlib.sha256()
    h1 = h.copy()
    h1.update(passwd.encode(encoding))
    h.update(h1.digest() + (domain + salt).encode(encoding))
    return base64.urlsafe_b64encode(h.digest()).decode(encoding)[:size]
    
    
def input_size(info):
    while True:
        try:
            _s = input(info)
            if not _s:
                return
            a = int(_s)
            if a < 1 or a > 44:
                info = 'size need to be around [1, 44], input size again:'
            return a
        except ValueError:
            info = 'size need to be a number, input again:' 
        
    
if __name__ == '__main__':
    password = get_pass(domain = input('input website domain or name: '),
                   salt = input('input user name or salt: '),
                   size = input_size("input password_size, press 'enter'"
                   + "to use 16: ") or 16,
                   passwd = input('input your source secret: '))
    print('Your Password Is: %s' %password)
    
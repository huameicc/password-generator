#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import base64, hashlib, msvcrt


UTF8 = 'utf-8'


def get_pass(passwd, domain, salt, size=16, encoding=UTF8):
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
                continue
            return a
        except ValueError:
            info = 'size need to be a number, input again:' 
            

def input_pwd(info):
    """safe input passwd, echo * but no real alpha."""
    # print(info, end='')
    for b in info.encode():
        msvcrt.putch(bytes([b,]))
    chars = []   
    while True:  
        try:  
            ch = msvcrt.getch().decode()  
            if ch in '\r\n':            
                 break   
            elif ch == '\b':  
                 if chars:    
                     del chars[-1]   
                     msvcrt.putch(b'\b') 
                     msvcrt.putch(b' ')
                     msvcrt.putch(b'\b')                    
            else:  
                chars.append(ch)  
                msvcrt.putch(b'*')  
        except:  
            return input("Warning - input will not be hided: ")  
    print()
    return ''.join(chars) 
        
    
if __name__ == '__main__':
    password = get_pass(domain = input('input website domain or name: '),
                   salt = input('input user name or salt: '),
                   passwd = input_pwd('input your source secret: '),
                   size = input_size("input password_size, press 'enter'"
                   + "to use 16: ") or 16)
    print('Your Password Is: %s' %password)
    
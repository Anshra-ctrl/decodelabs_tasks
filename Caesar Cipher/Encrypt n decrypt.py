def Ceaser_encrypt(text,s):
    result=""
    for i in range(len(text)):
        char=text[i]
        if 'a' <= char <= 'z':
            result+=chr((ord(char)+s-97)%26+97)
        else:
            result+=char
    return result


def Ceaser_decrypt(text, s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if 'a' <= char <= 'z':
            result += chr((ord(char) -s +26- 97) % 26 + 97)
        else:
            result += char
    return result   
if __name__=="__main__":
    Key=int(input("Enter Key/Shift: "))
    Plain=input("PlainText : ").lower()
    CipherText=Ceaser_encrypt(Plain,Key)
    print("CipherText: ",CipherText)
    print("DecipheredText: ",Ceaser_decrypt(CipherText,Key))
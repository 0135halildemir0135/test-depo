user = "ab2018"
password = "12345"
yılw = "2000"

while True:
    kullanici = input("Kullanıcı adınızı giriniz: ")
    parola = input("Şifrenizi giriniz: ")
    yıl = input("yıl gir")
    # ikisi de doğru
    if kullanici == user and parola == password and yıl == yılw:
        print("Hoşgeldiniz")
        break
    # kullanıcı adı doğru şifre yanlış
    elif kullanici == user and parola != password:
        print("Şifreniz yanlış\n")
    # şifre doğru kullacı adı yanlış
    elif kullanici != user and parola == password:
        print("Kullanıcı adınız yanlış \n")
    # ikisi de yanlış
    else:
        print("Kullanıcı adı ve şifre hatalı\n")
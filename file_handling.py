__author__ = 'PrasantJillella'
fm = open("prasant.txt","w")
fm.write("I want to be the greatest programmer in the world\n")
fm.write("I got my inspiration from Roronoa Zoro Who is one the charactor from One Piece\n")
fm.close()

fm =open("prasant.txt","r")
text=fm.read()
print(text)
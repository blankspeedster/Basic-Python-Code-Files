f1 = open('my_files/logo.jpg','rb')
f2 = open('my_files/logo2.jpg','wb')
f2.write(f1.read())
f1.close()
f2.close()
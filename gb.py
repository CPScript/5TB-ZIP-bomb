import os#,threading

# 1gb = 1024.1024.1024

# 1kb = 1024
# 1mb = 1024.1024
# 1gb = 1024.1024.1024

def gb(isim):
    open(isim,"wb").write(os.urandom(1024**3))


for i in range(90): # 90 gb veri için .
    print(i)
    gb( str(i) )


    #threading.Thread(target=gb,args=(str(i),)).start()

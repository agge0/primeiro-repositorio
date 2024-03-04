import segno, sys

try:
    info = sys.argv[1]

    if len(info) > 0:
        qr = segno.make_qr(info)

        qr.save("ageQr1.png",
                scale=6,
                border=0)
    else:
        print("error!!Exemplo:> python main.py +258870152510")

except:
    print("error!!Exemplo:> python main.py ageChabane")

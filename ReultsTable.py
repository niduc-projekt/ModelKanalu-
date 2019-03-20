import sys
from typing import TextIO

dataNumber=0
correctData=0
failData=0

with open("Stats.txt",'w') as output:
    with open("DataGenerated.txt",'r') as inputX:
        with open("DataRecived.txt",'r') as inputY:

                while True:
                    byteX= inputX.read(1)
                    byteY= inputY.read(1)
                    if not byteX: break
                    if byteX==byteY:
                       correctData +=1
                    else:
                        failData +=1
                    dataNumber +=1

    procOfGood = ((float(100) * float(correctData)) / float(dataNumber))
    print("Procent poprawnych bitów: ",procOfGood," %")
    print("Ilość złych bitów: ",failData)
    print("Ilość dobrych bitów: ",correctData)
    print("Ilość wszystkich bitów: ",dataNumber)



    output.write("Procent poprawnych bitów: "+str(procOfGood)+" %"+"\n")
    output.write("Ilość złych bitów: "+str(failData)+"\n")
    output.write("Ilość dobrych bitów: "+str(correctData)+"\n")
    output.write("Ilość wszystkich bitów: "+str(dataNumber)+"\n")

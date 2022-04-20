import os
import subprocess
import re
import sys
import Properties


def changePars(alpha, beta):
    file_path = "/Users/zhaoxiang/Desktop/Class/big data/CW/EPOS-jar/conf/epos.properties"
    new_par = "\"" + str(alpha) + " ," + str(beta) + "\""

    properties_path = '/Users/zhaoxiang/Desktop/Class/big data/CW/EPOS-jar/conf/epos.properties'
    p = Properties.Properties()
    p.load(open(properties_path))
    p['weightsString'] = new_par
    p.store(open(properties_path, 'w'))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    path = "/Users/zhaoxiang/Desktop/Class/big\ data/CW/EPOS-jar"
    command = "cd /Users/zhaoxiang/Desktop/EPOS-jar && java -jar IEPOS-Tutorial.jar"
    changePars(0, 0)

    for i in range(3):
        beta = float((i+1) / 10)
        changePars(0.3, beta)
        os.system(command)



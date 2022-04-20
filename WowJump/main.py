import os
import Properties
import threading


def changePars(alpha, beta):
    new_par = "\"" + str(alpha) + " ," + str(beta) + "\""

    properties_path = '../EPOS-jar/conf/epos.properties'
    p = Properties.Properties()
    p.load(open(properties_path))
    p['weightsString'] = new_par
    p.store(open(properties_path, 'w'))


if __name__ == '__main__':
    command = "cd ../EPOS-jar && java -jar IEPOS-Tutorial.jar"
    changePars(0, 0.3)
    count = 0
    for i in range(100):
        for j in range(100):
            alph = float((i+1) / 10)
            beta = float((j+1) / 10)
            if alph+beta < 1:
                changePars(alph, beta)
                os.system(command)
    print(count)



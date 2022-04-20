import os
import Properties
from os import path
import pandas


def changePars(alpha, beta):
    new_par = "\"" + str(alpha) + " ," + str(beta) + "\""

    properties_path = '../EPOS-jar/conf/epos.properties'
    p = Properties.Properties()
    p.load(open(properties_path))
    p['weightsString'] = new_par
    p.store(open(properties_path, 'w'))

def scaner_file(url):
    reMin = 9999
    alpha = 0
    beta = 0
    count = 0
    file = os.listdir(url)
    file_handle = open('../result.txt', mode='w')
    for f in file:
        count = count + 1
        if f == ".DS_Store":
            continue
        real_url = path.join(url, f)
        try:
            df = pandas.read_csv(real_url + "/global-cost.csv")
            df_par = pandas.read_csv(real_url + "/weights-alpha-beta.csv")
        except:
            file_handle.write(real_url + "   error" + ' \n')
        tmin = findMin(df.min()["Run-0"],df.min()["Run-1"],df.min()["Run-2"],df.min()["Run-3"],df.min()["Run-3"])
        if tmin < reMin:
            reMin = tmin
            alpha = df_par["Unfairness weight"][0]
            beta = df_par["Local cost weight"][0]
            text = str(reMin) + "  " + str(alpha) + "  " + str(beta)
            file_handle.write(text + ' \n')
    print(count)
    file_handle.close()


def findMin(a,b,c,d,e):
    return min(e, min(min(a, b), min(c, d)))

if __name__ == '__main__':
    command = "cd ../EPOS-jar && java -jar IEPOS-Tutorial.jar"
    count = 0
    for i in range(1000):
        for j in range(1000):
            alph = float(i / 100)
            beta = float(j / 100)
            if alph+beta < 1:
                changePars(alph, beta)
                os.system(command)
    print(count)
    scaner_file("../EPOS-jar/output")


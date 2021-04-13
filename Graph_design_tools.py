import pandas as pd
import matplotlib.pyplot as plt
import argparse


# for command
parser = argparse.ArgumentParser()

parser.add_argument('-f', help='type file name / path',
                    type=str, required=True)
parser.add_argument('-c', dest='choice', help='file info',
                    choices=['info', 'head'])

parser.add_argument('--p', help='column title name', type=str)
parser.add_argument('-s', help='select particular row')



args = parser.parse_args()
df = pd.read_csv(args.f)



# all function

def info():
    print(df.info())


def head():
    print(df.head())


# logic

if args.choice == 'info':
    try:
        info()
    except Exception as e:
        print(e)

elif args.choice == 'head':
    try:
        head()
    except Exception as e:
        print(e)

elif args.p:
    if args.s:

        rowname = args.s                        # for row name
        rowname = df[df[args.p] == rowname]
        print(rowname)
        x=input('write the x value : ')
        y=input('write the y value : ')
        plt.plot(rowname[x],rowname[y])
        plt.show()


    else:
        tabname = args.p                        # for column title name
        tabname = df[tabname]
        print(tabname)

else:
    parser.print_help()
    exit(-1)




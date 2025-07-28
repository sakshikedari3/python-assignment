import numpy as np

def main() :
    data = {'salary' : [25000, 27000, 29000, 31000, 50000, 100000]}

    values = list(data.values())
    q1 = np.percentile(values, 25, interpolation = 'midpoint')
    q3 = np.percentile(values, 75, interpolation = 'midpoint')

    IQR = q3 - q1

    print("IQR is :",IQR)

if __name__ == "__main__" :
    main()
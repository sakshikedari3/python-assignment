import pandas as pd

def main() :
    data = {'marks' : [85, None, 90, None, 95]}
    df = pd.DataFrame(data)
    interpolate = df.interpolate()

    print(interpolate)
    


if __name__ == "__main__" :
    main()
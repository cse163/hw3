import pandas as pd
import seaborn as sns
# Your imports here


# Define your functions here


def main():
    data = pd.read_csv('nces-ed-attainment.csv', na_values=['---'])
    sns.set()
    # Call your functions here


if __name__ == '__main__':
    main()

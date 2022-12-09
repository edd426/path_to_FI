from sqlite3 import Timestamp
import pandas as pd


class MintCsvTransformer:

    def __init__(self, mint_spending_path, mint_net_worth_path):
        self.mint_df = self.generate_mint_df(mint_spending_path,
                                             mint_net_worth_path)

    def generate_mint_df(self, mint_spending_path, mint_net_worth_path):

        def convert_from_dollar(dollar_sign_value):
            return float(dollar_sign_value.replace('$', '').replace(',', ''))

        def to_datetime(date_str):
            datetime_conv = pd.to_datetime(date_str, errors='ignore')
            if isinstance(datetime_conv, pd.Timestamp):
                return datetime_conv.date()
            else:
                return datetime_conv

        spending_converter = {
            'DATES': to_datetime,
            'Spending': convert_from_dollar
            }
        net_worth_converter = {
            'DATES': to_datetime,
            'Assets': convert_from_dollar,
            'Debts': convert_from_dollar,
            'NET': convert_from_dollar
        }

        spending_df = pd.read_csv(mint_spending_path,
                                  converters=spending_converter)
        net_worth_df = pd.read_csv(mint_net_worth_path,
                                   converters=net_worth_converter)

        spending_df = spending_df.loc[spending_df.loc[:, 'DATES'] != 'Total']

        net_worth_df.set_index('DATES')
        spending_df.set_index('DATES')

        mint_df = pd.merge(net_worth_df, spending_df, on='DATES', how='outer',
                           sort=True)
        print(mint_df)

        # mint_df = pd.concat([net_worth_df, spending_df],
        #                     axis=1)
        # mint_df.dropna(axis='index', how='any', inplace=True)
        # mint_df.drop(mint_df.tail(1).index, inplace=True)
        mint_df.to_csv('./debug.csv')
        return mint_df

    def get_mint_df(self):
        return self.mint_df

import pandas as pd


class MintCsvTransformer:

    def __init__(self, mint_spending_path, mint_net_worth_path):
        self.mint_df = self.generate_mint_df(mint_spending_path,
                                             mint_net_worth_path)

    def generate_mint_df(self, mint_spending_path, mint_net_worth_path):

        def convert_from_dollar(dollar_sign_value):
            return float(dollar_sign_value.replace('$', '').replace(',', ''))

        def to_datetime(date_str):
            return pd.to_datetime(date_str, errors='ignore')

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
        mint_df = pd.concat([net_worth_df, spending_df['Spending']],
                            axis=1)
        mint_df.dropna(axis='index', how='any', inplace=True)
        mint_df.drop(mint_df.tail(1).index, inplace=True)
        print(mint_df.dtypes)
        print(mint_df['DATES'].iat[0])
        print(type(mint_df['DATES'].iat[0]))
        return mint_df

    def get_mint_df(self):
        return self.mint_df

import sys
import seaborn as sns
from mint_csv_transformer import MintCsvTransformer
from mint_plotter import MintPlotter

def main(path_to_mint_spending_csv, path_to_mint_net_worth_csv):
    mint_tr = MintCsvTransformer(path_to_mint_spending_csv,
                                 path_to_mint_net_worth_csv)

    mint_pl = MintPlotter(mint_tr.get_mint_df())
    mint_pl.plot_net_worth_over_yearly_spending()


    # mint_df = mint_tr.get_mint_df()
    # print(mint_df.columns)
    # print(mint_df.loc[:, 'Amount'].sum())

if __name__ == '__main__':
    # print(sys.argv[1])
    main(sys.argv[1], sys.argv[2])  # pass the path to the mint data

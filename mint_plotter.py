from copy import deepcopy
import seaborn as sns
import matplotlib.pyplot as plt


class MintPlotter:

    def __init__(self, mint_df):
        self.mint_df = mint_df

    def plot_spending(self):
        
        plt.figure()
        # Plot the lines on two facets
        sns.lineplot(
            data=self.mint_df,
            x="DATES", y="Spending",
        )
        plt.show()

    def plot_sample(self):

        sns.set_theme(style="ticks")
        dots = sns.load_dataset("dots")
        palette = sns.color_palette("rocket_r")

        plt.figure()
        # Plot the lines on two facets
        sns.relplot(
            data=dots,
            x="time", y="firing_rate",
            hue="coherence", size="choice", col="align",
            kind="line", size_order=["T1", "T2"], palette=palette,
            height=5, aspect=.75, facet_kws=dict(sharex=False),
        )
        plt.show()

    def plot_net_worth_over_spending(self):

        self.mint_df['Net Worth Over Spending'] = \
            self.mint_df['NET'] / self.mint_df['Spending']

        self.mint_df['FI'] = 300

        plt.figure()
        # Plot the lines on two facets
        sns.lineplot(
            data=self.mint_df,
            x="DATES", y='Net Worth Over Spending',
        )

        sns.lineplot(
            data=self.mint_df,
            x="DATES", y='FI',
        )
        plt.show()

    def plot_net_worth_over_yearly_spending(self):
        win_num = 12
        # local_mint_df = self.mint_df.copy(deep=True)
        rolling_mint_df = self.mint_df.loc[:, ['Spending']] \
            .rolling(window=win_num).sum()
        print(rolling_mint_df)
        print(len(self.mint_df.loc[win_num:, 'NET']))
        rolling_mint_df['NET'] = self.mint_df.loc[win_num:, 'NET']
        rolling_mint_df['DATES'] = self.mint_df.loc[win_num:, 'DATES']

        rolling_mint_df['Net Worth Over Yearly Spending'] = \
            rolling_mint_df['NET'] / rolling_mint_df['Spending']

        rolling_mint_df['FI'] = 25
        
        rolling_mint_df.dropna(axis='index', how='any', inplace=True)

        print(rolling_mint_df)

        plt.figure()
        # Plot the lines on two facets
        sns.lineplot(
            data=rolling_mint_df,
            x="DATES", y='Net Worth Over Yearly Spending',
        )

        sns.lineplot(
            data=rolling_mint_df,
            x="DATES", y='FI',
        )
        plt.show()

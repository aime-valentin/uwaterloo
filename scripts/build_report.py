#! /usr/bin/python3
#created by: aime nishimwe
#created at: Avery Hall, UNL
#created on: March 17, 2022

#library imports
import matplotlib.pyplot as plt
import seaborn as sns
from data_processing import clean_data
from data_load import define_range

colsepname = ''
def save_table(df, filename, decimals=2, colsep=False, **kwargs):
	global colsepname
	if not colsep is False:
		colsepname = colsepname + 'A'

	pd.options.display.float_format = ('{:,.' + str(decimals) + 'f}').format

	with pd.option_context("max_colwidth", 1000):
		tab1 = df.to_latex(**kwargs)
	# print(tab1)
	with open(filename,'w',encoding='utf-8') as f:
		f.write('% DO NOT EDIT\n')
		f.write('% this file was automatically generated\n')
		if not colsep is False:
			f.write('\\newcommand{\\oldtabcolsep' + colsepname + '}{\\tabcolsep}\n')
			f.write('\\renewcommand{\\tabcolsep}{' + colsep + '}\n')
		f.write(tab1)
		if not colsep is False:
			f.write('\\renewcommand{\\tabcolsep}{\\oldtabcolsep' + colsepname +'}\n')

def make_bar_plot(df,xaxis, yaxis, title, xlabel, ylabel, path):
    sns.set_style('whitegrid')
    sns.set_context('notebook')
    sns.barplot(x = xaxis, y = yaxis, data =df)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation = 45)
    plt.savefig(path, dpi = 300)

def report_files():
    from_, to_ = define_range(6)
    active_mod, churn = clean_data()
    summary_stats = churn[['churn']].describe()
    save_table(summary_stats,'report/tables/churn_rate_summary_stats.tex')
    make_bar_plot(active_mod,'module','commit_hash','12 Most Active Modules','Modules','Commit Counts','report/figures/top12_active_modules.png')
    make_bar_plot(churn,'module','churn','12 Modules With High Churn Rate','Modules','Churn',"report/figures/top12_modules_with_most_churn")
    with open("report/study_period.txt") as f:
        f.write("OpenStack Nova Project\n")
        f.write(f"Study Period: {from_.date} to {to_.date}")

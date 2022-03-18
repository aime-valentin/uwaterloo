#! /usr/bin/python3
#created by: aime nishimwe
#created at: Avery Hall, UNL
#created on: March 17, 2022

#library imports
import pydriller as pdr
import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta

#define the range of study period
def define_range(n):
    to_tag = datetime.now()
    from_tag   = to_tag - relativedelta(months = n)
    return (from_tag, to_tag)

def create_df(repo):
    dfs = []
    for commit in repo.traverse_commits():
        commit_hash = commit.hash
        commit_add_ln = commit.insertions
        commit_rem_ln = commit.deletions
        modified_files_old_paths = [i.old_path for i in commit.modified_files]
        modified_files_new_paths = [i.new_path for i in commit.modified_files]
        df = pd.DataFrame.from_dict({
        'old_path': modified_files_old_paths,
        'new_path': modified_files_new_paths
        })
        df['commit_hash']   = commit_hash
        df['added_lines']   = commit_add_ln
        df['removed_lines'] = commit_rem_ln
        dfs.append(df)
    return pd.concat(dfs)
#extract data
def data_extract(repo_url,from_, to_):
    repo = pdr.Repository(repo_url, since = from_, to = to_, only_in_branch = 'master')
    data = create_df(repo)
    data.to_pickle("data/data.pkl")

def main():
    repo_url  = "https://github.com/openstack/nova.git"
    from_,to_ = define_range(6)
    data_extract(repo_url, from_, to_)

if __name__ == '__main__':
    main()
    # from_, to_  = define_range(6)
    # commits = list(pdr.Repository("https://github.com/openstack/nova.git", from_tag = from_, to_tag = to_, only_in_branch = 'master').traverse_commits())
    # print(len(commits))

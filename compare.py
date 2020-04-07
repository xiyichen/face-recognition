import pandas as pd

# compare the matching scores of editted and original faces

df_sr = pd.read_csv('./cleanedup_matching_sr.csv')
df_or = pd.read_csv('./cleanedup_matching.csv')
match_sr = []
match_or = []
for i in range(len(df_sr)):
	id = df_sr.loc[i]['identity'].astype(int)
	file = df_sr.loc[i]['file'].astype(int)
	match_sr.append(df_sr.loc[i]['best_matching_score'])
	match_or.append(df_or[(df_or.identity == id) & (df_or.file == file)]['best_matching_score'].values[0])

l = len(match_sr)
count = 0
for i in range(l):
	if match_sr[i] <= match_or[i]:
		count += 1
print(count/l)
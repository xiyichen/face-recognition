import pandas as pd

df_matching = pd.read_csv('./matching.csv', index_col=[0])
print(df_matching)

file_group = df_matching.groupby(['identity', 'file'])
cleanedup = pd.DataFrame()
for id_file, df_id_file in file_group:
	print(id_file)
	if len(df_id_file) > 1:
		df_id_file.sort_values(['query_id_position'], ascending=True, inplace=True)
	cleanedup = cleanedup.append(df_id_file.head(1))

cleanedup.to_csv('./cleanedup_matching.csv')

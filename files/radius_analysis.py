import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def safe_lower(item):
    if type(item) == str:
        return item.lower()
    return item
def num_conv(n):
    if not n:
        return np.nan
    if n.isdigit():
    	return float(n)
    return n
def phone_conv(n):
	return num_conv(n.replace('(', '').replace(')','').replace('-','').replace(' ', ''))

def not_null(df, col):
	return sum(df[col].notnull())
	
def cardinality(df, col):
	return len(map(safe_lower, set(df[col])))

def true_val_str(df, col, vals=['0', ' ', 'none']):
	return sum(df[col].notnull()) - sum(df[col].isin(vals))
	
def str_cat(df, cat):
	print 'Values for ' + cat
	print 'Non-null: ' + str(not_null(df, cat))
	print 'True valued: ' + str(true_val_str(df, cat))
	print 'Cardinality: ' + str(cardinality(df, cat))
	print '\n'
	
def valid_num_i(n, lb, ub):
    if type(n) != float:
        return False
    return n >= lb and n <= ub
def valid_num(df, cat, lb, ub):
	return sum(map(lambda x: valid_num_i(x, lb, ub), df[cat]))
	
def str_num(df, cat, lb, ub):
	print 'Values for ' + cat
	print 'Non-null: ' + str(not_null(df, cat))
	print 'True valued: ' + str(valid_num(df, cat, lb, ub))
	print 'Cardinality: ' + str(cardinality(df, cat))
	print '\n'
	
convs = {'zip': num_conv, 'phone': phone_conv, 'category_code': num_conv}
dtype = {'city': str, 'name': str, 'revenue': str, 'state': str, 'address': str, 'time_in_business': str, 'headcount': str}

df = pd.read_csv('data.csv', dtype=dtype, converters=convs)

for col in dtype.keys():
	str_cat(df, col)
	
str_num(df, 'zip', 501, 99999)

str_num(df, 'category_code', 10000000, 99999999)

str_num(df, 'phone', 2000000000, 9999999999)

# get zip code coordinates
zips = pd.read_csv('zip_coord.csv')

# select records with valid zip and industry
df_z = df.loc[(df['zip'] >= 601) & (df['zip'] <= 99929) & (df['category_code'] >= 10000000) & (df['category_code'] <= 99999999)]

df_z['zipc'] = df_z['zip'].astype(int)
df_z['cat'] = df_z['category_code'].astype(int)

df_z['cat2'] = (df_z['cat']/1000000).astype(int)
df_z['cat3'] = (df_z['cat']/100000).astype(int)
df_z['cat4'] = (df_z['cat']/10000).astype(int)
df_z['cat5'] = (df_z['cat']/1000).astype(int)
df_z['cat6'] = (df_z['cat']/100).astype(int)

# values of category codes
naics = pd.read_csv('naics.csv', dtype = {'code': int})

# limit zip codes to the continental US, in order to map easier
zips_conus = zips[(zips['ZIP'] < 601) | (zips['ZIP'] > 999)&(zips['ZIP'] < 96701) | 
                 (zips['ZIP'] > 97000)&(zips['ZIP'] < 99501)]

# calculate number of businesses by zip code
zips_companies = df_z.groupby('zipc').count()[['cat', 'cat2']]

# merge with coordinates
zips_merged = zips_companies.merge(zips_conus, how='inner', left_index=True, right_on='ZIP')
zips_merged['log_count'] = np.log(zips_merged['cat'])

# plot a geographical map of business density by zip code
# zips_merged.plot(kind='scatter', x='LNG', y='LAT', alpha=1, c='log_count', cmap=plt.get_cmap('Greens'), colorbar=True, 
#                  edgecolors='none', marker='.', figsize=(11,7))
# plt.savefig('zip_plot.png')
# plt.close()

# count businesses by 2-digit industry code
ind_counts = df_z.groupby('cat2').count()[['zipc', 'cat']]
c = ind_counts.merge(naics, left_index=True, right_on='code', how='inner')[['zipc', 'code', 'title']]
print c
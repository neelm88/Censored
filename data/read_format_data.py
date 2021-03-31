import pandas as pd 
import re
import numpy as np
df = pd.read_csv('raw_labeled_data.csv')  
http_regex = '(http|ftp|https)(:\/\/)([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?'
rt_regex = "RT"
username_regex = '@[a-zA-Z0-9_]*'
decimal_rep_regex = '&#[0-9]*|&amp;' # For &#.... or $amp;
special_char_regex = '[^A-Za-z0-9 ]'
combined_regex = '|'.join((http_regex,rt_regex,username_regex,decimal_rep_regex,special_char_regex))
df['tweet']=  [re.sub(combined_regex,'', str(text)) for text in df['tweet']]
space_regex = "\\s+"
start_space = "^\s"
end_space = "[ \t]+$"
df['tweet']=  [re.sub(space_regex,' ', str(text)) for text in df['tweet']]
df['tweet']=  [re.sub('|'.join((start_space, end_space)),'', str(text)) for text in df['tweet']]
df['tweet'].replace('', np.nan, inplace=True)
df.dropna(subset=['tweet'], inplace=True)
df.to_csv('labeled_data.csv', index=False)
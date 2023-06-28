# Import your libraries
import pandas as pd

# Start writing code
playbook_users.head()
appleProds = ['macbook pro', 'iphone 5s', 'ipad air']
all_users = playbook_events.merge(playbook_users[['user_id', 'language']], on='user_id')
all_users_count = all_users.groupby('language')['user_id'].nunique().to_frame('n_total_users')

apple_users = all_users[all_users['device'].isin(appleProds)].groupby('language')['user_id'].nunique().to_frame('n_apple_users').reset_index()

res = apple_users.merge(all_users_count, on='language', how='outer').fillna(0).sort_values(by='n_total_users', ascending=False)
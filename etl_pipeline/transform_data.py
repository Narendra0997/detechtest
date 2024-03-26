def post_length_category(body):
    if len(body) > 100:
        return "lengthy"
    else:
        return "concise"

# Apply the function to create a new column 'status'
df_posts['status'] = df_posts['body'].apply(post_length_category)

merged_df = pd.merge(df_posts, df_users, left_on='userId', right_on = 'id', how='left')

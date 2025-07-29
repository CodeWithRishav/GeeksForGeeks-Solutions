def find_invalid_comments(df):
    # Filter comments where the content length is greater than 20
    return df[df['content'].str.len() > 20][['comment_id']]
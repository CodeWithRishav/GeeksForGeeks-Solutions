def find_rank_scores(df):
    # Sort scores in descending order
    df_sorted = df.sort_values('score', ascending=False).reset_index(drop=True)

    # Create a new 'rank' column that assigns ranks
    df_sorted['rank'] = df_sorted['score'].rank(method='min',
                                                ascending=False).astype(int)

    return df_sorted[['score', 'rank']]
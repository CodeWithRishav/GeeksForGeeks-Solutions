def count_unique_projects(df):
    # Group by employee_id and count the unique project_id for each employee
    result = df.groupby('employee_id').agg(cnt=('project_id',
                                                'nunique')).reset_index()

    return result
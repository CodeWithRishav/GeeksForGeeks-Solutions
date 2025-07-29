def find_patients_with_hypertension(df):
    # Filter patients with conditions starting with 'HTN'
    result = df[df['conditions'].str.startswith('HTN')]
    return result[['patient_id', 'patient_name', 'conditions']]
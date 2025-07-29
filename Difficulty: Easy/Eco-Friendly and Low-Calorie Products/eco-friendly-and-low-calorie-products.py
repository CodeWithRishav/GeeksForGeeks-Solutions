def find_eco_low_calorie_products(df):
    # Filter products that are both eco-friendly and have low calories
    result = df[(df['eco_friendly'] == 'Y') & (df['calories'] <= 200)]
    return result[['product_id', 'product_name', 'calories']]
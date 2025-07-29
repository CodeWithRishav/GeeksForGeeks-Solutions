def count_city_population_categories(df):
    categories = {
        "Small City":
        len(df[df['population'] < 100000]),
        "Medium City":
        len(df[(df['population'] >= 100000) & (df['population'] <= 1000000)]),
        "Large City":
        len(df[df['population'] > 1000000])
    }
    result = pd.DataFrame(list(categories.items()),
                          columns=['category', 'cities_count'])
    return result
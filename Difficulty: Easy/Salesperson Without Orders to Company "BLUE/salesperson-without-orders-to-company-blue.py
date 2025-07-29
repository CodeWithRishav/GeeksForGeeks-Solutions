def find_salesperson_without_blue_orders(df_salesperson, df_orders,
                                         df_company):
    # First, find all orders that are related to 'BLUE' company
    blue_orders = df_orders[df_orders['com_id'] == df_company[
        df_company['name'] == 'BLUE']['com_id'].values[0]]

    # Get all sales_id from these orders
    sales_with_blue = blue_orders['sales_id'].unique()

    # Filter salespersons who did not have any orders to 'BLUE'
    result = df_salesperson[~df_salesperson['sales_id'].isin(sales_with_blue)]

    return result[['name']]
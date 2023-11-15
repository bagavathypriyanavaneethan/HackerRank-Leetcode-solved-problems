import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:

    res = pd.merge(customers,orders,left_on='id',right_on = 'customerId',how='left',suffixes=('_cus','_ord'))

    res = res[res['id_ord'].isna()]
    res = res.rename(columns = {'name':'Customers'})

    return res[['Customers']]
    

import pandas as pd

def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    
    result = pd.merge(sales,product,on='product_id',how='inner')
    # #result['total'] = result['quantity']*result['price']
    # print(result)

    return result.loc[:,['product_name','year','price']]

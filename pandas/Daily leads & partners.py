import pandas as pd

def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:

    res = daily_sales.groupby(['date_id','make_name']).nunique(['lead_id','partner_id']).reset_index()

    res.rename(columns = {'lead_id':'unique_leads','partner_id':'unique_partners'},inplace = True)

    return res
    

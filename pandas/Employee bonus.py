import pandas as pd

def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    
    res = pd.merge(employee,bonus,how='left',on='empId')
    res = res[(res['bonus'].isna()) | (res['bonus'] < 1000)]

    return res[['name','bonus']]

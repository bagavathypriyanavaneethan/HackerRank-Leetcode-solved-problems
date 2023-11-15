import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:

    result = pd.merge(employee,employee,left_on = 'managerId',right_on='id',how = 'inner',suffixes = ('_emp','_mngr'))
    result = result[result['salary_emp'] > result['salary_mngr']]
    result = result.rename(columns = {'name_emp':'Employee'})

    return result[['Employee']]
    

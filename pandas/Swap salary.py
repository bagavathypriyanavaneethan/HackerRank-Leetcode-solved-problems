import pandas as pd

def swap_salary(salary: pd.DataFrame) -> pd.DataFrame:
    print(salary)

    for i in range(salary.shape[0]):
        if salary.iat[i,2] == 'f':
            salary.iat[i,2] = 'm'
        elif salary.iat[i,2] == 'm':
            salary.iat[i,2] = 'f'
    
    return salary

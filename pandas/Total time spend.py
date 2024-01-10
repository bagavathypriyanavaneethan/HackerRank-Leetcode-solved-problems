import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    
    employees['timespend'] = employees['out_time'] - employees['in_time']

    res = employees.groupby(['event_day','emp_id']).sum('timespend').reset_index()
    res = res.rename(columns = {'event_day':'day',
    'timespend':'total_time'
    })
    print(res)
    return res[['day','emp_id','total_time']]
    

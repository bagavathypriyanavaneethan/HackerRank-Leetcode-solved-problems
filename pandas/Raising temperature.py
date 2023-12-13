import pandas as pd
import numpy as np

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:

    weather = weather.sort_values(by='recordDate')
    # weather['recordDate'] = pd.to_datetime(weather['recordDate'])

    weather['previousDate'] = weather['recordDate'].shift(1)
    weather['previous_temp'] = weather['temperature'].shift(1) 

    return weather[ (weather['temperature']>weather['previous_temp']) & (weather['recordDate'] == weather['previousDate'] + pd.Timedelta(days=1))][['id']]

    

import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    duplicate_df = person[person.duplicated(subset='email',keep='first')]
    duplicate_df = pd.DataFrame(duplicate_df['email'].unique(),columns=['Email'])

    return duplicate_df

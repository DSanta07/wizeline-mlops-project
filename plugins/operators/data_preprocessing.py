import pandas as pd

def preprocess(bookings_df):
    # Step 1: Handle Missing Values
    bookings_df['children'] = bookings_df['children'].fillna(bookings_df['children'].median())
    bookings_df['country'] = bookings_df['country'].fillna(bookings_df['country'].mode()[0])
    bookings_df['agent'] = bookings_df['agent'].fillna(-1)  # Using -1 to indicate missing agent
    bookings_df['company'] = bookings_df['company'].fillna(-1)  # Using -1 to indicate missing company
    
    # Step 2: Drop 'reservation_status_date'
    bookings_df.drop(columns=['reservation_status_date'], inplace=True)

    # Step 3: Remove Duplicates
    bookings_df = bookings_df.drop_duplicates()

    print("INFO: Data preprocessed...")

    return bookings_df
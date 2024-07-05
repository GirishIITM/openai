import csv
from googleapiclient.discovery import build


def fetchSheetData():
    api_key = 'AIzaSyDEKLTbfQmokfpOq57Z46yjeZcGLZikUZk'

    spreadsheet_id = '1BV12RbJNqAWNFz1oXZ3Mzud-W5-3ntF-qNIPd4qwzZE'
    range_name = 'Sheet1!A1:E47'
    service = build('sheets', 'v4', developerKey=api_key)

    try:
        result = service.spreadsheets().values().get(
            spreadsheetId=spreadsheet_id,
            range=range_name
        ).execute()

        values = result.get('values', [])

        if not values:
            print('No data found.')
        else:
            # print(values)
            with open('apartment_data.csv', mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(values)

    except Exception as err:
        print(f'An error occurred: {err}')


fetchSheetData()

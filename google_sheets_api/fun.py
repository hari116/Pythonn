from __future__ import print_function
import pickle
import os.path
from pprint import pprint

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
# permissons, visit auth reqs in G docs
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']  # .readonly if read only
creds = None

# The ID and range of a sample spreadsheet.
# SPREADSHEET_ID = '1Oq8CAD8Y7LSIw4Md0vy4g_83CtS6ibIB3ekQqNYdIGc'  # test.xlsx
SPREADSHEET_ID = '1Ib86_qGr_Lx6DKL7RjMfivlCYyjVJmVPP-Ev01vuLIk'  # oriental.xlsx
RANGE_NAME = 'Pvt.Car!C5'
RANGE_NAMES = ['Sheet1', 'Sheet2']


def getCreds():
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    # Just like json
    global creds
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    # print('getCreds ran')


def readSheets(READ_RANGE):
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    # Call the sheets API
    SheetService = service.spreadsheets()
    request = SheetService.values().get(spreadsheetId=SPREADSHEET_ID, range=READ_RANGE, majorDimension='ROWS')
    response = request.execute()
    values = response.get('values', [])  # =response['values']
    for row in values:
        for cell in row:
            print(cell, end=' ')
        print('\n')


def batchRead():
    # request = service.spreadsheets().values().batchGet(spreadsheetId=spreadsheet_id, ranges=ranges, valueRenderOption=value_render_option, dateTimeRenderOption=date_time_render_option)
    print("Batch reading")
    request = service.spreadsheets().values().batchGet(spreadsheetId=SPREADSHEET_ID, ranges=RANGE_NAMES)
    response = request.execute()
    pprint(response)
    valueRanges = response.get('valueRanges', [])
    pprint(valueRanges[0].get('values'))
    pprint(valueRanges[1].get('values'))


def createSheets(title):
    """
    Creating a spread sheet
    """
    # getCred() already ran
    print('Before create')
    # spreadsheet dict. Ref: https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets
    ss_dict = {
        'properties': {
            'title': title
        }
    }
    request = service.spreadsheets().create(body=ss_dict, fields='spreadsheetId,spreadsheetUrl,properties')
    response = request.execute()
    print(response)
    print('Spreadsheet Id: {0}'.format(response.get('spreadsheetId')))
    print('After create')


def updateSheets():
    print('Begining update')
    values = [
        [750000]
    ]
    body = {
        # 'range': 'Sheet2!A1:A2', NOT WORKING...
        'majorDimension': 'COLUMNS',
        'values': values
    }
    request = service.spreadsheets().values().update(
        spreadsheetId=SPREADSHEET_ID,
        range=RANGE_NAME,
        valueInputOption='USER_ENTERED',
        body=body
    )
    response = request.execute()
    pprint(response)


def batchUpdate():
    value = [
        [[360000, 75000, 12, 12]],
        [[2015, 'A', 1200]]
    ]
    data = [
        {
            'range': 'Pvt.Car!C4:C7',
            'majorDimension': 'COLUMNS',
            'values': value[0]
        },
        {
            'range': 'Pvt.Car!G4:G6',
            'majorDimension': 'COLUMNS',
            'values': value[1]
        }
    ]
    body = {
        'valueInputOption': 'USER_ENTERED',
        'data': data
    }
    # print(data[0]['values'][1])
    # exit()
    request = service.spreadsheets().values().batchUpdate(
        spreadsheetId=SPREADSHEET_ID, body=body
    )
    response = request.execute()
    pprint(response)


"""main()"""

if __name__ == '__main__':
    # Immideately run getCred()
    getCreds()
    # Initializing service obj
    service = build('sheets', 'v4',
                    credentials=creds)  # service = discovery.build('sheets', 'v4', credentials=credentials)
    # updateSheets()
    batchUpdate()
    # readSheets('Pvt.Car!B33:G36')
    readSheets('Pvt.Car')
    # batchRead()
    # createSheets('new23dec4')

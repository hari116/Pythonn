from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
# permissons, visit auth reqs in G docs
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']  # .readonly if read only
creds = None

# The ID and range of a sample spreadsheet.
SPREADSHEET_ID = '1Oq8CAD8Y7LSIw4Md0vy4g_83CtS6ibIB3ekQqNYdIGc'  # test.xlsx
RANGE_NAME = 'Sheet1'


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
    print('getCreds ran')

# Immideately run getCred()
getCreds()


def readSheets():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    # Starts service
    service = build('sheets', 'v4', credentials=creds)
    # Call the sheets API
    SheetService = service.spreadsheets()
    request = SheetService.values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME)
    response = request.execute()
    values = response.get('values', [])  # =response['values']
    for row in values:
        for cell in row:
            print(cell, end=' ')
        print('\n')
    # print(values[0][0])


def createSheets(title):
    """
    Creating a spread sheet
    """
    print('Before create')
    # spreadsheet dict. Ref: https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets
    ss_dict = {
        'properties': {
            'title': title
        }
    }
    service = build('sheets', 'v4', credentials=creds)
    request = service.spreadsheets().create(body=ss_dict, fields='spreadsheetId')
    response = request.execute()
    print(response)
    print('Spreadsheet Id: {0}'.format(response.get('spreadsheetId')))
    print('After create')


if __name__ == '__main__':
    # readSheets()
    createSheets('new20dec2')

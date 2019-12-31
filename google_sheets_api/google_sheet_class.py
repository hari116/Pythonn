from __future__ import print_function
from pprint import pprint
import fun
import json


# service = ''
class sheetApi:
    # sheetName = 'GCCV_Public'
    # SPREADSHEET_ID = '1Ib86_qGr_Lx6DKL7RjMfivlCYyjVJmVPP-Ev01vuLIk'  # oriental.xlsx
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']  # .readonly if read only

    # coord = {}

    # coords = [  # list of tuples
    #     ('IDV', 'C4'),
    #     ('elec', 'C5'),
    #     ('CNGKV', 'C6'),
    #     ('manYr', 'G4'),
    #     ('vehicleWt', 'G5'),
    #     ('zone', 'G6'),
    # ]

    def __init__(self, spreadId, sheetName, ):
        self.sheetName = sheetName
        self.SPREADSHEET_ID = spreadId
        self.coords = self.coords()

    # @property
    def coords(self, term='IDV', coord='A1'):
        with open('google_sheets_api/coords.json') as f:
            j = json.load(f)
        return j

    def createCoords(self, crds=None):
        with open(f'google_sheets_api/{self.SPREADSHEET_ID}_{self.sheetName}.json', 'xt') as f:
            crds = {
                "IDV": "C4",
                "elec": "C5",
                "CNGKV": "C6",
                "manYr": "G4",
                "vehicleWt": "G5",
                "zone": "G6"
            }

            json.dump(crds, f, ensure_ascii=False, indent=4)

    def getCoords(self, key=None):
        if key is not None:
            return self.coords.get(key)
        else:
            return self.coords

    def updateCoords(self, term, value):
        coords = self.coords
        coords[term] = value
        with open(f'google_sheets_api/{self.SPREADSHEET_ID}_{self.sheetName}.json', 'wt') as f:
            json.dump(coords, f, ensure_ascii=False, indent=4)

    def read(self, range, mDim='ROWS'):
        rangeKey = f'{self.sheetName}!{range}'
        request = service.spreadsheets().values().get(spreadsheetId=self.SPREADSHEET_ID, range=rangeKey,
                                                      majorDimension=mDim)
        response = request.execute()
        values = response.get('values', [])  # =response['values']
        for row in values:
            for cell in row:
                print(cell, end='|')
            print('\n')

    def write(self, IDV, elec, CNGKV, manYr, vehicleWt, zone='A'):
        values = [
            [IDV, elec, CNGKV],
            [manYr, vehicleWt, zone]
        ]

        data = [
            {
                'range': f'{self.sheetName}!C4:C6',
                'majorDimension': 'COLUMNS',
                'values': [values[0]]
            },
            {
                'range': f'{self.sheetName}!G4:G6',
                'majorDimension': 'COLUMNS',
                'values': [values[1]]
            }
        ]
        body = {
            'valueInputOption': 'USER_ENTERED',
            'data': data
        }
        request = service.spreadsheets().values().batchUpdate(
            spreadsheetId=self.SPREADSHEET_ID, body=body,
            fields='responses'
        )
        resp = request.execute()
        pprint(resp)

    def loadCoords(self):
        with open('google_sheets_api/coords.json') as f:
            j = json.load(f)
        return j

    def getCoords(self, key=None):
        if key is not None:
            return self.coords.get(key)
        else:
            return self.coords

    def changeCoords(self, term='IDV', coord='A1'):
        pprint(self.getCoords())


if __name__ == '__main__':
    fun.getCreds()
    service = fun.build('sheets', 'v4',
                        credentials=fun.creds)  # service = discovery.build('sheets', 'v4', credentials=credentials)
    carrier1 = sheetApi('1Ib86_qGr_Lx6DKL7RjMfivlCYyjVJmVPP-Ev01vuLIk', 'GCCV_Public')
    # print(carrier1.)
    carrier1.write(700000, 20000, 12, 2016, 1200, 'C')
    carrier1.read('E31:G34')
    # pprint(carrier1.getCoords('elec'))
    # carrier1.changeCoords('IDV', 'A1')
    # carrier1.updateCoords()

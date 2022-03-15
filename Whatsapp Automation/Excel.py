from typing import Dict, List

import pandas as pd

from Logger import Logger


class ExcelReader:
    df: pd.DataFrame
    data: List[Dict[str, str]]

    def __init__(self) -> None:
        self.df = None
        self.data = []

        self.file_name = "data.xlsx"

        """ CONTACT START """
        self.name_header = "name"
        self.phone_number_header = "phone number"
        self.code_header = "code"
        self.image = "image"
        """ CONTACT END """

    def read(self):
        try:
            self.df = pd.read_excel(self.file_name, engine="openpyxl")
            Logger.log("Retrieving data from excel", 'INFO')
        except FileNotFoundError:
            Logger.log(f"Excel '{self.file_name}' not found", 'ERROR')

            columns = [
                self.name_header,
                self.phone_number_header,
                self.code_header
            ]

            self.df = pd.DataFrame([], index=[], columns=columns)
            self.df.to_excel(f"{self.file_name}", index=False)

            Logger.log(f"Excel '{self.file_name}' is created", 'INFO')
        else:
            Logger.log(f"{len(self.df.index)} contacts found.", 'INFO')

            for i in self.df.index:
                name = self.df[self.name_header][i]
                image = str(self.df[self.code_header][i]) + ".jpg"
                number = str(self.df[self.phone_number_header][i])

                if not number.startswith("0"):
                    number = "+20" + number

                if '+' not in number:
                    if not number.startswith("0"):
                        number = "+20" + number

                    if number.startswith("0"):
                        number = "+2" + number

                contact = {
                    self.name_header: name,
                    self.phone_number_header: number,
                    self.image: image,
                }

                self.data.append(contact)

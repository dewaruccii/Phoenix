from prettytable import PrettyTable
from datetime import datetime
from comment.comment import LightRed
from convert.convert import sizeConvert


def table(data):
    myTable = PrettyTable(
        [LightRed("Id File"), LightRed("File Name"), LightRed("File Size"), LightRed("Upload At")])
    # return data
    for i in data:
        time = int(i['upload_at'])
        date_time = datetime.fromtimestamp(time)
        t = date_time.strftime("%d %B, %Y")

        converted = sizeConvert(i['size_file'])
        myTable.add_row([i['id_file'], i['file_name'],
                        converted, t])
    return print(myTable)

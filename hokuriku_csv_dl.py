import csv
from datetime import datetime
from pathlib import Path

import dl_csv_fn


def main() -> None:
    start_ymd = '20180101'
    dtnow = datetime.now().strftime('%Y%m%d')
    _date: datetime
    for _date in dl_csv_fn.datetime_string_range(start_ymd, dtnow):
        csvfile: Path = Path(__file__).parent / 'data' / 'Hokuriku' / f'{_date.year}' / f'{_date.month}' / f'{_date}.csv'
        if not csvfile.exists():
            try:
                dl_csv_fn.hokuriku_pd_csv_dl(_date)
            except:
                err_csv: Path = Path(__file__).parent / 'err' / f'hokuriku_dl_err.csv'
                if not err_csv.exists():
                    err_csv.mkdir(parents=True)
                    err_csv.touch()
                with open(err_csv, 'a') as f:
                    writer = csv.writer(f)
                    writer.writerow([_date])
                    


if __name__ == '__main__':
    try:
        main()
    except:
        pass

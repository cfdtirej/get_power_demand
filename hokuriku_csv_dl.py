import csv
from datetime import date, datetime
from pathlib import Path

import dl_csv_fn


def main() -> None:
    start_ymd = '20180101'
    dtnow = datetime.now().strftime('%Y%m%d')
    _ymd: datetime
    for _ymd in dl_csv_fn.datetime_string_range(start_ymd, dtnow):
        csvfile: Path = Path(__file__).parent / 'data' / 'Hokuriku' / f'{_ymd.year}' / f'{_ymd.month}' / f'{_ymd}.csv'
        if not csvfile.exists():
            try:
                dl_csv_fn.hokuriku_pd_csv_dl(_ymd)
            except:
                err_csv: Path = Path(__file__).parent / 'err' / f'hokuriku_dl_err.csv'
                if not err_csv.exists():
                    err_csv.mkdir(parents=True)
                    err_csv.touch()
                with open(err_csv, 'a') as f:
                    writer = csv.writer(f)
                    writer.writerow([_ymd])
                    


if __name__ == '__main__':
    try:
        main()
    except:
        pass

import csv
import datetime
from datetime import datetime, timedelta
from os import write
from pathlib import Path
from typing import Any, List, Dict, Iterator
from pandas.io.pytables import Term
import requests


def datetime_string_range(start_ymd: str = '20180101', end_ymd: str = '20210101') -> Iterator[datetime]:
    """
    :param start: 始まりの日付(YYMMDD)
    :param end: 終わりの日付(YYMMDD) 
    :return: start~endまでの日付(YYMMDD)を返す 
    """
    start = datetime.strptime(start_ymd, '%Y%m%d').date()
    end = datetime.strptime(end_ymd, '%Y%m%d').date()
    for _day in range((end-start).days):
        dt = start + timedelta(_day)
        yield dt


def hokuriku_pd_csv_dl(ymd: datetime) -> None:
    """北陸のエリア需要csvをダウンロード
    :param ymd: 日付(YYMMDD),datetime_string_range()の返り値
    """
    url = f'http://www.rikuden.co.jp/nw/denki-yoho/csv/juyo_05_{ymd}.csv'
    res = requests.get(url)
    table: List[List[str]] = [[t for t in txt.split(',')] for txt in res.text.splitlines()]
    dl_dir: Path = Path(__file__).parent / 'data' / 'Hokuriku' / f'{ymd.year}' / f'{ymd.month}'
    if not dl_dir.is_dir():
        dl_dir.mkdir(parents=True)
    csvfile: Path = dl_dir / f'{ymd}.csv'
    if not csvfile.exists():
        csvfile.touch()
    with open(csvfile, 'w') as f:
        writer = csv.writer(f)
        writer.writerows(table)
    

if __name__ == '__main__':
    for d in datetime_string_range():
        print(d.month)
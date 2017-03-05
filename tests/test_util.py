import pytest
import pytz
from datetime import datetime
from pytz.reference import Pacific
from app import util


def test_same_date():
    ''' same time '''
    dt1 = datetime(2017, 3, 4, 12, 0, 0)
    dt2 = dt1
    rv = util.same_date(dt1, dt2, 'US/Pacific')
    assert rv is True

def test_same_date2():
    ''' same day '''
    dt1 = datetime(2017, 3, 4, 7, 59, 0)
    dt2 = datetime(2017, 3, 4, 0, 0, 0)
    rv = util.same_date(dt1, dt2, 'US/Pacific')
    assert rv is True

def test_same_date3():
    ''' not same dat '''
    dt1 = datetime(2017, 3, 4, 8, 1, 0)
    dt2 = datetime(2017, 3, 4, 0, 0, 0)
    rv = util.same_date(dt1, dt2, 'US/Pacific')
    assert rv is False

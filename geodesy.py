"""
Johnson O. Oguntuase's Matlab function library
Geo plu Bathy (GpB) Lab
University of Southern Mississippi
Geodesy functions
History:
2022/05/07
2019/11/09
"""

import pandas as pd
import numpy as np
from datetime import datetime
import calendar
# from typing import TypeAlias


def dayofweek1(yy, mm, dd):
	"""
	1 is added to shift the beginning of week from Monday to Sunday, so DoW = 0 is Sunday, DoW = 1 is Monday, and
	DoW = 6 is Saturday
	"""
	ts = pd.Timestamp(yy, mm, dd, 0, 0, 0)
	jdt = ts.to_julian_date() + 0.5
	dow = jdt.__floor__().__mod__(7) + 1
	return dow


def dayofweek2(yy, mm, dd):
	ts = pd.Timestamp(yy, mm, dd)
	dow = ts.day_of_week + 1
	return dow


def gps_week_num(yy, mm, dd):
	in_date = pd.Timestamp(yy, mm, dd)
	gps_ref_epoch = pd.Timestamp(1980, 1, 6, 0, 0, 0)
	gps_ref_epoch = gps_ref_epoch.to_julian_date()
	gps_wk_no = np.floor((in_date.to_julian_date() - gps_ref_epoch)/7)
	return gps_wk_no


def gps_calendar(sta='2021-12-01', sto='2021-12-31'):
	gps_cal = pd.DataFrame({"Date": pd.date_range(sta, sto)})
	gps_cal["day_name"] = gps_cal.Date.dt.day_name()
	gps_cal["doy"] = gps_cal.Date.dt.dayofyear
	gps_cal["dom"] = gps_cal.Date.dt.day
	gps_cal["dow"] = gps_cal.Date.dt.day_of_week + 1  # DoW = 0 is Sun and Dow = 6 is Sat
	temp = gps_cal.dow[:]
	temp = temp.array

	for kk in range(len(temp)):
		if temp[kk] == 7:
			temp[kk] = 0

	temp = pd.DataFrame(temp, columns=['dow'])
	gps_cal.dow = temp
	gps_ref_epoch = pd.Timestamp(1980, 1, 6, 0, 0, 0)
	xx = (gps_cal.Date - gps_ref_epoch) / 7
	xx = xx.dt.days
	xx.name = "gps_wk_no"
	gps_cal["gps_wk_no"] = xx
	return gps_cal


def tow_sec_2_hms(yy: int, mm: int, n_day: int, tow_sec):
	cv_t = []
	cv_date_time = []
	yyy = str(yy).rjust(4, "0")
	mmm = str(mm).rjust(2, "0")
	n_date = datetime(yy, mm, n_day)
	mm_range = calendar.monthrange(n_date.year, n_date.month)[1]
	sta = yyy + '-' + mmm + '-' + str(1).rjust(2, "0")
	sto = yyy + '-' + mmm + '-' + str(mm_range).rjust(2, "0")
	gps_cal = gps_calendar(sta=sta, sto=sto)
	n_cal = gps_cal[gps_cal.dom == n_day]
	sun_date = n_cal.dom - n_cal.dow
	tow_sec = np.array(tow_sec)
	dec_day = tow_sec / (60 * 60 * 24)
	d_day = np.fix(dec_day) + sun_date.array
	dow = np.fix(dec_day)
	dec_hr = (dec_day - dow) * 24
	hr = np.fix(dec_hr)
	dec_mm = (dec_hr - hr) * 60
	mmi = np.fix(dec_mm)
	dec_ss = (dec_mm - mmi) * 60
	sss = np.fix(dec_ss)
	mls = np.fix((dec_ss - sss) * 1000 * 1000)

	if np.size(yy) == 1:
		for ii in range(np.size(tow_sec)):
			i_day = d_day[ii]
			i_hr = hr[ii]
			i_mm = mmi[ii]
			i_ss = sss[ii]
			i_mls = mls[ii]
			tm = pd.Timestamp(yy, mm, int(i_day), int(i_hr), int(i_mm), int(i_ss), int(i_mls))
			cv_t.append(tm)
		cv_date_time = pd.DataFrame(data=cv_t, columns=["Date"])
	return cv_date_time

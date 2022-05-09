"""
Johnson O. Oguntuase's Matlab function library
Geo plu Bathy (GpB) Lab
University of Southern Mississippi
Geodesy functions
History:
2022/05/07
2019/11/09
"""

import os as os
from geodesy import *


# %%
def file_2_strct(f_path):
    """
    Defining export file header options for exported files from Qinertia, Kinematica, POSPAC-MMS, CSRS-PPP, GrafNav
    The function is expandable to handle any exported file formats provided the expected header and variable sections
    are well defined
    """
    hdr_qin_opt1 = "UTC Date	    UTC Time	UTC Time	Longitude	Longitude Std.	Latitude	Latitude Std.	" \
                   "Altitude Ellipsoid	Altitude Std.	Roll	Roll Std.	Pitch	Pitch Std.	Yaw	Yaw Std.	" \
                   "East Velocity	East Velocity Std.	North Velocity	North Velocity Std.	Down Velocity	" \
                   "Down Velocity Std.	X Velocity	Y Velocity	Z Velocity	Delta Angle X	Delta Angle Y	" \
                   "Delta Angle Z	Heave	Delayed Heave"

    var_qin_opt1 = "utc_date_ymd", "utc_t_hms", "utc_tow_s", "lon_dd", "east_sd", "lat_dd",\
                   "north_sd", "eht", "eht_sd", "roll_dd", "roll_sd", "pit_dd", "pitch_sd", "yaw",\
                   "yaw_sd", "east_vel", "east_vel_sd", "north_vel", "north_vel_sd", "down_vel",\
                   "down_vel_sd", "x_vel", "y_vel", "z_vel", "x_delta_ang", "y_delta_ang", \
                   "z_delta_ang", "heave", "d_heave"

    # hdr_qin_opt2 = " "
    #
    # var_qin_opt2 = " "

    hdr_pos_opt1 = "UTC_TOW_s	Distance	Easting (m)	sd-east (m)	Northing (m)	sd-north (m)	Ell-Hgt (m)	" \
                   "sd-ehgt (m)	Geoid Sep (m)	Ortho Hgt (m)	Roll (deg)	sd-roll (deg)	Pitch (deg)	" \
                   "sd-pitch (deg)	Heading (deg)	sd-head (deg)	East-vel (m/s)	sd-east_ve (m/s)l	" \
                   "North-vel (m/s)	sd-north_vel (m/s)	Up-vel (m/s)	sd-up_vel (m/s)	X-body_acc	Y-body_acc	" \
                   "Z-body_acc	X-body_ang_rate	Y-body_ang_rate	Z-body_ang_rate"

    var_pos_opt1 = "utc_tow_s", "dist", "east", "east_sd", "north", "north_sd", "eht",\
                   "eht_sd", "geoid_sep", "ortho_ht", "roll_dd", "roll_sd", "pit_dd", \
                   "pit_sd", "hdg_dd", "hdg_sd", "east_vel", "east_vel_sd", \
                   "north_vel", "north_vel_sd", "up_vel", "up_vel_sd", "x_body_acc", "y_body_acc", \
                   "z_body_acc", "x_body_ang_rate", "y_body_ang_rate", "z_body_ang_rate"

    hdr_pos_opt2 = "UTC_Date_Time	UTC_TOW_s	Easting (m)	sd-east (m)	Northing (m)	sd-north (m)	Ell-Hgt (m)	" \
                   "sd-ehgt (m)	Geoid Sep (m)	Ortho Hgt (m)	Roll (deg)	sd-roll (deg)	Pitch (deg)	" \
                   "sd-pitch (deg)	Heading (deg)	sd-head (deg)	East-vel (m/s)	sd-east_ve (m/s)l	" \
                   "North-vel (m/s)	sd-north_vel (m/s)	Up-vel (m/s)	sd-up_vel (m/s)	X-body_acc	Y-body_acc	" \
                   "Z-body_acc	X-body_ang_rate	Y-body_ang_rate	Z-body_ang_rate"

    var_pos_opt2 = "ddd", "mmm", "dd", "utc_t", "yyy", "utc_tow_s", "east", "east_sd", "north", "north_sd", "eht", \
                   "eht_sd", "geoid_sep", "ortho_ht", "roll_dd", "roll_sd", "pit_dd", "pit_sd", "hdg_dd", "hdg_sd",\
                   "east_vel", "east_vel_sd", "north_vel", "north_vel_sd", "up_vel", "up_vel_sd", "x_body_acc", \
                   "y_body_acc", "z_body_acc", "x_body_ang_rate", "y_body_ang_rate", "z_body_ang_rate"

    hdr_pos_opt3 = "UTC_Date_Time	UTC_TOW_s	Lon_dd	sd-east (m)	Lat_dd	sd-north (m)	Ell-Hgt (m)	sd-ehgt (m)	" \
                   "Geoid Sep (m)	Ortho Hgt (m)	Roll (deg)	sd-roll (deg)	Pitch (deg)	sd-pitch (deg)	" \
                   "Heading (deg)	sd-head (deg)	East-vel (m/s)	sd-east_ve (m/s)l	North-vel (m/s)	" \
                   "sd-north_vel (m/s)	Up-vel (m/s)	sd-up_vel (m/s)	X-body_acc	Y-body_acc	Z-body_acc	" \
                   "X-body_ang_rate	Y-body_ang_rate	Z-body_ang_rate"

    var_pos_opt3 = "ddd", "mmm", "dd", "yyy", "utc_am_pm", "am_pm", "utc_tow_s",\
                   "lon_dd", "east_sd", "lat_dd", "north_sd", "eht", "eht_sd", \
                   "geoid_sep", "ortho_ht", "roll_dd", "roll_sd", "pit_dd", "pit_sd", \
                   "hdg_dd", "hdg_sd", "east_vel", "east_vel_sd", "north_vel", \
                   "north_vel_sd", "up_vel", "up_vel_sd", "x_body_acc", "y_body_acc", "z_body_acc",\
                   "x_body_ang_rate", "y_body_ang_rate", "z_body_ang_rate"

    # hdr_kin_opt1 = " "
    #
    # var_kin_opt1 = " "
    #
    # hdr_csr_opt1 = " "
    #
    # var_csr_opt1 = " "
    #
    # hdr_gra_opt1 = " "
    #
    # var_gra_opt1 = " "
    #
    # hdr_gra_opt2 = " "
    #
    # var_gra_opt2 = " "

    # Identifies SBET ASCIIs and converts that "Pandas" data structure
    line_num = 0
    with open(f_path, 'r') as f_obj:
        file_name = os.path.split(f_path)[1]
        found = False
        while not found:
            for line_content in f_obj:
                line_num += 1
                if hdr_qin_opt1 in line_content:
                    found = True
                    data_start_n = line_num + 2
                    imu_str_data = file_2_pan(f_path, data_start_n, var_qin_opt1)
                    utc_tow_s = imu_str_data.utc_tow_s
                    str_date = imu_str_data.utc_date_ymd[0]
                    yy = str_date[:4]
                    mm = str_date[5:7]
                    n_day = str_date[8:]
                    cv_date_time = tow_sec_2_hms(int(yy), int(mm), int(n_day), utc_tow_s.array)
                    imu_str_data = pd.concat([cv_date_time, imu_str_data], axis=1)
                    break
                elif hdr_pos_opt1 in line_content:
                    found = True
                    data_start_n = line_num + 1
                    imu_str_data = file_2_pan(f_path, data_start_n, var_pos_opt1)
                    break
                elif hdr_pos_opt2 in line_content:
                    found = True
                    data_start_n = line_num + 1
                    imu_str_data = file_2_pan(f_path, data_start_n, var_pos_opt2)
                    utc_tow_s = imu_str_data.utc_tow_s
                    yy = str(imu_str_data.yyy[0])
                    month_name = imu_str_data.mmm[0]
                    mm = month_nam2_num(month_name)
                    n_day = imu_str_data.dd[0]
                    cv_date_time = tow_sec_2_hms(int(yy), int(mm), int(n_day), utc_tow_s.array)
                    imu_str_data = pd.concat([cv_date_time, imu_str_data], axis=1)
                    break
                elif hdr_pos_opt3 in line_content:
                    found = True
                    data_start_n = line_num + 1
                    imu_str_data = file_2_pan(f_path, data_start_n, var_pos_opt3)
                    utc_tow_s = imu_str_data.utc_tow_s
                    yy = str(imu_str_data.yyy[0])
                    month_name = imu_str_data.mmm[0]
                    mm = month_nam2_num(month_name)
                    n_day = imu_str_data.dd[0]
                    n_day = int(n_day.replace(",", ""))
                    cv_date_time = tow_sec_2_hms(int(yy), int(mm), int(n_day), utc_tow_s.array)
                    imu_str_data = pd.concat([cv_date_time, imu_str_data], axis=1)
                    break
                else:
                    print("Searching for a valid header")
                    if line_num > 51:
                        print('File name:', file_name, '--- ', 'I did not find a valid header in the first ',
                              line_num, "lines")
                        break
        print('File name:', file_name, '---', 'Found valid export-template header on line', line_num)
    return imu_str_data


def file_2_pan(f_path, data_start_n, var_name):
    with open(f_path, 'r') as file_obj:
        imu_str_data = pd.read_csv(file_obj, header=data_start_n, delim_whitespace=True)
        imu_str_data.columns = list(var_name)
    return imu_str_data


def month_nam2_num(month_name):
    dto = datetime.strptime(month_name, "%b")
    month_num = dto.month
    return month_num


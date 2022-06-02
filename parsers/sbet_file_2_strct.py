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

    var_pos_opt1 = "utc_tow_s", "cum_dist", "east", "east_sd", "north", "north_sd", "eht",\
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

    hdr_pos_opt4 = "UTC_TOW_s	Distance	Lon_dd	sdeast_m	Lat_dd	sdnorth_m	Elht_m	sdElht	GeoidSep_m	" \
                   "Ortht_m	Roll_deg	sdRoll_deg	Pitch_deg	sdPitch_deg	sdPitch_deg	sdHead_deg	EastVel_mps	" \
                   "sdEastvel_mps	NorthVel_mps	sdNorthVel_mps	UpVel_mps	sdUpVel	XBodyAcc_mps2	" \
                   "YBodyAcc_mps2	ZBodyAcc_mps2	XBodyAngR_mps2	YBodyAngR_mps2	ZBodyAngR_mps2"

    var_pos_opt4 = "utc_tow_s", "cum_dist", "lon_dd", "east_sd", "lat_dd", "north_sd", "eht", "eht_sd", "geoid_sep", \
                   "ortho_ht", "roll_dd", "roll_sd", "pit_dd", "pit_sd", "hdg_dd", "hdg_sd", "east_vel", \
                   "east_vel_sd", "north_vel", "north_vel_sd", "up_vel", "up_vel_sd", "x_body_acc", \
                   "y_body_acc", "z_body_acc", "x_body_ang_rate", "y_body_ang_rate", "z_body_ang_rate"

    hdr_pos_opt5 = "UTCTime1	UTC_Time	Lon_deg	sdeast_m	Lat_deg	sdnorth_m	Elht_m	sdElht	GeoidSep_m	" \
                   "Ortht_m	Roll_deg	sdRoll_deg	Pitch_deg	sdPitch_deg	sdPitch_deg	sdHead_deg	EastVel_mps	" \
                   "sdEastvel_mps	NorthVel_mps	sdNorthVel_mps	UpVel_mps	sdUpVel	XBodyAcc_mps2	" \
                   "YBodyAcc_mps2	ZBodyAcc_mps2	XBodyAngR_mps2	YBodyAngR_mps2	ZBodyAngR_mps2"

    """
    var_pos_opt5 = "Note that hdr_pos_opt5 is the same as hdr_pos_opt4. Instead of creating new column names for 
        var_pos_opt5, we simply equate var_pos_opt5 = var_pos_opt4.
    """
    var_pos_opt5 = var_pos_opt4

    hdr_pos_opt6 = "UTC Time of Week	Distance	Easting (m)	sd-east (m)	Northing (m)	sd-north (m)	" \
                   "Ell-Hgt (m)	sd-ehgt (m)	Geoid Sep (m)	Ortho Hgt (m)	Roll (deg)	sd-roll (deg)	Pitch (deg)	" \
                   "sd-pitch (deg)	Heading (deg)	sd-head (deg)	East-vel (m/s)	sd-east_ve (m/s)l	" \
                   "North-vel (m/s)	sd-north_vel (m/s)	Up-vel (m/s)	sd-up_vel (m/s)	" \
                   "X-body_acc	Y-body_acc	Z-body_acc	X-body_ang_rate	Y-body_ang_rate	Z-body_ang_rate"

    var_pos_opt6 = var_pos_opt1

    # POS RTK
    hdr_pos_opt7 = "id,length,version,utc_seconds,utc_nanos,status,latitude,longitude,height,roll,pitch,heading,heave,"\
                   "roll_rate,pitch_rate,yaw_rate,north_vel,east_vel,down_vel,latitude_error,longitude_error," \
                   "height_error,roll_error,pitch_error,heading_error,heave_error,north_acceleration," \
                   "east_acceleration,down_acceleration,delayed_seconds,delayed_nanos,delayed_heave,utc_time"

    var_pos_opt7 = "id", "sys_name", "ver", "utc_tow_int_s", "utc_tow_int_ns", "status", "lat_dd", "lon_dd", "eht", \
                   "roll_dd", "pit_dd", "hdg_dd", "heave", "roll_rate", "pitch_rate", "yaw_rate", "north_vel", \
                   "east_vel", "down_vel", "north_sd", "east_sd", "hdg_sd", "roll_sd", "pit_sd", "heading_sd", \
                   "heave_sd", "north_acc", "east_acc", "down_acc", "del_heave_ts", "del_heave_tns", \
                   "del_heave", "utc_tow_s"

    # hdr_pos_opt8 =
    #
    # var_pos_opt8 =
    #
    hdr_kin_opt1 = "Human Timestamp,Unix Time,Microseconds,Fix Type,Latitude,Longitude,Height,Latitude SD," \
                   "Longitude SD,Height SD,Velocity North,Velocity East,Velocity Down,Velocity North SD," \
                   "Velocity East SD,Velocity Down SD,Roll,Pitch,Heading,Roll SD,Pitch SD,Heading SD," \
                   "Accelerometer Bias X,Accelerometer Bias Y,Accelerometer Bias Z,Accelerometer Bias X SD," \
                   "Accelerometer Bias Y SD,Accelerometer Bias Z SD,Gyroscope Bias X,Gyroscope Bias Y," \
                   "Gyroscope Bias Z,Gyroscope Bias X SD,Gyroscope Bias Y SD,Gyroscope Bias Z SD," \
                   "GPS Satellites,GLONASS Satellites,BeiDou Satellites,Galileo Satellites," \
                   "Differential GPS Satellites,Differential Glonass Satellites,Differential BeiDou Satellites," \
                   "Differential Galileo Satellites,Dual Antenna Fix,Horizontal Separation,Vertical Separation," \
                   "SBAS Satellites,Differential SBAS Satellites,Zero Velocity Update,Base to Rover North," \
                   "Base to Rover East,Base to Rover Down,Base to Rover North SD,Base to Rover East SD," \
                   "Base to Rover Down SD,Moving Base Fix Type,Event 1 Flag,Event 2 Flag"

    # in var_kin_opt1, [x_body_acc, y_body_acc, z_body_acc], z_body_acc replaces [x_acc_bia, y_acc_bia, z_acc_bia]
    # Likewise, [x_body_ang_rate, y_body_ang_rate, z_body_ang_rate], replaces [x_gyr_bia, y_gyr_bia, z_gyr_bia]
    var_kin_opt1 = "cvil_t_cst", "unix_t_s", "unix_t_ms", "fix_typ", "lat_dd", "lon_dd", "eht", "north_sd",\
                   "east_sd", "eht_sd", "north_vel", "east_vel", "up_vel", "north_vel_sd", "east_vel_sd",\
                   "up_vel_sd", "roll_dd", "pit_dd", "hdg_dd", "roll_sd", "pit_sd", "hdg_sd", "x_body_acc",\
                   "y_body_acc", "z_body_acc", "x_acc_bia_sd", "y_acc_bia_sd", "z_acc_bia_sd", "x_body_ang_rate",\
                   "y_body_ang_rate", "z_body_ang_rate", "x_gyr_bia_sd", "y_gyr_bia_sd", "z_gyr_bia_sd", "nGPS", \
                   "nGLO", "nBDS", "nGAL", "dGPS", "dGLO", "dBDS", "dGAL", "dual_ant_fix", "hz_sep", "vert_sep", \
                   "nSBAS", "dSBAS", "zero_vel_update", "bl2rov_north", "bl2rov_east", "bl2rov_down", \
                   "bl2rov_north_sd", "bl2rov_east_sd", "bl2rov_down_sd", "mov_base_fix", "ev1_flag", "ev2_flag"

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
    #
    # hdr_gpx_opt2 = " "
    #
    # var_gpx_opt2 = " "

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
                elif hdr_pos_opt4 in line_content:
                    found = True
                    data_start_n = line_num + 1
                    imu_str_data = file_2_pan(f_path, data_start_n, var_pos_opt4)
                    break
                elif hdr_pos_opt5 in line_content:
                    found = True
                    data_start_n = line_num + 1
                    imu_str_data = file_2_pan(f_path, data_start_n, var_pos_opt5)
                    break
                elif hdr_pos_opt6 in line_content:
                    found = True
                    data_start_n = line_num + 1
                    imu_str_data = file_2_pan(f_path, data_start_n, var_pos_opt6)
                    break
                elif hdr_pos_opt7 in line_content:
                    found = True
                    data_start_n = line_num + 1
                    imu_str_data = fileCSV_2_pan(f_path, data_start_n, var_pos_opt7)
                    break
                # elif hdr_pos_opt8 in line_content:
                #     found = True
                #     data_start_n = line_num + 1
                #     imu_str_data = file_2_pan(f_path, data_start_n, var_pos_opt8)
                #     break
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


def fileCSV_2_pan(f_path, data_start_n, var_name):
    with open(f_path, 'r') as file_obj:
        imu_str_data = pd.read_csv(file_obj, header=data_start_n, delimiter=",")
        imu_str_data.columns = list(var_name)
    return imu_str_data


def month_nam2_num(month_name):
    dto = datetime.strptime(month_name, "%b")
    month_num = dto.month
    return month_num

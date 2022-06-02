# Modified by:
# Johnson O. Oguntuase's Matlab & Python library
# Geo plu Bathy (GpB) Lab
# University of Southern Mississippi
# Geodesy functions
# History:
# 2022-05-20


import math as ma
import struct
import time


# %%

sbet_hdr = "utc_tow_s", "lat_dd", "lon_dd", "eht", "north_vel", "east_vel", "up_vel", "roll_dd", "pit_dd", "hdg_dd", \
           "x_body_acc", "y_body_acc", "z_body_acc", "x_body_ang_rate", "y_body_ang_rate", "z_body_ang_rate"

sbet_rms_hdr = "north_sd", "east_sd", "eht_sd", "north_vel_sd", "east_vel_sd", "up_vel_sd", \
               "roll_sd", "pit_dd", "hdg_sd"

def pos_ascii_2_sbet(sbet_df):
    # converts ASCII SBET to binary SBET format
    pro_sta_tim = time.process_time()
    print(pro_sta_tim, ": Sbet encoder starts")
    print("....... Expecting lat/lon and all angles in degrees .......")
    print("....... Writing sbet and rms files ........................")
    print("....... Please wait .......................................")
    sbet_file = open("GpB_sbet.out", 'wb')
    rms_file = open("GpB_smrmsg.out", 'wb')
    for ii in range(sbet_df.__len__()):
        sbet_file.write(
            struct.pack('17d',
                        sbet_df.utc_tow_s[ii],
                        ma.radians(sbet_df.lat_dd[ii]),
                        ma.radians(sbet_df.lon_dd[ii]),
                        sbet_df.eht[ii],
                        sbet_df.north_vel[ii],
                        sbet_df.east_vel[ii],
                        sbet_df.up_vel[ii],
                        ma.radians(sbet_df.roll_dd[ii]),
                        ma.radians(sbet_df.pit_dd[ii]),
                        ma.radians(sbet_df.hdg_dd[ii]),
                        0,
                        sbet_df.x_body_acc[ii],
                        sbet_df.y_body_acc[ii],
                        sbet_df.z_body_acc[ii],
                        ma.radians(sbet_df.x_body_ang_rate[ii]),
                        ma.radians(sbet_df.y_body_ang_rate[ii]),
                        ma.radians(sbet_df.z_body_ang_rate[ii]))
        )
        rms_file.write(
            struct.pack('10d',
                        sbet_df.utc_tow_s[ii],
                        sbet_df.north_sd[ii],
                        sbet_df.east_sd[ii],
                        sbet_df.eht_sd[ii],
                        sbet_df.north_vel_sd[ii],
                        sbet_df.east_vel_sd[ii],
                        sbet_df.up_vel_sd[ii],
                        ma.radians(sbet_df.roll_sd[ii]),
                        ma.radians(sbet_df.pit_sd[ii]),
                        ma.radians(sbet_df.hdg_sd[ii]))
        )
    sbet_file.close()
    rms_file.close()
    pro_sto_tim = time.process_time()
    print(pro_sto_tim, ": Sbet encoder ends")
    print(pro_sto_tim - pro_sta_tim, "Sbet encoding duration")
    print("done!")


def sbet_int_chk(sbet_df):
    if set(sbet_df.columns) & set(sbet_hdr + sbet_rms_hdr) == set(sbet_hdr + sbet_rms_hdr):
        print("sbet data frame has all required columns to write binary sbet file")
    else:
        print("sbet data frame is invalid, please modify")
        print("")
        print("available columns are:", sorted(set(sbet_df.columns) & set(sbet_hdr + sbet_rms_hdr)))
        print("")
        print("Sbet writer requires 27 parameters: ", sorted(set(sbet_hdr + sbet_rms_hdr)))

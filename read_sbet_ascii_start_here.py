"""
Johnson O. Oguntuase's Matlab function library
Geo plu Bathy (GpB) Lab
University of Southern Mississippi
Geodesy functions
History:
2022/05/07
2019/11/09
"""

"""
Dec IMU project:
Dec 2021, IMU Project
Qinertia data path
"""
# %%
from parsers.sbet_file_2_strct import *
from parsers.ascii2sbet import *

test_proj_dir = r"G:/____TECHNICAL/___USM_COLLABORATION_PROJECTS/___2021_Dec_IMU_Projects/___202112_IMU_Projects_Results" \
           r"/Testdata/"


# %%
"""
When reading POS_File_Type_1 (hdr_pos_opt1), for a file containing tow in seconds only,
use “tow_sec_2_hms(yy, mm, dd, tow)” function to convert to wall-clock-like time format; 
where “yy”, “mm”, and “dd” are integers, and tow is an array.
Note that dd is a nominal day of month, and it can be any day within the week the data was collected.

That is better explained by walking through an example. First generate GPS calendar from 
Johnson's geodesy library by calling “gps_calendar(sta='2021-12-01', sto='2021-12-31').”
Assuming the observation date was 2021-12-13 Monday; ideally, dd should be 13. 
Calling tow_sec_2_hms(2021, 12, 13, tow) will return full dates and time in pandas datetime object. 

However, you can safely pass dd=14, dd=15, dd=16 and the time and date will still be accurate as day 13. 
For instance tow_sec_2_hms(2021, 12, 15, [146092.82]) will return 2021-12-13 16:34:52.820.
Any number representing any day within the week the data was collected will return accurate result. 
Note, however, that using a day outside the week will move date-time representation to the chosen week accordingly.
"""

# %% To see all columns, type "imu_data.column"
# data_file = "SBG_test_data.txt"
# file_path = proj_dir + data_file
# sbg_data = file_2_strct(file_path)
# print("")
# print("imu_data columns:", sbg_data.columns)

# %%
# data_file = "POS_ENH_UTC_TOWs_Type1.txt"
# file_path = proj_dir + data_file
# pos1_data = file_2_strct(file_path)

# %%
# data_file = "POS_ENH_UTC_DnT_TOWs_Type2.txt"
# file_path = proj_dir + data_file
# pos2_data = file_2_strct(file_path)

# %%
data_file = "POS_LonLat_UTC_DTT_Type3.txt"
file_path = test_proj_dir + data_file
pos3_data = file_2_strct(file_path)
print(pos3_data.columns)

# Generate SBET and RMS files
sbet_int_chk(pos3_data) # check SBET writing integrity before binary encoding
pos_ascii_2_sbet(pos3_data)
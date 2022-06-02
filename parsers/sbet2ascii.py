# Original code from Kurt Schwehr
#
# Modified by:
# Johnson O. Oguntuase's Matlab & Python library
# Geo plu Bathy (GpB) Lab
# University of Southern Mississippi
# Geodesy functions
# History:
# 2022-05-19

import math
import mmap
import os
import struct

import pandas as pd

datagram_size = 136  # 17 parameters x 8 bytes

field_names = ('time', 'latitude', 'longitude', 'altitude', 'x_vel', 'y_vel', 'z_vel', 'roll', 'pitch',
               'platform_heading', 'wander_angle', 'x_acceleration', 'y_acceleration', 'z_acceleration',
               'x_angular_rate', 'y_angular_rate', 'z_angular_rate')

var_sbt_out = "utc_tow_s", "lat_dd", "lon_dd", "eht", "x_vel", "y_vel", "z_vel", "roll_dd", "pit_dd", \
              "hdg_dd", "wander_angle", "x_body_acc", "y_body_acc", "z_body_acc", "x_body_ang_rate", \
              "y_body_ang_rate", "z_body_ang_rate"


def get_offset(datagram_index):
    return datagram_index * datagram_size


class Sbet(object):
    def __init__(self, filename, use_mmap=True):

        sbet_file = open(filename)

        if use_mmap:
            sbet_size = os.path.getsize(filename)
            self.data = mmap.mmap(sbet_file.fileno(), sbet_size, access=mmap.ACCESS_READ)
        else:
            self.data = sbet_file.read()

        # Make sure the file is sane
        assert (len(self.data) % datagram_size == 0)

        self.num_datagrams = len(self.data) / datagram_size

    def decode(self, offset=0):
        """Return a dictionary for an SBet datagram starting at offset"""

        subset = self.data[offset: offset + datagram_size]
        values = struct.unpack('17d', subset)

        sbet_values = dict(zip(field_names, values))

        sbet_values['lat_deg'] = math.degrees(sbet_values['latitude'])
        sbet_values['lon_deg'] = math.degrees(sbet_values['longitude'])
        sbet_values['roll_deg'] = math.degrees(sbet_values['roll'])
        sbet_values['pitch_deg'] = math.degrees(sbet_values['pitch'])
        sbet_values['plat_hdg_deg'] = math.degrees(sbet_values['platform_heading'])
        sbet_values['wander_angle_deg'] = math.degrees(sbet_values['wander_angle'])
        sbet_values['x_angular_rate_deg'] = math.degrees(sbet_values['x_angular_rate'])
        sbet_values['y_angular_rate_deg'] = math.degrees(sbet_values['y_angular_rate'])
        sbet_values['z_angular_rate_deg'] = math.degrees(sbet_values['z_angular_rate'])

        return sbet_values

    def get_datagram(self, datagram_index):
        offset = get_offset(datagram_index)
        values = self.decode(offset)
        return values

    def __iter__(self):
        return SbetIterator(self)


class SbetIterator(object):
    """Independent iterator class for Sbet files"""

    def __init__(self, sbet):
        self.sbet = sbet
        self.iter_position = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.iter_position >= self.sbet.num_datagrams:
            raise StopIteration

        values = self.sbet.get_datagram(self.iter_position)
        self.iter_position += 1
        return values


def sbet_parser_main(sbet_file_name):
    print('Datagram Number, Time, x, y')
    sbo = Sbet(sbet_file_name)
    dat_len = sbo.num_datagrams

    utc_tow_s = []
    lat_dd = []
    lon_dd = []
    eht = []
    x_vel = []
    y_vel = []
    z_vel = []
    roll_dd = []
    pit_dd = []
    hdg_dd = []
    wander_angle = []
    x_body_acc = []
    y_body_acc = []
    z_body_acc = []
    x_body_ang_rate = []
    y_body_ang_rate = []
    z_body_ang_rate = []

    sbet_file_name = sbet_file_name + "_ascii.txt"
    print('First 10 outputs on screen.......')
    print(var_sbt_out)
    print("")
    with open(sbet_file_name, 'w') as sbo_ascii:
        fmt = 17 * "%.11f,"
        fmt = "%d," + fmt.strip(",") + "\n"
        for index, datagram in enumerate(sbo):
            parameter_output = (index, datagram['time'], datagram['lon_deg'], datagram['lat_deg'], datagram['altitude'],
                                datagram['x_vel'], datagram['y_vel'], datagram['z_vel'], datagram['roll_deg'],
                                datagram['pitch_deg'],
                                datagram['plat_hdg_deg'], datagram['wander_angle_deg'], datagram['x_acceleration'],
                                datagram['y_acceleration'], datagram['z_acceleration'], datagram['x_angular_rate'],
                                datagram['y_angular_rate'], datagram['z_angular_rate'])

            # Printing snippet to screen
            if index < 10:
                print(fmt % parameter_output)

            sbo_ascii.write(fmt % parameter_output)

            utc_tow_s.append(datagram['time'])
            lat_dd.append(datagram['lat_deg'])
            lon_dd.append(datagram['lon_deg'])
            eht.append(datagram['altitude'])
            x_vel.append(datagram['x_vel'])
            y_vel.append(datagram['y_vel'])
            z_vel.append(datagram['z_vel'])
            roll_dd.append(datagram['roll_deg'])
            pit_dd.append(datagram['pitch_deg'])
            hdg_dd.append(datagram['plat_hdg_deg'])
            wander_angle.append(datagram['wander_angle_deg'])
            x_body_acc.append(datagram['x_acceleration'])
            y_body_acc.append(datagram['y_acceleration'])
            z_body_acc.append(datagram['z_acceleration'])
            x_body_ang_rate.append(datagram['x_angular_rate'])
            y_body_ang_rate.append(datagram['y_angular_rate'])
            z_body_ang_rate.append(datagram['z_angular_rate'])

        sbet_df = pd.DataFrame(
            {"utc_tow_s": utc_tow_s,
             "lat_dd": lat_dd,
             "lon_dd": lon_dd,
             "eht": eht,
             "x_vel": x_vel,
             "y_vel": y_vel,
             "z_vel": z_vel,
             "roll_dd": roll_dd,
             "pit_dd": pit_dd,
             "hdg_dd": hdg_dd,
             "wander_angle": wander_angle,
             "x_body_acc": x_body_acc,
             "y_body_acc": y_body_acc,
             "z_body_acc": z_body_acc,
             "x_body_ang_rate": x_body_ang_rate,
             "y_body_ang_rate": y_body_ang_rate,
             "z_body_ang_rate": z_body_ang_rate
             },
        )

    print("done!")
    return sbet_df, dat_len

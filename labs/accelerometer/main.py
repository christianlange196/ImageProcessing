from machine import Pin, I2C
import utime

# Define the I2C communication
i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=400000)

# MPU6050 I2C address
MPU6050_I2C_ADDRESS = 0x68

# MPU6050 Registers
POWER_MANAGEMENT_1 = 0x6B
ACCEL_XOUT_H = 0x3B
GYRO_XOUT_H = 0x43

def mpu6050_init():
    # Wake up the MPU6050
    i2c.writeto_mem(MPU6050_I2C_ADDRESS, POWER_MANAGEMENT_1, bytearray([0]))

def read_acceleration():
    accel_x = i2c.readfrom_mem(MPU6050_I2C_ADDRESS, ACCEL_XOUT_H, 2)
    accel_y = i2c.readfrom_mem(MPU6050_I2C_ADDRESS, ACCEL_XOUT_H + 2, 2)
    accel_z = i2c.readfrom_mem(MPU6050_I2C_ADDRESS, ACCEL_XOUT_H + 4, 2)
    x = int.from_bytes(accel_x, 'big') if accel_x[0] < 128 else int.from_bytes(accel_x, 'big') - 65536
    y = int.from_bytes(accel_y, 'big') if accel_y[0] < 128 else int.from_bytes(accel_y, 'big') - 65536
    z = int.from_bytes(accel_z, 'big') if accel_z[0] < 128 else int.from_bytes(accel_z, 'big') - 65536
    return x, y, z

def read_gyroscope():
    gyro_x = i2c.readfrom_mem(MPU6050_I2C_ADDRESS, GYRO_XOUT_H, 2)
    gyro_y = i2c.readfrom_mem(MPU6050_I2C_ADDRESS, GYRO_XOUT_H + 2, 2)
    gyro_z = i2c.readfrom_mem(MPU6050_I2C_ADDRESS, GYRO_XOUT_H + 4, 2)
    x = int.from_bytes(gyro_x, 'big') if gyro_x[0] < 128 else int.from_bytes(gyro_x, 'big') - 65536
    y = int.from_bytes(gyro_y, 'big') if gyro_y[0] < 128 else int.from_bytes(gyro_y, 'big') - 65536
    z = int.from_bytes(gyro_z, 'big') if gyro_z[0] < 128 else int.from_bytes(gyro_z, 'big') - 65536
    return x, y, z

mpu6050_init()

while True:
    accel_x, accel_y, accel_z = read_acceleration()
    gyro_x, gyro_y, gyro_z = read_gyroscope()
    print(accel_x, accel_y, accel_z, gyro_x, gyro_y, gyro_z)
    # utime.sleep(1)

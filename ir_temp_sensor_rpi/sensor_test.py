from email.headerregistry import Address
import board 
import busio as io
import adafruit_mlx90614

from time import sleep


if __name__ == "__main__":
    
    i2c = io.I2C(board.SCL, board.SDA, frequency=800000)

    # ADDRESS = 0x55a    

    mlx = adafruit_mlx90614.MLX90614(i2c)

    while True:
        ambient_temp = "{:.2f}".format(mlx.ambient_temperature)
        target_temp = "{:.2f}".format(mlx.object_temperature)

        sleep(5)

        print(f"Ambient Temp: {ambient_temp} C")
        print(f"Object Temp: {target_temp} C")
        
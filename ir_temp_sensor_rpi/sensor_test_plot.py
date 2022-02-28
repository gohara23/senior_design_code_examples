import board 
import busio as io
import adafruit_mlx90614
import matplotlib
import matplotlib.pyplot as plt
from time import time
from time import sleep


if __name__ == "__main__":
    
    i2c = io.I2C(board.SCL, board.SDA, frequency=800000)

    mlx = adafruit_mlx90614.MLX90614(i2c)

    t_0 = time()
    tvec = []
    data = []
    matplotlib.use("TkAgg")
    plt.style.use("classic")

    while True:
        ambient_temp = "{:.2f}".format(mlx.ambient_temperature)
        target_temp = "{:.2f}".format(mlx.object_temperature)
        tvec.append(time()-t_0)
        data.append(target_temp)
        # plt.plot(tvec, data, '-b', label="IR Target", scaley=False)
        # plt.xlabel("Time [s]")
        # plt.ylabel("Temp (c)")
        # plt.ylim(0,50)
        
        plt.scatter(time()-t_0, target_temp, c='black', s=10, marker='x')
        
        plt.pause(0.05)

        print(f"Ambient Temp: {ambient_temp} C")
        print(f"Object Temp: {target_temp} C")
        
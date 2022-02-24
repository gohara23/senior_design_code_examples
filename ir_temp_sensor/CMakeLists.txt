# Generated Cmake Pico project file

cmake_minimum_required(VERSION 3.13)

set(CMAKE_C_STANDARD 11)
set(CMAKE_CXX_STANDARD 17)

# Initialise pico_sdk from installed location
# (note this can come from environment, CMake cache etc)
set(PICO_SDK_PATH "/home/gohara/Downloads/pico/pico-sdk")

# Pull in Raspberry Pi Pico SDK (must be before project)
include(pico_sdk_import.cmake)

project(ir_temp_sensor C CXX ASM)

# Initialise the Raspberry Pi Pico SDK
pico_sdk_init()

# Add executable. Default name is the project name, version 0.1

add_executable(ir_temp_sensor ir_temp_sensor.c )

pico_set_program_name(ir_temp_sensor "ir_temp_sensor")
pico_set_program_version(ir_temp_sensor "0.1")

pico_enable_stdio_uart(ir_temp_sensor 1)
pico_enable_stdio_usb(ir_temp_sensor 1)

# Add the standard library to the build
target_link_libraries(ir_temp_sensor pico_stdlib)

# Add any user requested libraries
target_link_libraries(ir_temp_sensor
        hardware_i2c
        )

pico_add_extra_outputs(ir_temp_sensor)


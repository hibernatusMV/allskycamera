# Allsky Camera

## Hardware
- Raspberry Pi 3B+
- LED Red
- LED Green
- Temperature sensor DS 18B20
- Relais EIN Kanal Relaismodul Bord Schild Für PIC AVR DSP ARM https://amzn.to/2vrqiVI

## Wiring
**_Power LED_**

| RasPi Pin     | Pin        | LED       |
| ------------- |------------|:---------:|
| 1             | 3.3V       | (+)       |
| 6             | GND        | (-)       |

**_Activity LED_**
| RasPi Pin     | Pin        | LED       |
| ------------- |------------|:---------:|
| 38            | GPIO20     | (+)       |
| 39            | GND        | (-)       |


**_Heater Switch Relay_**
| RasPi Pin     | Relay      |                 |
| ------------- |------------|-----------------|
| 2             | (+)        |                 |
| 4             | IN         | Relay input     |
| 9             | COM        | Resistors (GND) |
| 11            | S          | Signal          |
| 14            | (-)        | GND             |

**_Temperature Sensor_**
| RasPi Pin     | DS18B20    |
| ------------- |------------|
| 7             | Data       |
| 17            | 3.3V       |
| 21            | GND        |

**_Raspberry Pi 3 B+ Pinout_**
![RaspPi3B_Pinout](https://github.com/hibernatusMV/allskycamera/blob/master/raspberrypi_pinout.png "Raspberry Pi 3 B+ Pinout")


## Raspberry Pi Environment
**_Shell scripts and cronjobs_**
1. in home directory /home/pi/ create directories bin and log
```
mkdir bin
mkdir python
mkdir log
```
2. copy shell scripts to the bin directory
3. copy python scripts and subfolder to the python directory
4. edit crontab ``` crontab -e ```
5. add cronjob ``` */1 * * * * /home/pi/bin/tempGuard.sh >>/home/pi/log/$(date +\%Y\%m\%d)_tempGuard.log 2>&1 ```

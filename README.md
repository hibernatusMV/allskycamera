# Allsky Camera

## Hardware
..Raspberry Pi 3B+
..LED Red
..LED Green
..Temperature sensor DS 18B20
..Relais EIN Kanal Relaismodul Bord Schild Für PIC AVR DSP ARM https://amzn.to/2vrqiVI

## Wiring
**_Power LED_**

| RasPi Pin     | Pin        | LED       |
| ------------- |------------|:---------:|
| 1             | 3.3V       | (+)       |
| 6             | GND        | (-)       |

**_Activity LED_**
| RasPi Pin     | Pin        | LED       
| ------------- |------------|:---------:|
| 38            | GPIO20     | (+)       |
| 39            | GND        | (-)       |

**_Raspberry Pi 3 B+ Pinout_**
![RaspPi3B_Pinout](https://github.com/hibernatusMV/allskycamera/blob/master/raspberrypi_pinout.png "Raspberry Pi 3 B+ Pinout")


## Raspberry Pi Environment
1. in home directory /home/pi/ create directories bin and log
```
mkdir bin
mkdir log
```
2. copy shell scripts to bin directory
3. edit crontab ``` crontab -e ```
4. add cronjob ``` */1 * * * * /home/pi/bin/tempGuard.sh >>/home/pi/log/$(date +\%Y\%m\%d)_tempGuard.log 2>&1 ```

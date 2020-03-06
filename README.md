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
1. create two new folder named bin and log in /home/pi/
```bash
mkdir bin
mkdir log
```
2. copy shell scripts to the bin directory
3. edit crontab ``` crontab -e ```
4. add cronjob ``` */1 * * * * /home/pi/bin/tempGuard.sh >>/home/pi/log/$(date +\%Y\%m\%d)_tempGuard.log 2>&1 ```

**_Installing Telegramm and Telegramm Bot_**

1. Follow the link to setup a Telegramm bot :
[Using Telegram Bot with Raspberry Pi](https://circuitdigest.com/microcontroller-projects/raspberry-pi-telegram-bot) until Step 4.

2. Install telebot to communicate with Telegramm.

```bash
sudo apt-get install python-pip
sudo pip install telepot
```

3. Create a new folder named python in /home/pi/:

```bash
mkdir python
```

4. Copy the python scripts and subfolder into the python directory.
5. Add the service script allskybot.service into /lib/systemd/system/ .
6. Enable newly added service to start at Pi startup

```bash
sudo systemctl daemon-reload
sudo systemctl enable allskybot.service
sudo systemctl start allskybot.service
```

7. Check status of the service
```bash
sudo systemctl status allskybot.service
```

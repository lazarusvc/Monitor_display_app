# Cron job to start Application on reboot (in development)

$ crontab -e
$ @reboot python /home/Monitor_display_app/app.py
$ @reboot firefox

# Command to Keep screen on at all times

$ sudo nano /etc/lightdm/lightdm.conf
[SeatDefaults]
xserver-command=X -s 0 -dpms

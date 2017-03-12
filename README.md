# Cron job to start Application on reboot (in development)

$ crontab -e <br />
$ @reboot python /home/Monitor_display_app/app.py <br />
$ @reboot firefox <br />

# Command to Keep screen on at all times

$ sudo nano /etc/lightdm/lightdm.conf <br />
[SeatDefaults] <br />
xserver-command=X -s 0 -dpms <br />

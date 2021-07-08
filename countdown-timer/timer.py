import time

def countdownTimer():
    # get the number of seconds to countdown
	no_of_secs = int(input('How many secs?: '))
	while no_of_secs:
		if no_of_secs < 60:
            # calculate the number of hours, minutes and seconds
			hrs = no_of_secs // 3600
			mins = no_of_secs // 60
			secs = no_of_secs % 60
            # format the number of hours
            # minutes and seconds to be displayed
			timer = '%02d:%02d:%02d' %(hrs, mins, secs)
			print(timer, end = '\r')
            # delay execution of code by one second
			time.sleep(1)
            # coutdown the number of seconds by 1
			no_of_secs -= 1
		elif 60 <= no_of_secs < 3600:
            # calculate the number of hours, minutes and seconds
			hrs = no_of_secs // 3600
			mins = no_of_secs // 60
			secs = no_of_secs % 60
            # format the number of hours
            # minutes and seconds to be displayed
			timer = '%02d:%02d:%02d' %(hrs, mins, secs)
			print(timer, end = '\r')
            # delay execution of code by one second
			time.sleep(1)
            # coutdown the number of seconds by 1
			no_of_secs -= 1
		elif 3600 <= no_of_secs <= 86400:
            # calculate the number of hours, minutes and seconds
			hrs = no_of_secs // 3600
			mins = (no_of_secs % 3600) // 60
			secs = (no_of_secs % 3600) % 60
			# format the number of hours
            # minutes and seconds to be displayed
			timer = '%02d:%02d:%02d' %(hrs, mins, secs)
			print(timer, end = '\r')
            # delay execution of code by one second
			time.sleep(1)
            # coutdown the number of seconds by 1
			no_of_secs -= 1
	print('Time Up!')

countdownTimer()
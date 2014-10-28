import threading
import boto, time

#Fill this array with a DB or CSV
emails = ['success@simulator.amazonses.com','success@simulator.amazonses.com','success@simulator.amazonses.com','success@simulator.amazonses.com','success@simulator.amazonses.com']

class SES():
    client = None
    def __init__(self):
        self.access_key = '[PROVIDE ACCESS KEY HERE]'
        self.secret_key = '[PROVIDE SECRET KEY HERE]'
        self.burst = 5 #Default will be override
    def get_ses_client(self):
        if not self.client:
            self.client = boto.connect_ses(self.access_key, self.secret_key)
            dict_quota = self.client.get_send_quota()
            self.burst = int(round(float(dict_quota['GetSendQuotaResponse']['GetSendQuotaResult']['MaxSendRate'])))
        return self.client

SES = SES()  

def send_email(recipient):
    client = SES.get_ses_client()
    success.append((recipient,'SUCCESS'))
    client.send_email("test@test.com",'Testing','<html><h1>Test</html>',recipient,format='html')
    print "Email sent to: " + str(recipient)

success = []
counter = 0
thread_list = []

global_start_time = time.clock() 
start_time = time.clock()
for email in emails:
    counter += 1
    t = threading.Thread(target=send_email, args=(email,)) 
    t.daemon = True
    thread_list.append(t)
    if counter % SES.burst == 0:
        for thread in thread_list:
            thread.start()
        for thread in thread_list:
            thread.join()
        end_time = time.clock()
        elapsed = end_time - start_time
        if elapsed < 1:
                sleep_time = 1 - elapsed
                print "Sleeping Main Thread for: " + str(sleep_time)
                time.sleep(sleep_time)
        #Clear
        start_time = time.clock()
        thread_list = []

# Demonstrates that the main process waited for threads to complete
global_end_time = time.clock()
global_elapsed = global_end_time - global_start_time
print "Done - Elapsed: " + str(elapsed)

import rockBlock
import serial
from rockBlock import rockBlockProtocol

class MoExample (rockBlockProtocol):

        def main(self):
		x = 0
                ser = serial.Serial('/dev/ttyACM0',9600)
                for count in range(0,5):
			while True:
                        	print "about to listen"
                        	message= ser.readline().decode('ascii')
                        	if(message.startswith("*")):
                                	print "it worked!"
                                	break
                	message = message[:-1]
                	print message
                	file = open("datafile.txt","a")
                	file.write(message)
                	file.close()
		
		while x < 25:
                	rb = rockBlock.rockBlock("/dev/ttyAMA0", self)
			signal = rb.requestSignalStrength()
			print signal
			if signal > 2:

				message = message[:-1]
				rb._clearMoBuffer()
                		rb.sendMessage(message)
				rb._clearMoBuffer()
                		rb.close()
				break
			else:
				signal = rb.requestSignalStrength()
			rb.close()
			x = x+1
        def rockBlockTxStarted(self):
                print "rockBlockTxStarted"

        def rockBlockTxFailed(self):
                print "rockBlockTxFailed"
                file = open("logfile.txt","a")
                file.write("It failed bro")
                file.close()
		

        def rockBlockTxSuccess(self,momsn):
                print "rockBlockTxSuccess " + str(momsn)
                file = open("logfile.txt","a")
                file.write("it worked")
                file.close()

if __name__ == '__main__':
        MoExample().main()


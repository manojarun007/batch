import logging
logging.basicConfig(level=logging.DEBUG, # for flter the log statements
	format="%(asctime)s-->%(levelname)s==>%(message)s",
	filename="log.txt")
logging.info("program started")
logging.info("Getting an input from the user")
a=raw_input("Enter a value:")
logging.info("got the a value")
logging.debug("a=%s"%a)
b=raw_input("enter b value:")
logging.info("got the b value")
logging.debug("b=%s"%b)
logging.debug("befor conversion: a=%s, b=%s"%(a,b))
try:
	a=float(a)
	logging.info("a value conversion done.")
	logging.debug("a=%s"%a)
	b=float(b)
	logging.info("b value conversion done.")
	logging.debug("b=%s"%b)
	logging.debug("after conversion: a=%s, b=%s"%(a,b))
	logging.info("calculating the result")
	res=a/b
	logging.info("result calculation done")
	logging.debug("result=%s"%res)
	print "result=",res
except ZeroDivisionError as err:
	logging.error(err.message)
	logging.error("should not enter zero for b")
	print "should not enter zero for b"
except ValueError as err:
	logging.error(err.message)
	logging.error("expecting digits only for a,b values")
	print "expecting digits only for a,b values"
except Exception as err:
	logging.error(err.message)
	print "something went wrong: error: %s"%err
logging.info("done!!")
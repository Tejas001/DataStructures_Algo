
import logging
ext_data = {
    'user': 'tejas.chougule1994@gmail.com'
}
class Logging:

    def __init__(self):
        self.logging_main()

    def anotherFunction(self):
        logging.debug("This is debug function message", extra= ext_data)

    def logging_main(self):

        fmtstr = "User:%(user)s %(asctime)s : %(levelname)s : %(funcName)s Line:%(lineno)d %(message)s"
        datestr = "%Y-%m-%d %I:%M:%S %p"

        logging.basicConfig(level=logging.DEBUG, filename='output.log', 
                            filemode="w",
                            format=fmtstr,
                            datefmt=datestr)
        logging.debug('This debug logging', extra=ext_data)
        logging.info('This info logging', extra=ext_data)
        logging.warning('This warning logging', extra=ext_data)
        logging.error('This error logging', extra=ext_data)
        logging.critical('This critical logging', extra=ext_data)
        logging.info('Here is {} and an int {}'.format('string',10), extra=ext_data)
        self.anotherFunction()
        
if __name__ == "__main__":
    cls1 = Logging()
import inspect
import logging


class Test_LogGenerator():

    @staticmethod
    def logger():

        name=inspect.stack()[1][3] ;

        logger=logging.getLogger(name) ;

        log_file=logging.FileHandler("D:\\PYTHON CT15\\REVISION\logs\\swaglab.log") ;

        log_format=logging.Formatter(" %(asctime)s : %(name)s : %(levelname)s : %(lineno)d : %(funcName)s : %(message)s ") ;

        log_file.setFormatter(log_format) ;

        logger.addHandler(log_file) ;

        logger.setLevel(logging.INFO) ;

        return logger ;
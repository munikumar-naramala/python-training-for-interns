def logging_module_debugging():
    import logging
    logging.basicConfig(filename='test.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s',
                        level=logging.DEBUG)
    logging.warning('This will get logged to a file')

    logging.debug('This is a debug message')
    logging.info('This is an info message')
    logging.warning('This is a warning message')
    logging.error('This is an error message')
    logging.critical('This is a critical message')

    # def logg_from_debug_level():
    #     import logging
    #     logging.basicConfig(filename='test2.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s',
    #                         level=logging.DEBUG)
    #     logging.debug('this debug level will also be logged')
    #     logging.critical('this is a blah')


if __name__ == '__main__':
    logging_module_debugging()

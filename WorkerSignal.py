from PyQt5 import QtCore

class WorkerSignals(QtCore.QObject):
    '''
    Defines the signals available from a running worker thread.

    Supported signals are:

    finished
        No data

    error
        `tuple` (exctype, value, traceback.format_exc() )

    result
        `object` data returned from processing, anything

    '''
    finished = QtCore.pyqtSignal()
    error =  QtCore.pyqtSignal(tuple)
    result =  QtCore.pyqtSignal(object)
    progress =  QtCore.pyqtSignal(int)
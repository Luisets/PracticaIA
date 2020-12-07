from PySide2 import QtCore

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
    finished = QtCore.Signal()
    error =  QtCore.Signal(tuple)
    result =  QtCore.Signal(object)
    progress =  QtCore.Signal(int)
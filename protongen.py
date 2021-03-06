#!/usr/bin/env python

__author__ = "Pruthvi Kumar, pruthvikumar.123@gmail.com"
__copyright__ = "Copyright (C) 2018 Pruthvi Kumar | http://www.apricity.co.in"
__license__ = "Public Domain"
__version__ = "1.0"

import argparse
from colorama import Fore, Style
from nucleus.execgen import ExecGen
from nucleus.metagen import MetaGen


class ProtonGen(MetaGen, ExecGen):

    def __init__(self):
        super(ProtonGen, self).__init__()
        self.logger = self.getLogger(logFileName='protonGen_logs',
                                     logFilePath='{}/trace/protonGen_logs.log'.format(self.ROOT_DIR))
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument('--micName', help='MIC stands for Model Interface & Controller. Proton spins up'
                                                   'the MIC stack for you; when provided with a name.')
        self.parser.add_argument('--port', help='Port for PROTON to launch the interface onto. Defaults to 3000.')
        self.parser.add_argument('--forceStart', help='Do not create a new MIC Stack; but, executes PROTON stack '
                                                      'by re-generating main with existing iFace!')
        self.proton_args = self.parser.parse_args()

        if (self.proton_args.micName == None):
            if (self.proton_args.forceStart != None):
                self.generateExecutor(port=3000)
                print(Fore.GREEN + 'PROTON initialized with existing iFace stack! Starting service '
                                   '@ 3000' + Style.RESET_ALL)
                self.logger.info('PROTON initialized with existing iFace stack! Starting service @ 3000')
            else:
                raise (Fore.LIGHTRED_EX + '[PROTON-GEN] - There is no name provided for Proton to initiate. '
                                          'Please provide a valid micName using --micName argument' + Style.RESET_ALL)
        else:
            if (self.proton_args.port == None):
                self.proton_args.port = 8000
            self.__creator(self.proton_args.micName, self.proton_args.port)

    def __creator(self, micName, port):

        try:
            self.newMIC(micName=micName)
            self.generateExecutor(port=port)
            print(Fore.GREEN + 'PROTON initialized for {}. Starting service @ {}'.format(micName, port) + Style.RESET_ALL)
            self.logger.info('[ProtonGen] Proton initialized for micName - {} @ port {}'.format(micName, port))
        except Exception as e:
            self.logger.exception('[ProtonGen] Error during protonGen initialization for micName '
                                  '{}. Details: {}'.format(micName, str(e)))
            raise (Fore.LIGHTRED_EX + '[ProtonGen] Error during protonGen initialization for micName '
                                  '{}. Details: {}'.format(micName, str(e)) + Style.RESET_ALL)

if __name__ == '__main__':
    pg = ProtonGen()



import ctypes

import SDIL_Tests.FW_Val.FW_ValUtils.GreyBoxEngine as GreyBoxEngine

import infrastructure.UFSVldTestCase as UFSVldTestCase
import infrastructure.SDIL_Utils.DVT.DvtFeatures.SmartReport.Utils.SmartReportUtil as SmartReportUtil
from infrastructure.SDIL_Utils.DVT.DvtFeatures.SmartReport.Utils.SmartReportUtil import SmartReport
import infrastructure.SDIL_Utils.FW_ValUtils.GeneralUtils as GeneralUtils
import infrastructure.DvtUtils.ResetInitUtil.ResetInit as ResetInit
from infrastructure.SDIL_Utils.DVT.DvtEnums.Resets import ResetType as ResetTypes
from infrastructure.SDIL_Utils.DVT.DvtEnums.Resets import ResetPreconditionEnum

CROSSING_THERSHOLD_MAX = 95
CROSSING_THERSHOLD_MIN = -25
MAX_TEMPERATURE = 125
MIN_TEMPERATURE = -42

class Seq_D_MinMaxTemperatureCounters(UFSVldTestCase.UFSVldTestCase):

    def setUp(self):
        super(Seq_D_MinMaxTemperatureCounters, self).setUp()
        self.gbe = GreyBoxEngine.GreyBoxEngine()
        self.gbe.preFunc = self.PreFuncChangeTemp
        self.genUtils = GeneralUtils.GeneralUtils()
        self.randObj = self.tester.tf_api.get_randomizer()
        self.srUtil = SmartReportUtil.SmartReportUtil(self.randObj, tester=self.tester)
        self.livet = self.tester.dutf_api.get_livet()
        self.rootObj = self.livet.GetRootObject()
        self.numOfChecks = 0
        # MaxTemperature count each time that the temperature above 95
        self.expectedMaxTemperatureCounter = 0
        # MinTemp count each time that the temperature lass then -25
        self.expectedMinTemperatureCounter = 0
        self.expectedTemp = 0
        self.checkSREnable = True
        self.freq = 0
        self.resetInitUtil = ResetInit.ResetInit()

    def seq_D_MinMaxTemperatureCounters(self):
        super(Seq_D_MinMaxTemperatureCounters, self).ufsVldTestCase()
        self.sr = SmartReport(tester=self.tester)
        minTemperatureCounter = self.sr.MinTemperatureCounter
        maxTemperatureCounter = self.sr.MaxTemperatureCounter
        self.srUtil.myAssertEq("MinTemperatureCounter",
                               minTemperatureCounter,
                               0)
        self.srUtil.myAssertEq("MaxTemperatureCounter",
                               maxTemperatureCounter,
                               0)
        self.gbe.Start(disableAllOperationsBetween=True)

    def PreFuncChangeTemp(self, cmdInfo=None, additionalInfo = None):
        self.freq += 1
        if self.freq % 40 == 0:
            self.sr = SmartReport(tester=self.tester)
            currentTemperature = self.sr.currentTemperature
            if abs(currentTemperature - self.expectedTemp) <= 1:
                self.checkSREnable = True

        if self.checkSREnable:
            self.sr = SmartReport(tester=self.tester)
            minTemperatureCounter = self.sr.MinTemperatureCounter
            maxTemperatureCounter = self.sr.MaxTemperatureCounter
            self.currentTemperature = self.sr.currentTemperature
            self.logger.VTFInfo("minTemperatureCounter = " + str(minTemperatureCounter) +
                                ", maxTemperatureCounter = " + str(maxTemperatureCounter) +
                                ", currentTemperature = " + str(self.currentTemperature))
            self.numOfChecks += 1
            self.srUtil.myAssertEq("MinTemperatureCounter",
                               minTemperatureCounter,
                               self.expectedMinTemperatureCounter)
            self.srUtil.myAssertEq("MaxTemperatureCounter",
                               maxTemperatureCounter,
                               self.expectedMaxTemperatureCounter)

            # Change Temperature
            self.expectedTemp = self.SetNewTemperature()
            # self.PerformPowerCycle()

        if self.numOfChecks > 10:
            self.gbe.Stop()

    def SetNewTemperature(self):
        self.sr = SmartReport(tester=self.tester)
        temperature = self.randObj.choice(list(range(-50, 140, 10)))
        self.logger.VTFInfo("set new temperature: {}".format(temperature))

        self.rootObj.SetTemperature(temperature)
        if temperature < CROSSING_THERSHOLD_MIN:
            if self.currentTemperature > CROSSING_THERSHOLD_MIN:
                self.expectedMinTemperatureCounter += 1

        elif temperature > CROSSING_THERSHOLD_MAX:
            if self.currentTemperature < CROSSING_THERSHOLD_MAX:
                self.expectedMaxTemperatureCounter += 1

        if temperature < MIN_TEMPERATURE:
            temperature = MIN_TEMPERATURE

        if temperature > MAX_TEMPERATURE:
            temperature = MAX_TEMPERATURE

        self.checkSREnable = False
        return temperature


    def PerformPowerCycle(self, resetPrecondition=ResetPreconditionEnum.Nothing):

        self.logger.VTFInfo("PerformPowerCycle:: Reset Initiated. resetPrecondition: {}" .format(resetPrecondition))
        # add SSU3 - reset with notification - resetPreconditionEnum=ResetPreconditionEnum.SSU3
        self.resetInitUtil.ResetExecuter(ResetType=ResetTypes.HW, resetPreconditionEnum=resetPrecondition)
        self.logger.VTFInfo("PerformPowerCycle:: Reset Ended")
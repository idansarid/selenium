diff - -git
a / Tests / SDIL_Tests / FW_Val / ErrorInjectionsV2 / CrossProject / CrossProjectsLoader.py
b / Tests / SDIL_Tests / FW_Val / ErrorInjectionsV2 / CrossProject / CrossProjectsLoader.py
index
5
f623ff2fc.
.2e06
d894de
100644
--- a / Tests / SDIL_Tests / FW_Val / ErrorInjectionsV2 / CrossProject / CrossProjectsLoader.py
+++ b / Tests / SDIL_Tests / FW_Val / ErrorInjectionsV2 / CrossProject / CrossProjectsLoader.py


@ @


-7, 6 + 7, 7 @ @
from SDIL_Tests.FW_Val.ErrorInjectionsV2.Common.PowerDropErrorBase import PowerD
from SDIL_Tests.FW_Val.ErrorInjectionsV2.Common.CeccCvdHandler import CeccCvdHandler
from SDIL_Tests.FW_Val.ErrorInjectionsV2.CrossProject.OpbuidFamiliesLoader import OpbuidFamiliesLoader
import infrastructure.TesterInfra.tester as Tester

+
from collections import namedtuple

CECC_LOWER_SAFE_ZONE = 0.07
CECC_UPPER_SAFE_ZONE = 0.2


@ @


-30, 9 + 31, 11 @ @


class CrossProjectsLoader(object):
    self.minUeccRandBer = None
    self.maxUeccRandBer = None
    self.is_rollback_needed = None


+        self.waypoints_args = None
self.opbuidFamily = OpbuidFamiliesLoader()
self.set_cecc_bers()
self.set_uecc_bers()
+        self.set_waypoints_args()
self.cross_project_loader()


def cross_project_loader(self):
    @ @

    -75, 3 + 78, 17 @ @

    class CrossProjectsLoader(object):

        else:
    self.minUeccRandBer = max(self.projDefs.UECC_SLC_BER, self.projDefs.UECC_MLC_BER)
    self.maxUeccRandBer = MAX_BER_BORDER


+
+


def set_waypoints_args(self):
    +        args = {
        "D_MODEL_BME_RLC_WRITE_STEP": "destStartPfmu destStartMfmu targetOpbUid dummiesCount sourceMfmu validFmusNum sourcePfmu"}


+        project_args = {'SWIFT_PRO': {
    "D_MODEL_BME_RLC_WRITE_STEP": "destStartPfmu destStartMfmu targetOpbUid dummiesCount sourceMfmu validFmusNum sourcePfmu metaDieArg rlcType stepId"}}
+
if self.current_project in project_args:
    +            args = project_args[self.current_project]
+        self.waypoints_args = dict()
+
for (waypoint, arg_list) in args.iteritems():
    +            self.waypoints_args[waypoint] = namedtuple(waypoint, arg_list)
+
+


def get_args_by_project(self, waypoint, args):
    +        ArgsTuple = self.waypoints_args[waypoint]


+
return ArgsTuple(args)
+
diff - -git
a / Tests / SDIL_Tests / FW_Val / ErrorInjectionsV2 / MetaAddressing / ProgramErrorsBase.py
b / Tests / SDIL_Tests / FW_Val / ErrorInjectionsV2 / MetaAddressing / ProgramErrorsBase.py
index
b25f300103..b06a9b11e3
100644
--- a / Tests / SDIL_Tests / FW_Val / ErrorInjectionsV2 / MetaAddressing / ProgramErrorsBase.py
+++ b / Tests / SDIL_Tests / FW_Val / ErrorInjectionsV2 / MetaAddressing / ProgramErrorsBase.py


@ @


-13, 7 + 13, 6 @ @
from SDIL_Tests.FW_Val.ErrorInjectionsV2.MetaAddressing.EeiMetaStimuliBase impor
from SDIL_Tests.FW_Val.ErrorInjectionsV2.Common.CommonConfigurations import IS_DEBUG_MODE, MetaBlockId, MetaBlockData
from SDIL_Tests.FW_Val.PfiPro.Common.CommonDefs import NUMBER_OF_FMUS_IN_PFI_SNAPSHOT_WRITES

-


class ProgramErrorsBase(EeiMetaStimuliBase):
    """
    brief: This class is a base class for different Eei Stimuli(erase, prog, etc.), subclass must
@@ -94,28 +93,23 @@ class ProgramErrorsBase(EeiMetaStimuliBase):
        :param destStartMfmu = args[1]
        :param opbUid = args[2]
        """


-        destStartPfmu = args[0]
-        destStartMfmu = args[1]
-        targetOpbUid = OPBUids(args[2])
-        dummiesCount = args[3]
-        sourceMfmu = args[4]
-        validFmusNum = args[5]
-        sourcePfmu = args[6]
-        metaDieArg = args[7]
-        rlcType = args[8]
-        stepId = args[9]
+        arg = self.crossProject.get_args_by_project("D_MODEL_BME_RLC_WRITE_STEP", args)
+        targetOpbUid = OPBUids(arg.targetOpbUid)
+        metaDieArg = ", metaDieArg:{}".format(arg.metaDieArg) if "metaDieArg" in arg._fields else ""
+        rlcType = ", rlcType:{}".format(arg.rlcType) if "rlcType" in arg._fields else ""
+        stepId = ", stepId:{}".format(arg.stepId) if "stepId" in arg._fields else ""
phyAddr = AddressUtil.PhysicalAddress()
-        phyAddr.UpdateObjcetByGivenFmu(destStartPfmu)
-        metaDie, metaBlock, mfmuOffset, blockType = self.generalUtils.MfmuToMetaAddrObj(destStartMfmu)
-        injectionDone = self.ConditionalInjectError(pfmu=destStartPfmu, opbUid=targetOpbUid, metaBlock=metaBlock,
                                                     -                                                    amountFmus = validFmusNum)
+        phyAddr.UpdateObjcetByGivenFmu(arg.destStartPfmu)
+        metaDie, metaBlock, mfmuOffset, blockType = self.generalUtils.MfmuToMetaAddrObj(arg.destStartMfmu)
+        injectionDone = self.ConditionalInjectError(pfmu=arg.destStartPfmu, opbUid=targetOpbUid, metaBlock=metaBlock,
                                                     +                                                    amountFmus = arg.validFmusNum)
if any([injectionDone, IS_DEBUG_MODE]):
    self.logger.VTFInfo(
        "ProgramErrorsBase::CB_D_MODEL_BME_RLC_WRITE_STEP: destStartMfmu:{}, opbUid:{}({}), destStartPfmu:{}, die:{}, plane:{}, "
        "block:{}, wordline:{}, string:{}, page:{}, fmu:{}, metaDie:{}, metaBlock:{}, mfmuOffset:{}, blockType:{}, dummiesCount:{}, "
        - "sourceMfmu:{}, sourcePfmu:{}, metaDieArg:{}, rlcType:{}, stepId:{}".
        - format(destStartMfmu, targetOpbUid, int(targetOpbUid), destStartPfmu, phyAddr.die, phyAddr.plane,
                 phyAddr.block,
                 -                                       phyAddr.wordline, phyAddr.string, phyAddr.page, phyAddr.fmu,
                 metaDie, metaBlock, mfmuOffset, blockType, dummiesCount,
                 -                                       sourceMfmu, sourcePfmu, metaDieArg, rlcType, stepId))
+                                "sourceMfmu:{}, sourcePfmu:{}{}{}{}".
+                                format(arg.destStartMfmu, targetOpbUid, int(targetOpbUid), arg.destStartPfmu,
                                        phyAddr.die, phyAddr.plane, phyAddr.block,
                                        +                                       phyAddr.wordline, phyAddr.string,
                                        phyAddr.page, phyAddr.fmu, metaDie, metaBlock, mfmuOffset, blockType,
                                        arg.dummiesCount,
                                        +                                       arg.sourceMfmu, arg.sourcePfmu,
                                        metaDieArg, rlcType, stepId))

def CB_D_MODEL_MST_STORE(self, eventKey, args, processorID):

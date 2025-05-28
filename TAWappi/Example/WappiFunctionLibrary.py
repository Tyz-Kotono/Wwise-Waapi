from WaapiSubSystem import *
from WappiCommon import *
from Wwise_UI import *


def InitWappi():
    SetSelectOptionsAndData(defaultOpstionsReturn)


def SetSelectOptions(options):
    """
    Sets the options for a select element in the Wappi application.

    :param options: A list of options to set for the select element.
    """

    SetSelectOptionsAndData(options)


def SetSelectOptionsAndData(options):
    """
    Sets the options and data for a select element in the Wappi application.

    :param instance: An instance of WwiseDataInstance.
    :param options: A list of options to set for the select element.
    """
    dataSystem = WwiseDataInstance()
    dataSystem.Set_optionsList(WwiseListType.SELECT, options)

    client = dataSystem.getClient()
    result = getSelectedObjects(client, options)
    dataSystem.set_Datalist(WwiseListType.SELECT, result)


def GetWappiData(type: WwiseListType):
    dataSystem = WwiseDataInstance()
    Options = dataSystem.get_optionsList(type)
    Datas = dataSystem.get_Datalist(type)
    return Options, Datas

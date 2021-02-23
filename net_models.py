
def getHostname(nameOut):
    nameSp = nameOut.split()
    hostname = nameSp[1]
    return hostname

def getVersion(verOut):
    verSp = verOut.split()
    version = verSp[1]
    return version

def getSerial(ser):
    serLine = ser.split()
    serial = serLine[4]
    return serial

def getModel(modOut):
    modSp = modOut.splitlines()
    for mod in modSp:
        modLine = mod.split()
        model = modLine[4]
        modelNumbers.append(model)

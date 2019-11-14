import r2pipe
import base64

def staticAnalysis(filePath):
    global infile
    infile = r2pipe.open(filePath)
    infile.cmd('aaa')
    return extract_all()

def functions_analysis():
    functions = infile.cmdj('afllj')
    return functions

def string_analysis():
    strings = infile.cmdj('izzj')
    # decode from base 64
    for i in range(len(strings)):
        strings[i]['string'] = base64.b64decode(strings[i]['string']).decode("utf-8")
    return strings

def variables_analysis():
    variable = infile.cmdj('afvj')
    return variable

def dll_analysis():
    dlls = infile.cmdj('iij')
    return dlls

def struct_analysis():
    structs = infile.cmdj('tscj')
    return structs

def packet_protocol_analysis():
    # TODO
    protocols = []
    return protocols

def extract_all():
    function = functions_analysis()
    string = string_analysis()
    variable = variables_analysis()
    dll = dll_analysis()
    #print(type(function)) for testing
    return [function, string, variable, dll]

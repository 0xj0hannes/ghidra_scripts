def list_xrefs_call_funcs(func_names):
    manager = currentProgram.getFunctionManager()
    for func in manager.getFunctions(True):
        if func.getName() in func_names:
            for xref in getReferencesTo(func.getEntryPoint()):
                if xref.getReferenceType().toString() == 'UNCONDITIONAL_CALL':
                    print('{} is called at {}'.format(func.getName(), xref.getFromAddress()))

def main():
    dangerous_funcs = ['getpw', 'gets', 'sprintf', 'strcat', 'strcpy', 'vsprintf']

    list_xrefs_call_funcs(dangerous_funcs)

if __name__ == '__main__':
    main()

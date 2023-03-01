#
#@author 
#@category 
#@keybinding
#@menupath
#@toolbar

#TODO: Add script code here
def main():
    regex = askString('MyRegex', 'what do you want to search?')
    
    if not regex:
        print('[!] no inputs')
        return
    
    founds = findBytes(None, regex, -1)
    if not founds:
        print('[!] nothing found')
        return
    
    for found in founds:
        value = getDataAt(found).getValue()
        print('[+] {addr} -> {data}'.format(addr=found, data=value))
        
if __name__ == '__main__':
    main()
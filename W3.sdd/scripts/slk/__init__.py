
def readSlk(file):
    objects = dict()
    keyMappings = dict()
    nowY=0
    for line in open(file,'r'):
        char = line[0]
        if char == 'I':
            pass
            #print 'SLK_F'
        elif char == 'B':
            pass
            #print 'SLK_INFO'
        elif char == 'C':
            props = parseData(line)
            if 'y' in props:
                nowY = props['y']
            if nowY == 1:
                # We are having a problem with some propertiy keys not having an
                # 'x' component. We'll have to look into that...
                if 'k' in props and 'x' in props:
                    keyMappings[props['x']] = props['k']
            else:
                if 'y' in props:
                    nowY = props['y']
                    objects[nowY] = dict()
                if 'x' in props and len(keyMappings)>0 and props['x'] in keyMappings:
                    key = keyMappings[props['x']]
                    objects[nowY][key] = props['k']
        elif char == 'E':
            pass
            #print 'EOF'
    return objects

def parseData(data):
    props = dict()
    for prop in data.split(';'):
        char = prop[0]
        if char == 'X':
            props['x'] = int(prop[1:])
        elif char == 'Y':
            props['y'] = int(prop[1:])
        # This property might not always be the last property on the line
        # We need to fix this
        elif char == 'K':
            props['k'] = prop[1:-2].replace('\"','')
        elif char == 'D':
            props['k'] = prop[1:-2]

    return props

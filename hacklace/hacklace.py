import pew

def load():
    print("Loading...")
    apps = []
    state = 'start'

    with open('hacklace.txt') as f:
        while line := f.readline():
            print("L:", line)
            bytes = bytearray()
            if state == 'start':
                if line.startswith('HL'):
                    state = 'read'
                else:
                    continue
            elif state == 'read':
                i = 0
                start = -1
                while i < len(line):
                    print("C:", i)
                    c = line[i]
                    if c == '\n':
                        break
                    if ord(c) < 32:
                        i += 1
                        continue

                    if start >= 0:
                        if c == '#':
                            break
                        if c == '\\':
                            bytes += bytearray.fromhex(line[start:i])
                            start = -1 
                    else:
                        if c == '\\':
                            i += 1
                            start = i
                            continue
                        else:
                            bytes.append(ord(c))
                    i += 1
            
            # We only want animations
            if bytes != b'' and bytes[0] == 0:
                apps.append({
                    'speed': bytes[1] >> 4,
                    'delay': bytes[1] & 0xf,
                    'dir': bytes[2] >> 4,
                    'inc': bytes[2] & 0xf,
                    'data': bytes[3:-2],
                    # 'bytes': bytes
                })


    print(apps)






def run():
    pew.init()
    screen = pew.Pix()
    x = 0
    y = 0
    dx = 1
    dy = 1
    while True:
        x += dx
        y += dy
        screen.pixel(x, y, 3)
        pew.show(screen)
        pew.tick(1/12)

if __name__ == '__main__':
    load()
    #run()
import sys
# недодел
lines = []
for l in sys.stdin:
    l = l.replace('\n', '')
    lines.append(l)

n, m = list(map(int, lines[0].split()))
com = lines[1]
x, y = 0, 0
k = 0
while k < m:
    com1 = com
    if k < m:
        if k + 3 < m:
            if 'NNN' in com1 and k + 3 < m:
                com1 = com1.replace('NNN', '', 1)
                k += 3
            elif 'NNE' in com1 and k + 3 < m:
                com1 = com1.replace('NNE', '', 1)
                k += 3
            elif 'NNS' in com1 and k + 3 < m:
                com1 = com1.replace('NNS', '', 1)
                k += 3
            elif 'NNW' in com1 and k + 3 < m:
                com1 = com1.replace('NNW', '', 1)
                k += 3

            elif 'NEN' in com1 and k + 3 < m:
                com1 = com1.replace('NEN', '', 1)
                k += 3
            elif 'NEE' in com1 and k + 3 < m:
                com1 = com1.replace('NEE', '', 1)
                k += 3
            elif 'NES' in com1 and k + 3 < m:
                com1 = com1.replace('NES', '', 1)
                k += 3
            elif 'NEW' in com1 and k + 3 < m:
                com1 = com1.replace('NEW', '', 1)
                k += 3

            elif 'NSN' in com1 and k + 3 < m:
                com1 = com1.replace('NSN', '', 1)
                k += 3
            elif 'NSE' in com1 and k + 3 < m:
                com1 = com1.replace('NSE', '', 1)
                k += 3
            elif 'NSS' in com1 and k + 3 < m:
                com1 = com1.replace('NSS', '', 1)
                k += 3
            elif 'NSW' in com1 and k + 3 < m:
                com1 = com1.replace('NSW', '', 1)
                k += 3

            elif 'NWN' in com1 and k + 3 < m:
                com1 = com1.replace('NWN', '', 1)
                k += 3
            elif 'NWE' in com1 and k + 3 < m:
                com1 = com1.replace('NWE', '', 1)
                k += 3
            elif 'NWS' in com1 and k + 3 < m:
                com1 = com1.replace('NWS', '', 1)
                k += 3
            elif 'NWW' in com1 and k + 3 < m:
                com1 = com1.replace('NWW', '', 1)
                k += 3

            elif 'ENN' in com1 and k + 3 < m:
                com1 = com1.replace('ENN', '', 1)
                k += 3
            elif 'ENE' in com1 and k + 3 < m:
                com1 = com1.replace('ENE', '', 1)
                k += 3
            elif 'ENS' in com1 and k + 3 < m:
                com1 = com1.replace('ENS', '', 1)
                k += 3
            elif 'ENW' in com1 and k + 3 < m:
                com1 = com1.replace('ENW', '', 1)
                k += 3

            elif 'EEN' in com1 and k + 3 < m:
                com1 = com1.replace('EEN', '', 1)
                k += 3
            elif 'EEE' in com1 and k + 3 < m:
                com1 = com1.replace('EEE', '', 1)
                k += 3
            elif 'EES' in com1 and k + 3 < m:
                com1 = com1.replace('EES', '', 1)
                k += 3
            elif 'EEW' in com1 and k + 3 < m:
                com1 = com1.replace('EEW', '', 1)
                k += 3

            elif 'ESN' in com1 and k + 3 < m:
                com1 = com1.replace('ESN', '', 1)
                k += 3
            elif 'ESE' in com1 and k + 3 < m:
                com1 = com1.replace('ESE', '', 1)
                k += 3
            elif 'ESS' in com1 and k + 3 < m:
                com1 = com1.replace('ESS', '', 1)
                k += 3
            elif 'ESW' in com1 and k + 3 < m:
                com1 = com1.replace('ESW', '', 1)
                k += 3

            elif 'EWN' in com1 and k + 3 < m:
                com1 = com1.replace('EWN', '', 1)
                k += 3
            elif 'EWE' in com1 and k + 3 < m:
                com1 = com1.replace('EWE', '', 1)
                k += 3
            elif 'EWS' in com1 and k + 3 < m:
                com1 = com1.replace('EWS', '', 1)
                k += 3
            elif 'EWW' in com1 and k + 3 < m:
                com1 = com1.replace('EWW', '', 1)
                k += 3

            if 'NNN' in com1 and k + 3 < m:
                com1 = com1.replace('NNN', '', 1)
                k += 3
            elif 'NNE' in com1 and k + 3 < m:
                com1 = com1.replace('NNE', '', 1)
                k += 3
            elif 'NNS' in com1 and k + 3 < m:
                com1 = com1.replace('NNS', '', 1)
                k += 3
            elif 'NNW' in com1 and k + 3 < m:
                com1 = com1.replace('NNW', '', 1)
                k += 3

            elif 'NEN' in com1 and k + 3 < m:
                com1 = com1.replace('NEN', '', 1)
                k += 3
            elif 'NEE' in com1 and k + 3 < m:
                com1 = com1.replace('NEE', '', 1)
                k += 3
            elif 'NES' in com1 and k + 3 < m:
                com1 = com1.replace('NES', '', 1)
                k += 3
            elif 'NEW' in com1 and k + 3 < m:
                com1 = com1.replace('NEW', '', 1)
                k += 3

            elif 'NSN' in com1 and k + 3 < m:
                com1 = com1.replace('NSN', '', 1)
                k += 3
            elif 'NSE' in com1 and k + 3 < m:
                com1 = com1.replace('NSE', '', 1)
                k += 3
            elif 'NSS' in com1 and k + 3 < m:
                com1 = com1.replace('NSS', '', 1)
                k += 3
            elif 'NSW' in com1 and k + 3 < m:
                com1 = com1.replace('NSW', '', 1)
                k += 3

            elif 'NWN' in com1 and k + 3 < m:
                com1 = com1.replace('NWN', '', 1)
                k += 3
            elif 'NWE' in com1 and k + 3 < m:
                com1 = com1.replace('NWE', '', 1)
                k += 3
            elif 'NWS' in com1 and k + 3 < m:
                com1 = com1.replace('NWS', '', 1)
                k += 3
            elif 'NWW' in com1 and k + 3 < m:
                com1 = com1.replace('NWW', '', 1)
                k += 3
        else:
            break
print(x, y)

# недодел

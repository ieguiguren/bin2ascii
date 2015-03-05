#!/usr/bin/env python

mensaje = True
while mensaje != '':
	mensaje = raw_input('Binary sequence: ').replace(" ","")
	uncoded = [ mensaje[byte:byte+8]  for byte in range(0, len(mensaje), 8) ]
	chain = []
	for i in uncoded:
		chain.append(chr(int(i,2)))
	print ''.join(chain)

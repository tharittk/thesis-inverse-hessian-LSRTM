
#file1 = open('out_cgrtm0.txt')
#file1 = open('out_pcgrtm0.txt')
#file1 = open('out_wwpcgrtm0_2.txt')

#file1 = open('out_cgrtm0_100.txt')
#file1 = open('out_pcgrtm0_100.txt')
#file1 = open('out_wwpcgrtm0_100.txt')


#################
# print "|m_ref| : %g" %l2mref
# print "---------"
# print "**L2-norm calulation "
# #print "r = |m_k - m_ref| / |m_ref|"
# print "r = |m_k - m_ref|"
# print "---------"

# Process Model residual
for i in range(400):
	try:
		line = file1.readline().strip()
		if line[0] == "M":
			print line
	except IndexError:
		break
###################


####################
#Process data residual
print "Data residual"
print "---------"
print "** L2-norm calulation"
print "r = | d_k - d_shot |"
print "---------"

for i in range(400):
	try:
		line = file1.readline()
		if line[0] == 'D':
			line2 = line.strip()
			print line2
	except IndexError:
		break
####################
# Comment this part out when run .py
# Use this in SConstruct not this .py orload m8r module

# Process file of 100 iterations data
##
file1 = open('Dres_cg0_100.txt')

dres_cg100 = []
for i in range(110):
  try:
    line = file1.readline().split()
    if i>5:
      dres_cg100.append(float(line[4]))
  except:
    break
file1.close()
##
dres_pcg100 = []
file2 = open('Dres_pcg0_100.txt')
for i in range(110):
  try:
    line = file2.readline().split()
    if i>5:
      dres_pcg100.append(float(line[4]))
  except:
    break
file2.close()

ndres_cg = m8r.File([x/dres0 for x in dres_cg100])
ndres_pcg = m8r.File([x/dres0 for x in dres_pcg100])

print ndres_cg
print ndres_pcg

# then convert the tmp file to rsf
#sfmath< tmp.rsf output=input --out=stdout>error.rsf
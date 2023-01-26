import os
x = input("Please Enter your file name")
command1 = 'sed -n \'1~4s/^@/>/p;2~4p\' {}.fastq > OUTFILE.fasta'.format(x)
os.system(command1)
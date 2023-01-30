from Bio.Blast import NCBIXML
result_handle = open("XGDDN6HD013-Alignment.xml",'r')
blast_record =NCBIXML.read(result_handle)

E_VALUE_THRESH =0.0001
ct =0
for alignment in blast_record.alignments:
    for hsp in alignment.hsps:
        ct+=1
        if hsp.expect <E_VALUE_THRESH:
            print("\n")
            print('*******ALIGNMENT******')
            print('sequence:',alignment.title)
            print('length:',alignment.length)
            print('E value:',hsp.expect)
            print(hsp.query[0:75] + '....')
            print(hsp.match[0:75] + '....')
            print(hsp.sbjct[0:75] + '....')


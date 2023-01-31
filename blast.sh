#!/usr/bin/env bash
makeblastdb -in database.fasta -dbtype prot

for i in SRR*.fasta;
do
blastp -query "$i" -db database.fasta -out "$i"out.txt
done

import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from Bio import AlignIO
from Bio import SeqIO
from Bio.pairwise2 import format_alignment
from pathlib import Path
from Bio.Align.Applications import ClustalwCommandline
from Bio.Align.Applications import MuscleCommandline
import os
from Bio import Phylo
import glob
import screed
from Bio import pairwise2
from Bio.SeqUtils import GC
from Bio.Phylo.TreeConstruction import DistanceCalculator
from Bio.Phylo.TreeConstruction import DistanceTreeConstructor
from Bio import Entrez


def do_MSA(file):
    output.config(state="normal")
    output.delete('1.0', tk.END)
    consere
    strong_sim.delete('1.0', tk.END)
    gaps.delete('1.0', tk.END)
    deletefile()
    cline = ClustalwCommandline("clustalw2", infile=file )
    print(cline)
    clustalw_exe = r"C:\Program Files (x86)\ClustalW2\clustalw2.exe"
    clustalw_cline = ClustalwCommandline(clustalw_exe, infile=file)
    assert os.path.isfile(clustalw_exe), "Clustal W executable missing"
    stdout, stderr = clustalw_cline()
    sp = Path(file).stem
    print(sp)
    full_path=os.path.join("C:\\Users\\Rana nasser\\Downloads\\",f"{sp}.aln")
    print(full_path)
alignments = pairwise2.align.globalxx(firstseqoutput.get("1.0", "end-1c"),secondseqoutput.get("1.0", "end-1c"))
    pwoutput.insert(tk.INSERT,format_alignment(*alignments[0]))

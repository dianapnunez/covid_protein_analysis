#  🧬 Structural Bioinformatics: COVID-19 Protease & N3 Inhibitor Analysis

This repository contains a structural bioinformatics script and Jupyter Notebook designed to parse, analyze, and visualize the 3D molecular structure of the main COVID-19 protease enzyme bound to the N3 inhibitor drug.

## 📌  Project Overview
- **Target PDB ID:** 6LU7 (The crystal structure of COVID-19 main protease in complex with an inhibitor).
- **Chain A:** The main COVID-19 protease enzyme polymer structure.
- **Chain C:** The N3 inhibitor drug molecular ligand structure.

##  ⚙️  Core Pipeline Features
- **Genomic Parsing:** Extracts raw genomic data records directly from FASTA formats using Biopython.
- **High-Speed Translation:** Translates viral DNA into RNA, and translates into amino acid chains.
- **Structural Visualization:** Selectively applies customized 3D molecular layer styles to isolate individual target chains and drug ligands.

## 📂  Project Structure

```text
structural_bioinformatics_tutorial/
├── data/
│   ├── 6LU7.pdb
│   └── sequence.fasta
├── visualizing_3D_structure_of_covid-19.ipynb
├── analysis_script.py
├── protein_structure.html
├── .gitignore
├── requirements.txt
└── README.md
```

### Project Files

| File / Folder | Type | Description                                                                     |
| :--- | :--- |:--------------------------------------------------------------------------------|
| **`data/`** | Directory | Folder containing all structural and genomic data.                              |
| **`data/6LU7.pdb`** | Data File | 3D coordinate data for the protease enzyme and N3 inhibitor, from NCBI.         |
| **`data/sequence.fasta`** | Data File | Viral genome nucleotide sequence for sequence translation, from NCBI.           |
| **`analysis_script.py`** | Python Script | Pipeline script for transcribing and translating the FASTA data.                |
| **`visualizing_3D_structure_of_covid-19.ipynb`** | Notebook | Interactive environment for prototyping and 3D molecular modeling.              |
| **`protein_structure.html`** | Web Asset | Exported standalone HTML page for viewing the 3D molecule model.                |
| **`.gitignore`** | Config | Prevents tracking data files and virtual environments in git.                   |
| **`README.md`** | Markdown | Main project documentation and setup instructions.                              |


##  🚀  Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/dianapnunez/structural_bioinformatics_tutorial
cd structural_bioinformatics_tutorial
```

###  2. Set Up the Data Directory
Because raw genomic FASTA sequences can be quite large, they are excluded from this Git repository via `.gitignore`. You must set up the data directory locally:

1. Create a folder named `data/` in the project root directory.
2. Download your target COVID-19 genomic sequence file (e.g., from NCBI GenBank).
3. Save and rename the file exactly to: `data/sequence.fasta`
4. Download the 6LU7.pdb crystal structure file from the RCSB PDB database and place it in the same folder.

### 3. Install Dependencies
Ensure you have Biopython installed in your local or virtual environment:
```bash
pip install -r requirements.txt
```

###  4. Run the Pipeline
Execute the main analysis script to parse the FASTA header records:
```bash
python analysis_script.py
```

## 🧠  Learning Outcomes

* **Transcribe viral DNA sequences**
* **Translate RNA nucleotide strings**
* **Process sequence-to-structure pipelines**
* **Manage local project dependencies**
* **Parse 3D atomic coordinates**
* **Render interactive 3D protein structures**
* **Isolate target polymer chains and small-molecule drug ligands**
* **Apply customized layer styling**
* **Generate portable HTML assets**

## 🔮  Future Directions

* **Multi-Format Structural Parsing & Validation** (PDB, mmCIF, and MTZ)
* **Automated Data Curation & Quality Control (QC) Pipeline**
* **Experimental Density Docking & Cryo-EM Alignment** (EMDB & AlphaFold)
* **Biophysical Feature Mapping & Functional Insight Logging**

## 🎓  Acknowledgements

This practice project is adapted from the tutorial by **JCharisTech (Jesse E. Agbe)**:
* 📺 **Video Tutorial:** [Protein Sequence Analysis of Covid19 using BioPython on YouTube](https://youtube.com/watch?v=dxVKG2gNSos&t=1805s)
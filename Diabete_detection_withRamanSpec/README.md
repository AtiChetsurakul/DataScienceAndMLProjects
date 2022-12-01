# Raman spectroscopy to screen diabetes using ML tool

**Reference** 
<br>[1..all]  Guevara, E., Torres-Galván, J. C., Ramírez-Elías, M. G., Luevano-Contreras, C., & González, F. J. (2018). Use of Raman spectroscopy to screen diabetes mellitus with machine learning tools. Biomedical Optics Express, 9(10), 4998–5010. https://doi.org/10.1364/BOE.9.004998
<br><br>[2] Lippincott , W. &. W. (2006). Advanced Glycation End Products. Circulation. https://doi.org/10.1161/CIRCULATIONAHA.106.621854

### Scope and Topic understanding
- #### To indicate diabetes by using `Blood Biomarker` or `Analyte` called `advanced glycation end products` with `Raman spectroscopy`
    - In this dataset there are 6 Analyte including
        - 3-deoxyglucosone
        - glyoxal
        - glyoxal-lysine dimer GOLD
        - methylglyoxal
        - methylglyoxal-derived hydroimidazolone MG-H2
        - pentosidine
    <br><br>
    - what is these 6 compound ?**[2]**<br>
    <img src = 'https://www.ahajournals.org/cms/asset/838a5e28-bbae-46fd-8a56-7f87c632167c/13ff1.jpg'>
- Advanced glycation end products (AGEs) are modifications of proteins or lipids that become nonenzymatically glycated and oxidized after contact with aldose sugars.1,2 Early glycation and oxidation processes result in the formation of Schiff bases and Amadori products. 
### Ideal
- Normally, Raman spec can **ethier** identify the compound or indicating the present of compound in solution **and** finding the concentration.
- Thus, the height,Intensity or Peak area  of the spectra at **exact** wavenumber ($cm^{-1}$) can tell both concentration and **bond** identification.

-----------------------------------------

## Progress 

- **DONE** Implenment the baseline Model according to the [1] but still not perform DATAENGINEER to mesh the spectra 
- **DONE** 29 nov, we finish preprocessing, basic model traing using deep-learning method.
- **DONE** making , easy to follow data training notebook.
- **DONE** training with ML nd DL.
- **DONE** Concluding result.

----------------------------------------------


## TO use

- to read our work as pdf please look at `CP present.pdf`
- follow the step on `datawatcher.ipynb`,and you can download dataset from `Kaggle` 
- After finish download data, all the `csv` file can be place in `dataset` directory which you can create new here
- then run `bash starter.sh`, `zsh starter.sh` or `ssh starter.sh` depend on your `shell`
    - the list in `requirements.txt` is inculding unneed gym, please be aware.
- In `datawatcher`, we focus on EDA process of the data and also learn the dataset.
- In `model_fitting.ipynb`, we hide the EDA step for easier looking
- In `src` directory, we provide python function module that might help.
- Want to try your DL model or ML model plese visit 
    - for DL`light_template.ipynb`
    - for ML **IN progress**

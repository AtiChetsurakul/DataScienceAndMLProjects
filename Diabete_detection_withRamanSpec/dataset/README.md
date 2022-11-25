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

- Implenment the baseline Model according to the [1] but still not perform DATAENGINEER to mesh the spectra

----------------------------------------------


## TO use

- follow the step on `datawatcher.ipynb`,and you can download dataset from `Kaggle` 
# EEG Motor Movement/Imagery Dataset


- Prelim the dataset from `physionet.org`
- Dataset consist of task as follow 
```
    Experimental Protocol
        Subjects performed different motor/imagery tasks while 64-channel EEG were recorded using the BCI2000 system (http://www.bci2000.org). Each subject performed 14 experimental runs: two one-minute baseline runs (one with eyes open, one with eyes closed), and three two-minute runs of each of the four following tasks:

        A target appears on either the left or the right side of the screen. The subject opens and closes the corresponding fist until the target disappears. Then the subject relaxes.
        A target appears on either the left or the right side of the screen. The subject imagines opening and closing the corresponding fist until the target disappears. Then the subject relaxes.
        A target appears on either the top or the bottom of the screen. The subject opens and closes either both fists (if the target is on top) or both feet (if the target is on the bottom) until the target disappears. Then the subject relaxes.
        A target appears on either the top or the bottom of the screen. The subject imagines opening and closing either both fists (if the target is on top) or both feet (if the target is on the bottom) until the target disappears. Then the subject relaxes.
```

- ECG device (electrode) format in this [pdf](https://physionet.org/content/eegmmidb/1.0.0/64_channel_sharbrough.pdf)




- Reference dataset
    - [Original publication] [Schalk, G., McFarland, D.J., Hinterberger, T., Birbaumer, N., Wolpaw, J.R. BCI2000: A General-Purpose Brain-Computer Interface (BCI) System. IEEE Transactions on Biomedical Engineering 51(6):1034-1043, 2004.](http://www.ncbi.nlm.nih.gov/pubmed/15188875)

    - [PhysioNet] Goldberger, A., Amaral, L., Glass, L., Hausdorff, J., Ivanov, P. C., Mark, R., ... & Stanley, H. E. (2000). PhysioBank, PhysioToolkit, and PhysioNet: Components of a new research resource for complex physiologic signals. Circulation [Online]. 101 (23), pp. e215–e220.

------------------------------------------
## Dataset are from [here](https://physionet.org/content/eegmmidb/1.0.0/)

-------------------------------------------

## able to download wit terminal via [wget](https://www.gnu.org/software/wget/)


--------------------------------------------


## ABstract of dataset can be found at the [here](https://physionet.org/content/eegmmidb/1.0.0/)


----------------------------------------------

## TO use

- `with terminal` type `mkdir data_keep;cd data_keep;wget -r -N -c -np https://physionet.org/files/eegmmidb/1.0.0/`

- What we are going to do is following the guide [here](https://mne.tools/dev/auto_tutorials/intro/10_overview.html)

- Also, [here](https://github.com/nutapol97/EEG-Motor-Imagery-Classification)

- Addition [RDEDFANN](https://physionet.org/physiotools/wag/rdedfa-1.htm)

--------------------------------------------------

 
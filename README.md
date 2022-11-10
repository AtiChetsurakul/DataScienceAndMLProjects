# MLproject_group2work
> this respiratory created for implement few ML model.
<br>

## Contributor


- ### objective
	- To sent as class project home work for `CP for DSAI` class as final project.
	- To learn more on the process for implementing ML model.


- ### October Progress 
	- RAMANporkfat
		- ~~The `http://www.models.life.ku.dk/RAMANporkfat` dataset are unable to load due to it is `.mat` file~~.
		- The loaded data are not well labeled; it quite hard to use.
		- Since scope are too  wide, format is not so good and reference paper are quite old, I put this topic **onhold**.

	- RAMAN diabete
		- Understanding dataset and paper. > done
		- ETL > Done
		- Prelim > find some different baseline signal 
		- ABORT LIKEly to be done quite easy.
	
	- PlantVillage
		- ETL with both ofline and online.
			- might go with online `deeplake` because it easier.
		- Using **simple** `tensorflow` model blueprint that created from my previous class.
			- fitting with Deeplearning (maxpool,convolu2D,some hidden layer)
			- with 80% of 300 sample (3 labels) was choose and photo was resized to 64*64
				- background
				- stawberry
				- tomato
			- Result -> greate accuracy
				- <h3>How to use the script</h3>
					- for Retriving data first on `keep script retrive` directory, the `picture_retrival.py` and `directory_retrive.py` are need
					- you need to change some in `picture_retrival.py` other than that you can retrive a `list` of picture using script
					- on `simple_tf_model.py` is a **temp** model blueprint to test the data.
					- On `Simple model` notebook you will see how I use the data to generate simple model
					- asset of model are at `simple_model_ati` directory.
		

		- TODO > study
		- We need to rescale the imagevalue ( the value of the color).
	
- ### Nov Progress
	- 11/10/2022
		- Raman for diabete type 2
			<!-- - On hold || dataProblem -->
			- Finish Baseline model **without** implement the Validation set.

			- I Put this topic on hold due to It seem too easy to solve.

		- Plant Village
			- Baseline model implemantation

		- EEG EEG Motor Movement/Imagery Dataset
			- Retrive dataset from [here](https://physionet.org/content/eegmmidb/1.0.0/)
			- starting




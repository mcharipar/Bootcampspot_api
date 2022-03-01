# Bootcampspot_api
Python package to simplify working with the [bootcampspot.com](https://bootcampspot.com) api.

This is a work in progress and looking to add additional features.
- [x] GUI
    - [ ] Update UI, add more interactivity for below features.
        - [x] Add course feedback tab.
            - [x] Add questions table.
                - [ ] Update this table to be used outside of "Update All button."
        - [x] Have Table selections update main Table and visuals.
            - [ ] Clean up and add selection for all tabs.
        - [x] Add Visuals to Tabs.
            - [ ] Clean up and add PDF/visulas to tabs themselves and create more.
- [ ] Create executable file for major OS's and a simple command to compile the executable on any machine capable of running [Anaconda](https://docs.anaconda.com/anaconda/install/index.html).
    - [ ] Possible Docker Containter creation.
- [ ] Publish to [Pypi](https://pypi.org/) &/or to [Conda Forge](https://conda-forge.org/). 
- [x] ~Easier way to accept BCS login credentials and to save or update them across application uses.~
- [x] ~Allows user to select which course(s) to return data on, if multiple courses tied to single account.~
    - Only allows selection of one course at a time.
- [x] Saves and opens PDF report on course metrics in users default browser (see above).
    - [ ] Univariate & Multivariate forecasting students potential performance.
        - [ ] Use NLP for sentiment analysis on feedback using IBM [Tone Analyzer](https://cloud.ibm.com/catalog/services/tone-analyzer). 
- [ ] Improve documentation.
    - Use dummy data to create visuals for repo, doc, and video info.
    - Read the Docs.
    - Github Pages.
- [ ] Suggestions

## Instructions
Enter in your login credentials to [bootcampspot.com](https://bootcampspot.com) in the [DELETE_THIS_PLACE_HOLDER.env](DELETE_THIS_PLACE_HOLDER.env) file, save it and delete the prefix.

In a python/conda terminal execute the following command:
```
python testscript.py
```

<sub>If needed use this script to create a new conda env and install the necessary dependencies:
```
conda create --name bcsenv python=3.7 -y
conda activate bcsenv
conda install -c anaconda requests -y
conda install -c anaconda pandas -y
conda install -c conda-forge matplotlib -y
conda install -c conda-forge python-dotenv -y
conda install -c conda-forge pysimplegui -y
```
</sub>


## Additional Info
See [docs for BCS api](https://bootcampspot.com/instructor-api-docs).
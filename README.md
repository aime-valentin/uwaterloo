# Most Activiely Modified Modules of the OpenStack Nova Project

By running this program, a report is created that summarizes the 12 most actively modified modules of OpenStack Nova Project from the last six months.
All the activies within a module have been aggregated to the module level. Example of the indicators used in this program include:

  - A number of commits occured during the studied period
  - The extent of churn occured during hte studied period

*Note*: Churn is defined as the sum of added and removed lines by all commits

# Running the program  

```
#in your command line
> git clone <link-to-this-repo>
> conda install -r requirements.txt #assumes that you alread have anaconda installed]
> cd uwaterloo
> python3 ./scripts/nova.py
```

#Important Libraries
If conda install fails, you might want to install the following libraries using pip3
pandas    --version 1.4.1
pydriller --version 2.1
seaborn   --version 0.11.2
tqdm      --version 4.63.0
numpy     --version 1.21.2

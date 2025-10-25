#Steps for tackling extended heatmap question in Assignment

## Creating Conda Environment
1. In Terminal , conda create environment 

```
conda create -n coach_2
```
Note: "coach_2" is the name of the environment. Up to you on how you want to name it

2.  Head over to the working folder and activate environment

```
conda activate <conda_environment_name>
```

3. Start installing packages. For this case, it will be

```
conda install numpy pandas matplotlib seaborn
```

4. Once done, export the environment. So that way you will have something to fall back on if the environment gets corrupted or something.

```
conda env export --no-build- --from-history- > environment.yml  
```
Note - 
--no-build- removes the build version of the packages. Aim is to have a cleaner .yml file
--from-history- indicate only the packages that you explicitly installed. Aim is also to have a cleaner .yml file
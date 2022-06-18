## Start Machine-Learnig-Project

## Software and Account Requirements

1. [Github Account](http://github.com)
2. [Heroku Account](https://dashboard.heroku.com)
3. [VS code IDE](https://code.visualstudio.com/download)
4. [GIT CLI](https://git-scm.com/downloads)


Creating virtual enviournment
```
conda create -p venv python == 3.7 -y 
```
```
conda activate venv/
```

```
pip install -r requirements.txt
```

To add files to git

```
git add .
```
OR 

```
git add <filename>
```

> Note: To ignore filename or folder from git we can add that file/folder name in .gitignore file


To check the git status 
```
git status
```

To create version/commit all changes by git 
```
git commit -m "message"
```

To send the version/changes to github
```
git push origin main
```

To check remote URL
```
git remote -v
```


To setup CI/CD pipeline in heroku, we need 3 information

1. Heroku email = pbaliyan1992@gmail.com
2. Heroku_api_key = d47f4155-38a3-4403-ad00-c8eb605a7f0a
3. Heroku app name = ml-regression-appli


Buid docker image 
```
docker build -t <image_name>:<tag_name>
```

To list docker image
```
docker images
```

To run docker image
```
docker run -p 5000:5000 -e PORT=5000 <imageid>
```

```
python setup.py install
```
git clone https://github.com/Prathyusha16/learnpython.git
cd learnpython/
ls -ltra
### Add a new python file and use below command to add it to git
git add *
### check the status now you should see the added file
git status
### commit the file to your local git repo
git commit -m 'added new chapter'
### Below is one time configuration to configure. This needed not be done everytime
git config --global user.name "Prathyusha16"
git config --global user.email "parasaramchinnu@gmail.com"
### Now that you have your changes commited to local git repo if you are ready you could push them to origin (github.com)
git push origin main

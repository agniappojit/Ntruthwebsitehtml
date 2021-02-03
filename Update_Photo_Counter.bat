git clone "https://github.com/agniappojit/Ntruthwebsitehtml.git"
Update_Photo_Counter.py
cd Ntruthwebsitehtml
git add index.html
git commit -m " %date% - %time% : Automatic Update of Number of Photos "
git push -u origin main
cd..
rmdir /Q /S Ntruthwebsitehtml

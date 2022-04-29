echo "[ UNOS Assistant Framework ] Installing Dependencies"
cd Demo
pip3 install -r requirements.txt
python3 setup.py
cd ..
echo "[ UNOS Assistant Framework ] Starting UNOS Assistant"
python3 unos.py
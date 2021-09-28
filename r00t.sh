mno=$(whoami)
if [ $mno == root ]
  then
    python3 Who-is-this.py
else
    sudo python3 Who-is-this.py
fi

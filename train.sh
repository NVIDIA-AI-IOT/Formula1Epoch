export PATH=/usr/local/cuda-8.0/bin:$PATH
export LD_LIBRARY_PATH=/usr/local/cuda-8.0/lib64:$LD_LIBRARY_PATH
export LD_LIBRARY_PATH=/usr/local/cuda-8.0/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
export PATH=/usr/local/cuda-8.0/bin${PATH:+:${PATH}}
'''python SteerNet.py
python SteerNetL2.py
python SteerNetMoreConv.py
python SteerNetL2MoreConv.py'''
python SteerNetL2MoreConv64.py
'''
python SteerNetL2MoreConv3264.py
python SteerNetL264.py
python SteerNetL2Conv5.py'''
python SteerNetL2Conv564.py
'''python SteerNetL2Conv5643264.py
python SteerNetL2Conv5163264.py'''
python SteerNetL2Conv6.py
'''python SteerNetMoreConv3264.py
python SteerNetMoreConv64.py
python SteerNetL2Conv163264.py
python SteerNetL2Conv3264.py'''

echo "done"
echo "Meme machine"

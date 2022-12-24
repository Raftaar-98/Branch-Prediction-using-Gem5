#####################################################################################################################################################
#####################################################################################################################################################
#########################   Author: Shishir Sunil Yalburgi                                                           ################################
#########################   NET ID: SSY220000                                                                        ################################
#########################   Version: 2.0.1                                                                           ################################
#########################   Email ID: ssy220000@utdallas.edu                                                         ################################
#########################   This python script automates CE6304 Project 1                                            ################################
#####################################################################################################################################################
#####################################################################################################################################################





import os
import subprocess
range = {0 , 1, 2, 3}
BTB_sz = ["1024","2048","4096","8192"]
LHT_sz = ["1024","2048","4096","8192"]
CP_sz = ["1024","2048","4096","8192"]
GP_sz = ["1024","2048","4096","8192"]
LP_sz = ["1024","2048","4096","8192"]

#Output path
outpath = '/home/010/s/ss/ssy220000/P1/out/'

#Gem5 directory
Gem5dir = '/home/010/s/ss/ssy220000/P1/gem5'

#Branch predictor directory
BrnPredFile = '/home/010/s/ss/ssy220000/P1/gem5/src/cpu/pred/BranchPredictor.py'

#Simple CPU
SimpCPUFile = '/home/010/s/ss/ssy220000/P1/gem5/src/cpu/simple/BaseSimpleCPU.py'

#optfile path
optpath = '/home/010/s/ss/ssy220000/P1/gem5/build/X86/gem5.opt'

#Benchmark path
Benchpath = '/home/010/s/ss/ssy220000/P1/Project1_SPEC-master/'


def RunLocalBP(i,j):
    with open (SimpCPUFile,'r') as file:
         data = file.read()
         
    data = data.replace('BranchPredictorDummy','LocalBP()')
    with open (SimpCPUFile,'w') as file:
         file.write(data)
    
    with open (BrnPredFile,'r') as file:
         data = file.read()
         
    data = data.replace('BTB1',BTB_sz[j])
    with open (BrnPredFile,'w') as file:
         file.write(data)
  
    if i < 4:
       with open (BrnPredFile,'r') as file:
            data = file.read()
         
       data = data.replace('LP1',LP_sz[i])
       with open (BrnPredFile,'w') as file:
            file.write(data)
       with open (BrnPredFile,'r') as file:
            data = file.read()
         
       data = data.replace('LP2',LP_sz[i])
       with open (BrnPredFile,'w') as file:
            file.write(data)
       
       with open (BrnPredFile,'r') as file:
            data = file.read()
         
       data = data.replace('GP1',GP_sz[i])
       with open (BrnPredFile,'w') as file:
            file.write(data)
       with open (BrnPredFile,'r') as file:
            data = file.read()
         
       data = data.replace('GP2',GP_sz[i])
       with open (BrnPredFile,'w') as file:
            file.write(data)

       with open (BrnPredFile,'r') as file:
            data = file.read()
         
       data = data.replace('LHT1',LHT_sz[i])
       with open (BrnPredFile,'w') as file:
            file.write(data)
       with open (BrnPredFile,'r') as file:
            data = file.read()
         
       data = data.replace('CP1',CP_sz[i])
       with open (BrnPredFile,'w') as file:
            file.write(data)
       with open (BrnPredFile,'r') as file:
            data = file.read()
         
       data = data.replace('CP2',CP_sz[i])
       with open (BrnPredFile,'w') as file:
            file.write(data)
       tmp2 = i


    outpath2 = outpath + "BTB" + str(BTB_sz[j]) +"_" + str(GP_sz[i]) + "LocalBP"
   
    os.mkdir(outpath2)
    
    os.chdir(Gem5dir)
    
    subprocess.run(["scons",optpath])
    os.chdir(Benchpath)
    print("#############################################################################")
    print("####################### Compiled, now running simulation ####################")
    print("#############################################################################")
    subprocess.run(["sh","runGem5.sh"])
    subprocess.run(["sh","runGem5.sh"])
    subprocess.run(["cp","-rf","401.bzip2",outpath2])
    subprocess.run(["cp","-rf","429.mcf",outpath2])
    subprocess.run(["cp","-rf","456.hmmer",outpath2])
    subprocess.run(["cp","-rf","458.sjeng",outpath2])
    subprocess.run(["cp","-rf","470.lbm",outpath2])
    os.chdir(outpath)
    subprocess.run(["cp","-rf","BranchPredictor.py",BrnPredFile])
    subprocess.run(["cp","-rf","BaseSimpleCPU.py",SimpCPUFile])

def RunTournamentBP(i,j):
    with open (SimpCPUFile,'r') as file:
         data = file.read()
         
    data = data.replace('BranchPredictorDummy','TournamentBP()')
    with open (SimpCPUFile,'w') as file:
         file.write(data)
    
    with open (BrnPredFile,'r') as file:
         data = file.read()
         
    data = data.replace('BTB1',BTB_sz[j])
    with open (BrnPredFile,'w') as file:
         file.write(data)
    
    
    if i < 4:
       with open (BrnPredFile,'r') as file:
            data = file.read()
         
       data = data.replace('LP1',LP_sz[i])
       with open (BrnPredFile,'w') as file:
            file.write(data)
       with open (BrnPredFile,'r') as file:
            data = file.read()
         
       data = data.replace('LP2',LP_sz[i])
       with open (BrnPredFile,'w') as file:
            file.write(data)
       
       with open (BrnPredFile,'r') as file:
            data = file.read()
         
       data = data.replace('GP1',GP_sz[i])
       with open (BrnPredFile,'w') as file:
            file.write(data)
       with open (BrnPredFile,'r') as file:
            data = file.read()
         
       data = data.replace('GP2',GP_sz[i])
       with open (BrnPredFile,'w') as file:
            file.write(data)

       with open (BrnPredFile,'r') as file:
            data = file.read()
         
       data = data.replace('LHT1',LHT_sz[i])
       with open (BrnPredFile,'w') as file:
            file.write(data)
       with open (BrnPredFile,'r') as file:
            data = file.read()
         
       data = data.replace('CP1',CP_sz[i])
       with open (BrnPredFile,'w') as file:
            file.write(data)
       with open (BrnPredFile,'r') as file:
            data = file.read()
         
       data = data.replace('CP2',CP_sz[i])
       with open (BrnPredFile,'w') as file:
            file.write(data)
      


    outpath2 = outpath + "BTB" + str(BTB_sz[j]) +"_" + str(GP_sz[i]) + "TournamentBP"
   
    os.mkdir(outpath2)
    
    os.chdir(Gem5dir)
    
    subprocess.run(["scons",optpath])
    os.chdir(Benchpath)
    print("#############################################################################")
    print("####################### Compiled, now running simulation ####################")
    print("#############################################################################")
    subprocess.run(["sh","runGem5.sh"])
    subprocess.run(["sh","runGem5.sh"])
    subprocess.run(["cp","-rf","401.bzip2",outpath2])
    subprocess.run(["cp","-rf","429.mcf",outpath2])
    subprocess.run(["cp","-rf","456.hmmer",outpath2])
    subprocess.run(["cp","-rf","458.sjeng",outpath2])
    subprocess.run(["cp","-rf","470.lbm",outpath2])
    os.chdir(outpath)
    subprocess.run(["cp","-rf","BranchPredictor.py",BrnPredFile])
    subprocess.run(["cp","-rf","BaseSimpleCPU.py",SimpCPUFile])

def RunBiModeBP(i,j):
    with open (SimpCPUFile,'r') as file:
         data = file.read()
         
    data = data.replace('BranchPredictorDummy','BiModeBP()')
    with open (SimpCPUFile,'w') as file:
         file.write(data)
   
    with open (BrnPredFile,'r') as file:
         data = file.read()
         
    data = data.replace('BTB1',BTB_sz[j])
    with open (BrnPredFile,'w') as file:
         file.write(data)
    
    
    if i < 4:
       with open (BrnPredFile,'r') as file:
            data = file.read()
         
       data = data.replace('LP1',LP_sz[i])
       with open (BrnPredFile,'w') as file:
            file.write(data)
       with open (BrnPredFile,'r') as file:
            data = file.read()
         
       data = data.replace('LP2',LP_sz[i])
       with open (BrnPredFile,'w') as file:
            file.write(data)
       
       with open (BrnPredFile,'r') as file:
            data = file.read()
         
       data = data.replace('GP1',GP_sz[i])
       with open (BrnPredFile,'w') as file:
            file.write(data)
       with open (BrnPredFile,'r') as file:
            data = file.read()
         
       data = data.replace('GP2',GP_sz[i])
       with open (BrnPredFile,'w') as file:
            file.write(data)

       with open (BrnPredFile,'r') as file:
            data = file.read()
         
       data = data.replace('LHT1',LHT_sz[i])
       with open (BrnPredFile,'w') as file:
            file.write(data)
       with open (BrnPredFile,'r') as file:
            data = file.read()
         
       data = data.replace('CP1',CP_sz[i])
       with open (BrnPredFile,'w') as file:
            file.write(data)
       with open (BrnPredFile,'r') as file:
            data = file.read()
         
       data = data.replace('CP2',CP_sz[i])
       with open (BrnPredFile,'w') as file:
            file.write(data)
       


    outpath2 = outpath + "BTB" + str(BTB_sz[j]) +"_" + str(GP_sz[i])  + "BiModeBP"
   
    os.mkdir(outpath2)
    
    os.chdir(Gem5dir)
    
    subprocess.run(["scons",optpath])
    os.chdir(Benchpath)
    print("#############################################################################")
    print("####################### Compiled, now running simulation ####################")
    print("#############################################################################")
    subprocess.run(["sh","runGem5.sh"])
    subprocess.run(["sh","runGem5.sh"])
    subprocess.run(["cp","-rf","401.bzip2",outpath2])
    subprocess.run(["cp","-rf","429.mcf",outpath2])
    subprocess.run(["cp","-rf","456.hmmer",outpath2])
    subprocess.run(["cp","-rf","458.sjeng",outpath2])
    subprocess.run(["cp","-rf","470.lbm",outpath2])
    os.chdir(outpath)
    subprocess.run(["cp","-rf","BranchPredictor.py",BrnPredFile])
    subprocess.run(["cp","-rf","BaseSimpleCPU.py",SimpCPUFile])

if __name__ == "__main__":
   print("#####################################################################################")
   print("######################## Running Local BP ###########################################")
   print("#####################################################################################")
   for j in range:
        for i in range:
              RunLocalBP(i,j)

   print("#####################################################################################")
   print("######################## Running Tournament BP ######################################")
   print("#####################################################################################") 
   for j in range:
      for i in range:
            RunTournamentBP(i,j)
   print("#####################################################################################")
   print("######################## Running BiMode BP     ######################################")
   print("#####################################################################################")         

   for j in range:
      for i in range:
            RunBiModeBP(i,j)
           

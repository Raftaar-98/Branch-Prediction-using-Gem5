import os
import subprocess
range = {0 , 1 , 2 , 3}
BTB_sz = ["1024","2048","4096","8192"]
LHT_sz = ["1024","2048","4096","8192"]
CP_sz = ["1024","2048","4096","8192"]
GP_sz = ["1024","2048","4096","8192"]
LP_sz = ["1024","2048","4096","8192"]

# Output path
out = '/home/010/s/ss/ssy220000/P1/out/'

def ExtractDataLocalBP(i,j):
         outpath = out + "BTB" + str(BTB_sz[j]) +"_" + str(GP_sz[i])  + "LocalBP"
         os.chdir(outpath)
         os.chdir("401.bzip2/m5out")
         with open ("stats.txt",'r') as file2:
              line = file2.readlines()
         file1.write("BTB" + str(BTB_sz[j]) +"_" + str(GP_sz[i])  + "LocalBP")
         file1.write("\n")
         file1.write("Benchmark: 401.bzip2\n")
         file1.write(line[286])
         file1.write("\n")
         file1.write(line[254])
         file1.write("\n")
         os.chdir(outpath)
         os.chdir("429.mcf/m5out")
         with open ("stats.txt",'r') as file2:
              line = file2.readlines()
         file1.write("BTB" + str(BTB_sz[j]) +"_" + str(GP_sz[i])  + "LocalBP")
         file1.write("\n")
         file1.write("Benchmark: 429.mcf\n")
         file1.write(line[286])
         file1.write("\n")
         file1.write(line[254])
         file1.write("\n")
         os.chdir(outpath)
         os.chdir("456.hmmer/m5out")
         with open ("stats.txt",'r') as file2:
              line = file2.readlines()
         file1.write("BTB" + str(BTB_sz[j]) +"_" + str(GP_sz[i])  + "LocalBP")
         file1.write("\n")
         file1.write("Benchmark: 456.hmmer\n")
         file1.write(line[286])
         file1.write("\n")
         file1.write(line[254])
         file1.write("\n")
         os.chdir(outpath)
         os.chdir("458.sjeng/m5out")
         with open ("stats.txt",'r') as file2:
              line = file2.readlines()
         file1.write("BTB" + str(BTB_sz[j]) +"_" + str(GP_sz[i])  + "LocalBP")
         file1.write("\n")
         file1.write("Benchmark: 458.sjeng\n")
         file1.write(line[286])
         file1.write("\n")
         file1.write(line[254])
         file1.write("\n")
         os.chdir(outpath)
         os.chdir("470.lbm/m5out")
         with open ("stats.txt",'r') as file2:
              line = file2.readlines()
         file1.write("BTB" + str(BTB_sz[j]) +"_" + str(GP_sz[i])  + "LocalBP")
         file1.write("\n")
         file1.write("Benchmark: 470.lbm\n")
         file1.write(line[279])
         file1.write("\n")
         file1.write(line[247])
         file1.write("\n")
         file1.close

def ExtractDataTournamentBP(i,j):
         outpath = out + "BTB" + str(BTB_sz[j]) +"_" + str(GP_sz[i])  + "TournamentBP"         
         os.chdir(outpath)
         os.chdir("401.bzip2/m5out")
         with open ("stats.txt",'r') as file2:
              line = file2.readlines()
         file1.write("BTB" + str(BTB_sz[j]) +"_" + str(GP_sz[i])  + "TournamentBP")
         file1.write("\n")
         file1.write("Benchmark: 401.bzip2\n")
         file1.write(line[286])
         file1.write("\n")
         file1.write(line[254])
         file1.write("\n")
         os.chdir(outpath)
         os.chdir("429.mcf/m5out")
         with open ("stats.txt",'r') as file2:
              line = file2.readlines()
         file1.write("BTB" + str(BTB_sz[j]) +"_" + str(GP_sz[i])  + "TournamentBP")
         file1.write("\n")
         file1.write("Benchmark: 429.mcf\n")
         file1.write(line[286])
         file1.write("\n")
         file1.write(line[254])
         file1.write("\n")
         os.chdir(outpath)
         os.chdir("456.hmmer/m5out")
         with open ("stats.txt",'r') as file2:
              line = file2.readlines()
         file1.write("BTB" + str(BTB_sz[j]) +"_" + str(GP_sz[i])  + "TournamentBP")
         file1.write("\n")
         file1.write("Benchmark: 456.hmmer\n")
         file1.write(line[286])
         file1.write("\n")
         file1.write(line[254])
         file1.write("\n")
         os.chdir(outpath)
         os.chdir("458.sjeng/m5out")
         with open ("stats.txt",'r') as file2:
              line = file2.readlines()
         file1.write("BTB" + str(BTB_sz[j]) +"_" + str(GP_sz[i])  + "TournamentBP")
         file1.write("\n")
         file1.write("Benchmark: 458.sjeng\n")
         file1.write(line[286])
         file1.write("\n")
         file1.write(line[254])
         file1.write("\n")
         os.chdir(outpath)
         os.chdir("470.lbm/m5out")
         with open ("stats.txt",'r') as file2:
              line = file2.readlines()
         file1.write("BTB" + str(BTB_sz[j]) +"_" + str(GP_sz[i])  + "TournamentBP")
         file1.write("\n")
         file1.write("Benchmark: 470.lbm\n")
         file1.write(line[279])
         file1.write("\n")
         file1.write(line[247])
         file1.write("\n")

def ExtractDataBiModeBP(i,j):
         outpath = out + "BTB" + str(BTB_sz[j]) +"_" + str(GP_sz[i])  + "BiModeBP"
         os.chdir(outpath)
         os.chdir("401.bzip2/m5out")
         with open ("stats.txt",'r') as file2:
              line = file2.readlines()
         file1.write("BTB" + str(BTB_sz[j]) +"_" + str(GP_sz[i])  + "BiModeBP")
         file1.write("\n")
         file1.write("Benchmark: 401.bzip2\n")
         file1.write(line[286])
         file1.write("\n")
         file1.write(line[254])
         file1.write("\n")
         os.chdir(outpath)
         os.chdir("429.mcf/m5out")
         with open ("stats.txt",'r') as file2:
              line = file2.readlines()
         file1.write("BTB" + str(BTB_sz[j]) +"_" + str(GP_sz[i])  + "BiModeBP")
         file1.write("\n")
         file1.write("Benchmark: 429.mcf\n")
         file1.write(line[286])
         file1.write("\n")
         file1.write(line[254])
         file1.write("\n")
         os.chdir(outpath)
         os.chdir("456.hmmer/m5out")
         with open ("stats.txt",'r') as file2:
              line = file2.readlines()
         file1.write("BTB" + str(BTB_sz[j]) +"_" + str(GP_sz[i])  + "BiModeBP")
         file1.write("\n")
         file1.write("Benchmark: 456.hmmer\n")
         file1.write(line[286])
         file1.write("\n")
         file1.write(line[254])
         file1.write("\n")
         os.chdir(outpath)
         os.chdir("458.sjeng/m5out")
         with open ("stats.txt",'r') as file2:
              line = file2.readlines()
         file1.write("BTB" + str(BTB_sz[j]) +"_" + str(GP_sz[i])  + "BiModeBP")
         file1.write("\n")
         file1.write("Benchmark: 458.sjeng\n")
         file1.write(line[286])
         file1.write("\n")
         file1.write(line[254])
         file1.write("\n")
         os.chdir(outpath)
         os.chdir("470.lbm/m5out")
         with open ("stats.txt",'r') as file2:
              line = file2.readlines()
         file1.write("BTB" + str(BTB_sz[j]) +"_" + str(GP_sz[i])  + "BiModeBP")
         file1.write("\n")
         file1.write("Benchmark: 470.lbm\n")
         file1.write(line[279])
         file1.write("\n")
         file1.write(line[247])
         file1.write("\n")


if __name__ == "__main__":
   file1 = open ("results.txt",'w')
   for i in range:
       for j in range:
           ExtractDataLocalBP(i,j)
           
   for i in range:
       for j in range:
           ExtractDataTournamentBP(i,j)
           
   for i in range:
       for j in range:
           ExtractDataBiModeBP(i,j)
                  
   file1.close()      
         

    
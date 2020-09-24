import numpy as np

aa = ['R','H','K','D','E','S','T','N','Q','A','V','L','I','M','F' ,'Y', 'W', 'C','G','P']

def open_lakshims_files(predictions_file, sm_file=None):
    '''
    This is for opening files for a single protein.
    '''
    
    prot = {'sequence':'', 'predictions':[]}

    # read file with predictions
    with open(predictions_file,'r') as f:
        while True:
            try: 
                line = next(f)
                if not line[0].isdigit(): continue
        
                pos, res_type, _, pred = line.split(",")[:4]
                prot['sequence'] +=res_type
                prot['predictions'].append(pred)
                      
            except StopIteration:
                break    
    
    # info for heatmaps is in sm file, if exists. Here we initialize the dict.
    prot['heatmaps'] = {n:[] for n in range(len(prot['sequence'])+1)}

    if sm_file is None:
        return prot

    # read sm file
    flag=0
    with open(sm_file,'r') as f:
        while True:
            try: 
                line = next(f)
                if line[0] == ">":
        
                    if flag:
                        prot['heatmaps'][position] = arr[::-1]

                    position = int(line[1:-1])
                    arr = np.zeros(shape=(20,30))
    
                else:
                    line = line.strip().split(",")
                    if line[0] in aa:
                        arr[aa.index(line[0])] = np.array(line[1:])
                    flag=1
    
            except StopIteration:
                prot['heatmaps'][position] = arr
                break

    return prot

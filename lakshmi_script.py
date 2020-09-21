def open(predictions_file, sm_file):
    '''
    This is for opening files for a single protein.
    '''
    
    # read file with predictions
    prot = {'sequence':'', 'predictions':[], 'heatmap':{}}
    with open('predictions_file','r') as f:
        while True:
            try: 
                line = next(f)
                if not line[0].isdigit(): continue
        
                pos, res_type, _, pred = line.split(",")[:4]
                prot['sequence'] +=res_type
                prot['predictions'].append(pred)
                      
            except StopIteration:
                break    

    # read sm file
    flag=0
    with open('sm_file','r') as f:
        while True:
            try: 
                line = next(f)
                if line[0] == ">":
        
                    if flag:
                        prot['heatmap'][position] = arr
                              
                    position = int(line[1:-1])
                    arr = np.zeros(shape=(20,30))
    
                else:
                    line = line.strip().split(",")
                    arr[aa.index(line[0])] = np.array(line[1:])
                    flag=1
    
            except StopIteration:
                prot['heatmap'][position] = arr
                break


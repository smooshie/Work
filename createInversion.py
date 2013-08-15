'''
Created on 11.1.2013

@author: 

            ::.
      (\./)  .-""-.
       `\'-'`      \
         '.___,_^__/

     * Whale whale whale, what have we here?

'''

def rc(reversable):
    complement = { "A" : "T", "T" : "A", "C" : "G", "G" : "C"}
    result = "" 
    for i in reversed(reversable): 
        result += complement[i]
    
    return result

def main():
    seq = []
    with open("human_relative.fas", 'rU') as f:
        for line in f:
            line.rstrip('\r\n')
            if line[0] != ">":
                for i in line:
                    if i != '\n':
                        seq.append(i)
    
    indexes = open("indexes.txt", "w")
    for i in range (1, 2000000):
        if i % 10000 == 0:
            reversd = rc(seq[i:i+30])
            indexes.write("from " + str(i) + " took " + str(seq[i:i+30]) + " --> " + str(i-200) + "-" + str(i-180) + " inserted " + reversd + " \n")
            seq.pop(i-200)
            seq.pop(i-190)
            seq.insert(i-210, reversd)
        
    
    done = open("human_altered.fas", "w")
    
    done.write(''.join(seq))
                    

main()
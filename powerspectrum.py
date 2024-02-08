import numpy as np
import os

def write_ps(file_name,p_name,p_value,reio_model="reio_camb",verbose=True,root=" "):#能行
    '''
    write power spectrum for tanh and exp model
    file_name: *.ini
    p_name: the additional parameters
    p_value: the value of the additional parameters
    reio_model: the reionization model: only tanh and exp model
    verbose: whether need to print the thermodynamics paramters
    root: output root
    '''
    if root==" ":
        root='output/'+file_name
    content=['output=pCl,lCl\n','modes=s,t\n','reio_parametrization='+reio_model+'\n','lensing=yes\n','root='+root+'\n']
    if verbose==True:
        content.append('thermodynamics_verbose=1\n')
    with open(file_name+".ini",'w') as f:
        for i in range(len(content)):
            f.write(content[i])
        for i in range(len(p_name)):
            f.write(p_name[i]+'='+str(round(p_value[i],10))+'\n')

def write_ps_many(p_name,p_value,redshift,xe,file_name="check.ini",verbose=True,root="output/check"):#能过
    '''
    write power spectrum for many_tanh_model
    file_name: *.ini
    p_name: the additional parameters !!don't forget the r!
    p_value: the value of the additional parameters
    redshift: redshift of random points
    xe: xe of random points
    verbose: whether need to print the thermodynamics paramters
    root: output root
    '''
    content=['output=pCl,lCl\n','modes=s,t\n','reio_parametrization=reio_many_tanh\n','lensing=yes\n','root='+root+'\n']
    if verbose==True:
        content.append('thermodynamics_verbose=1\n')
    with open(file_name,'w') as f:
        for i in range(len(content)):
            f.write(content[i])
        for i in range(len(p_name)):
            f.write(p_name[i]+'='+str(round(p_value[i],10))+'\n')
        f.write("many_tanh_num=")
        f.write(str(int(len(redshift)))+"\n")
        f.write("many_tanh_z=")
        for i in redshift:
                f.write(str(round(i,10))+",")
        f.seek(f.tell() - 1, os.SEEK_SET)
        f.write("\n")
        f.write("many_tanh_xe=")
        for i in xe:
                f.write(str(round(i,10))+",")
        f.seek(f.tell() - 1, os.SEEK_SET)
        f.write("\n")

def run_fit_ps(p_ranges,p_names,file_name="chi1",verbose=True,root=" "):
    j=-1
    for p1 in p_ranges[0]:
        j+=1
        p=0
        for p2 in p_ranges[1]:
            write_ps(file_name+'_'+str(j)+'_'+str(int(p/100))+'_',p_names,[p1,p2],"reio_camb",verbose,root)
            os.system('./class '+file_name+'_'+str(j)+'_'+str(int(p/100))+'_.ini')
            p+=1
    os.system("rm -rf chi1*.ini")
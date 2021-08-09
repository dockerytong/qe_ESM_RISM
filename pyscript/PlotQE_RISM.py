import numpy as np
import matplotlib.pyplot as plt
import math
from scipy import integrate

def plot_1d_rism( path = '', prefix = '', normalization = False , limx = None ):
    with open( path+'/'+prefix+'.1drism', 'r' ) as file:
      data = file.readlines()
    line_atoms = data[4].split()
    data = np.loadtxt( path+'/'+prefix+'.1drism', comments='#', skiprows = 5 )

    number_of_sublines = int( math.ceil((len(line_atoms) - 1) / 3) )
    number_of_subplots = len( line_atoms ) - 1

    fig = plt.figure(
          figsize=(8, 6),  # inch
    )
    plt.rcParams["font.size"] = 20
    plt.rcParams['font.family'] = 'Times New Roman'
    plt.rcParams['mathtext.fontset']='stix'

    fact = 1
    fig.subplots_adjust(wspace=0.5, hspace=0.8)
    ax = fig.add_subplot(111)
    ax.set_xlabel( r'$r$ [$\mathrm{\AA}$]' )
    ax.set_xlim(0,limx)
    ax.set_ylabel( r'$g(r)$' )
    #ax.plot( data[:,0], data[:,1], label = line_atoms[1], linestyle = 'solid' )

    for i in range( 1, number_of_subplots + 1 ):
      ax.set_xlabel( r'$r$ [$\mathrm{\AA}$]' )
      ax.set_xlim(0,limx)
      ax.set_ylabel( r'$g(r)$' )
      ax.plot( data[:,0], data[:,i], label = line_atoms[i], linestyle = 'solid' )

#    for i in range( 1, number_of_sublines + 1 ):
#        if normalization:
#          fact = data[ -1, i ]
#
#        ax = fig.add_subplot( number_of_sublines, 3, i )
#        if limx is not None:
#          ax.set_xlim( [ 0.0, limx ] )
#        else:
#          ax.set_xlim( [ 0.0, 15.0 ] )
#
#        ax.set_xlabel( r'$r$ [$\mathrm{\AA}$]' )
#        ax.set_ylabel( r'$g(r)$' )
#
#        if ( number_of_subplots % 3 ) == 0:
#          if i <= ( number_of_subplots // 3 - 1 )*3:
#            ax.set_xlabel( '' )
#
#        ax.plot( data[:,0], data[:,i] / fact, color = 'black', label = line_atoms[i], linestyle = 'solid' )
    plt.legend(fontsize=15, ncol=2, loc='upper right', columnspacing=1)
    plt.show()


def plot_rism_NaCl_aq1( path = '', prefix = '' ):
 
      data = np.loadtxt( path+'/'+prefix+'.rism1', comments='#')

      fig = plt.figure(
            figsize=(12, 6),  # inch
            dpi=100,
      )

      fig.subplots_adjust(wspace=0.5, hspace=0.8)

      plt.rcParams["font.size"] = 15
      plt.rcParams['font.family'] = 'Times New Roman'
      plt.rcParams['mathtext.fontset']='stix'

      col=[]
      col.append('black')
      col.append('red')
      col.append('blue')
      col.append('green')
      col.append('orange')

      #ax1 = fig.add_subplot(221)
      #ax1.set_xlabel( r'$z$ [$\mathrm{\AA}$]' )
      #ax1.set_xlim(-10, 20)
      #ax1.set_ylabel( r'$\rho_{\mathrm{e}} (z)$ [e/$\mathrm{\AA}$]' )

      ax2 = fig.add_subplot(231)
      ax2.set_xlabel( r'$z$ [$\mathrm{\AA}$]' )
      ax2.set_xlim(-10,30)
      ax2.set_xticks(np.arange(-10,31,10))
      ax2.set_ylabel( r'$V (z)$ [eV]' )
      ax2.set_ylim(-10,5)

      lab2=[]
      lab2.append('solvent')
      lab2.append('solute')
      lab2.append('total')

      ax3 = fig.add_subplot(232)
      ax3.set_xlabel( r'$z$ [$\mathrm{\AA}$]' )
      ax3.set_xlim(0,20)
      ax3.set_xticks(np.arange(0,21,5))
      ax3.set_ylabel( r'$\rho_{\rm solv}(z)$ [1/$\mathrm{\AA}$] ' )

      lab3=[]
      lab3.append('O')
      lab3.append('H')
      lab3.append('Na')
      lab3.append('Cl')

      ax4 = fig.add_subplot(233)
      ax4.set_xlabel( r'$z$ [$\mathrm{\AA}$]' )
      ax4.set_xlim(0,20)
      ax4.set_ylabel( r'$\rho_{\rm solv}(z)$ [1/$\mathrm{\AA}$] ' )
      ax4.set_xticks(np.arange(0,21,5))

      #ax1.plot( data[:,0], data[:,1], color = 'black', linestyle = 'solid' )

      for i in range(2, 5):
            j=i-2
            ax2.plot( data[:,0], data[:,i], color = col[j], label = lab2[j], linestyle = 'solid' )

      for i in range(5, 9):
            j=i-5
            ax3.plot( data[:,0], data[:,i], color = col[j], label = lab3[j], linestyle = 'solid' )

      for i in range(7, 9):
            j=i-5
            ax4.plot( data[:,0], data[:,i], color = col[j], label = lab3[j], linestyle = 'solid' )

      ax2.legend(fontsize=10, ncol=1, loc='lower right', frameon = False )
      ax3.legend(fontsize=10, ncol=2, loc='upper right', columnspacing=1 , frameon = False )
      ax4.legend(fontsize=10, ncol=1, loc='upper right', columnspacing=1 , frameon = False )

      plt.show()

def plot_rism_NaCl( path = '', prefix = '', shift=0.0 ):

      data = np.loadtxt( path+'/'+prefix+'.rism1', comments='#')

      fig = plt.figure(
            figsize=(8, 6),  # inch
            dpi=100,
      )

      fig.subplots_adjust(wspace=0.5, hspace=0.8)

      plt.rcParams["font.size"] = 15
      plt.rcParams['font.family'] = 'Times New Roman'
      plt.rcParams['mathtext.fontset']='stix'

      col=[]
      col.append('black')
      col.append('red')
      col.append('blue')
      col.append('green')
      col.append('orange')

      #ax1 = fig.add_subplot(221)
      #ax1.set_xlabel( r'$z$ [$\mathrm{\AA}$]' )
      #ax1.set_xlim(-10, 20)
      #ax1.set_ylabel( r'$\rho_{\mathrm{e}} (z)$ [e/$\mathrm{\AA}$]' )

      ax2 = fig.add_subplot(231)
      ax2.set_xlabel( r'$z$ [$\mathrm{\AA}$]' )
      ax2.set_xlim(-10,30)
      ax2.set_xticks(np.arange(-10,31,10))
      ax2.set_ylabel( r'$V (z)$ [eV]' )
      ax2.set_ylim(-10,5)

      lab2=[]
      lab2.append('solvent')
      lab2.append('solute')
      lab2.append('total')

      ax3 = fig.add_subplot(232)
      ax3.set_xlabel( r'$z$ [$\mathrm{\AA}$]' )
      ax3.set_xlim(0,20)
      ax3.set_xticks(np.arange(0,21,5))
      ax3.set_ylabel( r'$\rho_{\rm solv}(z)$ [1/$\mathrm{\AA}$] ' )

      lab3=[]
      lab3.append('O')
      lab3.append('H')
      lab3.append('Na')
      lab3.append('Cl')

      ax4 = fig.add_subplot(233)
      ax4.set_xlabel( r'$z$ [$\mathrm{\AA}$]' )
      ax4.set_xlim(0,20)
      ax4.set_ylabel( r'$\rho_{\rm solv}(z)$ [1/$\mathrm{\AA}$] ' )
      ax4.set_xticks(np.arange(0,21,5))

      #ax1.plot( data[:,0], data[:,1], color = 'black', linestyle = 'solid' )

      for i in range(2, 5):
            j=i-2
            ax2.plot( data[:,0]-shift, data[:,i], color = col[j], label = lab2[j], linestyle = 'solid' )

      for i in range(5, 9):
            j=i-5
            ax3.plot( data[:,0]-shift, data[:,i], color = col[j], label = lab3[j], linestyle = 'solid' )

      for i in range(7, 9):
            j=i-5
            ax4.plot( data[:,0]-shift, data[:,i], color = col[j], label = lab3[j], linestyle = 'solid' )

      ax2.legend(fontsize=10, ncol=1, loc='lower right', frameon = False )
      ax3.legend(fontsize=10, ncol=2, loc='upper right', columnspacing=1 , frameon = False )
      ax4.legend(fontsize=10, ncol=1, loc='upper right', columnspacing=1 , frameon = False )

      plt.show()

def plot_rism_NaCl_charge( path = '', prefix = '', shift=0.0 ):

      data = np.loadtxt( path+'/'+prefix+'.rism1', comments='#')

      fig = plt.figure(
            figsize=(12, 6),  # inch
            dpi=100,
      )

      fig.subplots_adjust(wspace=0.5, hspace=0.8)

      plt.rcParams["font.size"] = 15
      plt.rcParams['font.family'] = 'Times New Roman'
      plt.rcParams['mathtext.fontset']='stix'

      col=[]
      col.append('black')
      col.append('red')
      col.append('blue')
      col.append('green')
      col.append('orange')

      ax1 = fig.add_subplot(111)
      ax1.set_xlabel( r'$z$ [$\mathrm{\AA}$]' )
      ax1.set_xlim(0, 20)
      ax1.set_ylabel( r'$\rho^{\mathrm{tot}}_{\mathrm{solv}} (z)$ [e/$\mathrm{\AA}$]' )
      ax1.plot( data[:,0], (-data[:,5]+0.5*data[:,6]+data[:,7]-data[:,8]), color = 'black', linestyle = 'solid' )

      plt.show()

def plot_bar( df, ymin, ymax ):
      fig, ax = plt.subplots(figsize=(8, 6))
      plt.rcParams["font.size"] = 15
      plt.rcParams['font.family'] = 'Times New Roman'
      plt.rcParams['mathtext.fontset']='stix'

      df.set_index('surfaces').plot.bar( 
            ax=ax
      )
      ax.set_xlabel('') 
      ax.set_ylabel('Energy [eV]')
      ax.set_ylim(ymin,ymax)
      plt.show()

def plot_1drism2(file1, xmin=0.0, xmax=20.0, ymin=0.0, ymax=4.0, nmin=1, nmax=10):

    with open( file1, 'r' ) as file:
        data=file.readlines()
    name = data[4].split()
    data = np.loadtxt(file1,comments='#',skiprows = 5 )
    ncolum=len(name)

    # Figure
    fig, ax1 = plt.subplots(
        figsize=(4, 3), # inch
        dpi =100
    )

    fig.subplots_adjust(wspace=0.5, hspace=0.8)

    plt.rcParams["font.size"] = 15
    plt.rcParams['font.family'] = 'Times New Roman'
    plt.rcParams['mathtext.fontset']='stix'

    #ax1= fig.add_subplot(111)
    ax1.set_xlabel( r'$r$ [$\mathrm{\AA}$]' )
    ax1.set_xlim(xmin,xmax)
    ax1.set_ylabel( r'$g(r)$' )
    ax1.set_ylim(ymin,ymax)
    r=data[:,0]

    for i in range (nmin, nmax):
        ax1.plot( r, data[:,i], label = name[i], linestyle = 'solid')

    ax1.legend(fontsize=10, ncol=2, loc='upper right', columnspacing=1)
    plt.grid(True)
    plt.show()


def sum_1drism():
    file1drism1='./data/H2O.NaCl_aq/H2O.NaCl_aq.1mol.1drism'
    # Load 1D-RISM data

    with open( file1drism1, 'r' ) as file:
        data = file.readlines()
    line_atoms = data[4].split()
    data = np.loadtxt( file1drism1, comments='#', skiprows = 5 )

    # Parameters
    nz=len(data[:,0])
    pi=np.pi
    bohr2angst=0.529177
    # averaged density
    rho=0.49533750E-02/(bohr2angst**3)
    rho2=0.89238936E-04/(bohr2angst**3)
    natom=4 #O:Na
    natom2=9 #Na:Cl

    y_int=[]
    y_int2=[]
    for i in range( 0, nz ):
        x=data[0:i, 0]
        y=data[0:i, natom]*4.0*pi*x[0:i]*x[0:i]*rho
        y2=data[0:i, natom2]*4.0*pi*x[0:i]*x[0:i]*rho2
        if( i > 0 ):
            inte=integrate.simps(y, x)
            inte2=integrate.simps(y2, x)
            y_int.append(inte)
            y_int2.append(inte2)
        else:
            y_int.append(0.0)
            y_int2.append(0.0)

    x=data[:, 0]
    y=data[:, natom]
    y2=data[:, natom2]

    # Definition of Figure
    fig = plt.figure(
        figsize=(4, 3),  # inch
        dpi=100,
    )

    fig.subplots_adjust(wspace=0.5, hspace=0.8)
    plt.rcParams["font.size"] = 15
    plt.rcParams['font.family'] = 'Times New Roman'
    plt.rcParams['mathtext.fontset']='stix'

    ax1 = fig.add_subplot(111)
    ln1=ax1.plot(x, y, 'C0', label=r'$g_{\rm [O:Na]}(r)$')
    ln1=ax1.plot(x, y2, 'C0', label=r'$g_{\rm [Na:Cl]}(r)$',color='red')


    ax2=ax1.twinx()
    ln2=ax2.plot(x, y_int, 'C1', label=r'$ \int \ 4 \pi  r^2 \rho_{\rm O} g_{\rm [O:Na]}(r) dr$' )
    ln2=ax2.plot(x, y_int2, 'C1', label=r'$ \int  4 \pi  r^2 \rho_{\rm Cl} g_{\rm [Na:Cl]}(r) dr$', color='green' )


    h1, l1 = ax1.get_legend_handles_labels()
    h2, l2 = ax2.get_legend_handles_labels()
    ax1.legend(h1+h2, l1+l2, fontsize=10, loc='upper right', frameon = False)


    ax1.set_xlabel(r'$r$ [$\mathrm{\AA}$]')
    ax1.set_ylabel(r'$g(r)$')
    ax2.set_ylabel(r'Integrated $g(r)$')
    ax1.set_xlim(0,10)
    ax1.set_ylim(0,12.0)
    ax2.set_ylim(0,10)

def Omega(file1, file2):

    # Load Pt data
    with open( file2, 'r' ) as file:
        data = file.readlines()
        line_labels = data[0].split()
        data = np.loadtxt( file2, comments='#', skiprows = 1 )

    # Set Pt data
        m_h2o_Pt=data[:,0] #eV
        N_h2o_Pt=data[:,1]
        A_h2o_Pt=data[:,2] #Ry
        m_h3o_Pt=data[:,3] #eV
        N_h3o_Pt=data[:,4]
        A_h3o_Pt=data[:,5] #Ry

    # Set parameters
        eV2Ry=1.0/13.6058
    Ry2eV=13.6058
    TS_H2=-0.404
    A_H2=-2.3322957476+TS_H2*eV2Ry
    Ezp_H2=0.270
    Ezp_H2O=0.562
    Ezp_H3O=0.909

    Omega_L_Pt=(A_h2o_Pt+m_h2o_Pt*N_h2o_Pt*eV2Ry+Ezp_H2O*eV2Ry)+(A_H2+Ezp_H2*eV2Ry)*0.5
    Omega_R_Pt=A_h3o_Pt+m_h3o_Pt*N_h3o_Pt*eV2Ry+Ezp_H3O*eV2Ry

    fig, (ax1, ax2, ax3) = plt.subplots(
        ncols = 3,
        figsize=(12, 4), # inch
        dpi =100
        )

    fig.subplots_adjust(wspace=0.5, hspace=0.8)

    plt.rcParams["font.size"] = 15
    plt.rcParams['font.family'] = 'Times New Roman'
    plt.rcParams['mathtext.fontset']='stix'

    ax1.set_xlabel( r'$\mu_{\rm e}^{\rm SHE}[\mathrm{vs.\Phi_S}]$' )
    ax1.set_xlim(-6.0, -5.1)
    ax1.set_xticks(np.arange(-6.0,-5.1,0.2))
    ax1.set_ylabel( r'$\Omega$ [eV]' )
    ax1.set_ylim(-0.5,0.2)

    Omega_PZC=Omega_L_Pt[1]

    ax1.plot(m_h2o_Pt, (Omega_L_Pt-Omega_PZC)*Ry2eV, label = '$\Omega_L$', linestyle = 'solid', marker='o', markersize=10 )
    ax1.plot(m_h3o_Pt, (Omega_R_Pt-Omega_PZC)*Ry2eV, label = '$\Omega_R$', linestyle = 'solid', marker='o', markersize=10 )
    ax1.legend(fontsize=10, ncol=1, loc='upper left', columnspacing=1)

    # Load Pt data
    with open( file1, 'r' ) as file:
        data = file.readlines()
        line_labels = data[1].split()
        data = np.loadtxt( file1, comments='#', skiprows = 2 )

    # Set Al data
    N_Pt=data[:,0]
    m_Pt=data[:,1] #eV
    A_Pt=data[:,2] #Ry

    Ry2eV=27.2116*0.5
    TS_H2=-0.404
    A_H2=-2.3322957476*Ry2eV+TS_H2
    A_H2O=-34.2914608381*Ry2eV
    A_H3O=-35.1019053889*Ry2eV

    Ezp_H2=0.270
    Ezp_H2O=0.562
    Ezp_H3O=0.909

    G_L=0.5*(A_H2+Ezp_H2)+A_H2O+Ezp_H2O
    G_R=A_H3O+Ezp_H3O

    PZC2=A_Pt[5]*Ry2eV+m_Pt[5]*N_Pt[5]

    Omega_Pt=(A_Pt)*Ry2eV+m_Pt*N_Pt-PZC2

    fig.subplots_adjust(wspace=0.5, hspace=0.8)
    plt.rcParams["font.size"] = 15
    plt.rcParams['font.family'] = 'Times New Roman'
    plt.rcParams['mathtext.fontset']='stix'

    ax2.set_xlabel( r'$\mu_{\rm e}^{\rm SHE}[\mathrm{vs.\Phi_S}]$' )
    ax2.set_xlim(-6.0,-5.1)
    ax2.set_xticks(np.arange(-6.0,-5.1,0.2))
    ax2.set_ylabel( r'$\Omega$ [eV]' )

    ax2.plot(m_Pt, (Omega_Pt), label = '$\Omega_{\mathrm{Pt}}$', linestyle = 'solid', marker='o', markersize=10 )
    ax2.legend(fontsize=10, ncol=2, loc='upper left', columnspacing=1)


    ax3.set_xlabel( r'$\mu_{\rm e}^{\rm SHE}[\mathrm{vs.\Phi_S}]$' )
    ax3.set_xlim(-6.0,-5.1)
    ax3.set_xticks(np.arange(-6.0,-5.1,0.2))
    ax3.set_ylabel( r'$\Omega$ [eV]' )

    ax3.plot(m_Pt, (Omega_Pt+G_L), label = '$\Omega_L$', linestyle = 'solid', marker='o', markersize=10 )
    ax3.plot(m_Pt, (Omega_Pt+m_Pt*(1.0)+G_R), label = '$\Omega_R$', linestyle = 'solid', marker='o', markersize=10 )
    ax3.plot(m_Pt, m_Pt*(1.0)+G_R, label = '$ax+b$', linestyle = 'solid', marker='o', markersize=10 )

    ax3.legend(fontsize=10, ncol=2, loc='lower right', columnspacing=1)

    plt.show()

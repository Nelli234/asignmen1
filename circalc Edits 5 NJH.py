""" circalc.py -- simplistic LCR calculator for TPRG 2131 Week 2 Asmt 1

Assignment 1 for Tprg 2131 intro week 1-2


ADD YOUR NAME, STUDENT ID and SECTION CRN here.
Nelson Hucklebridge
100614680
TPRG2131
#ready fore marking
This LCR calculator is ugly and incomplete. The code runs but doesn't actually
calculate anything. For full marks, you must complete the computation. You must
also "clean up" the code according to the course style guide and coding
standard. Specifically, you must:
  1) Take code that is duplicated and encapsulate it into a function that is
     called from the main program; the function must not "reach into" the
     main program for its working values;
  2) Rename variables so that they are not single letters, using descriptive
     names;
  3) Actually calculate the resonant frequency, bandwidth and Q factor for the
     SERIES resonant circuit (look up the formulas from ELEC II).

Keep working on the program. As you fix each problem, commit with an
informative commit message.
When done, commit with a message like "Ready for marking" and push the changes
to your assignment1 repository on the server hg.set.durhamcollege.org.
"""
import math #importing pi for required calculations
print("Series resonant circuit calculator\n(CTRL-C to quit)")



while True:
    try:
        option = input("hit q or Q too quit:")#option of quitting using q
        if option == 'q':
            break
        elif option == 'Q':
            break
        else:
            Circuit = input("is this curcuit series or parallel:")#for the option
            resonantoption = input("do you want the resonant freq yes or no")
            induct = float(input("What is the inductance in mH? "))
            while induct <= 0.0:#inductance
                induct = float(input("The value must be greater than zero\n"
                        "What is the inductance in mH? "))

            cap = float(input("What is the capacitance in uF? "))
            while cap <= 0.0:#capacitance
                cap = float(input("The value must be greater than zero\n"
                        "What is the capacitance in uF? "))

            res = float(input("What is the resistance in ohms? "))
            while res <= 0.0:#resistance
                res = float(input("The value must be greater than zero\n"
                        "What is the resistance in ohms? "))
            if Circuit == 'series':
        # Calculate the resonant frequency and the Q factor of this circuit
                freq = 1/(2*(math.pi)*(math.sqrt(induct*cap)))#resonant frequency calculation
                capreact = 1/(2*math.pi*freq*cap)#capacitive reactence
                inductreact = 2*math.pi*freq*induct#inductive reactence
                quality=inductreact/res#quality Factor
                BandWidth=freq/quality#bandwidth
                Tcons = res * cap# RC constant
    
            elif Circuit == 'parallel':
                freq = 1/(2*(math.pi)*(math.sqrt(induct*cap)))#resonant frequency calculation
                capreact = 1/(2*math.pi*freq*cap)#capacitive reactence
                inductreact = 2*math.pi*freq*induct#inductive reactence
                quality=res/(2*math.pi*freq*induct)#quality Factor
                BandWidth=freq/quality#bandwwidth
                Tcons = res * cap #RC constant
                
            
        
    # Formulas TBD
            if resonantoption =='yes':#option for resonant freq
                print("lcr:", induct, cap, res, freq, capreact, inductreact, quality, BandWidth, Tcons, "\n")
            else:
                print("lcr:", induct, cap, res, capreact, inductreact, quality, BandWidth, Tcons, "\n")  
        
    except KeyboardInterrupt: #too interrupt with ctrl-C
        print("finish")
        break

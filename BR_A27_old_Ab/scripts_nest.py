import matlab.engine



eng = matlab.engine.start_matlab()
eng.BR_A27_old(nargout=0)
eng.quit()
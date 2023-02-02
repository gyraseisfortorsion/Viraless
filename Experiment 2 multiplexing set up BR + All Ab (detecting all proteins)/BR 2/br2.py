import matlab.engine
eng = matlab.engine.start_matlab()
eng.BR_2(nargout=0)
eng.quit()

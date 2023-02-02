import matlab.engine

def implement():

    eng = matlab.engine.start_matlab()
    eng.final(nargout=0)
    eng.quit()
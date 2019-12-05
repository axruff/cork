
def convertToByte(num):
    if num >= 255:
        return 255;
    elif num < 0:
        return 0
    else:
        return num;

def convertToRGB(x, y):
	                   
	amp = 0        
	phi = 0        
	alpha = beta = 0 
                          
        
    #//----------------------------------
    #    // ATTENTION: Colors could be inverted!
    #    //----------------------------------
        
    #    //x = -x;
    #    //y = -y;

	 # determine amplitude and phase (cut amp at 1) */
	amp = math.sqrt (x * x + y * y);

	if amp > 1: 
        amp = 1;

	if x == 0.0:
        if y >= 0.0: 
            phi = 0.5 * PI;
		else: 
            phi = 1.5 * PI;

	elif x > 0.0:
		if y >= 0.0:
            phi = atan (y/x);
		else:
            phi = 2.0 * PI + atan (y/x);
	elif:
        phi = PI + atan (y/x);

	phi = phi / 2.0;

	#// interpolation between red (0) and blue (0.25 * Pi)
	if (phi >= 0.0) and (phi < 0.125 * PI):
		beta  = phi / (0.125 * PI);
		alpha = 1.0 - beta;
		r = math.floor(amp * (alpha * 255.0 + beta * 255.0));
		g = math.floor(amp * (alpha *   0.0 + beta *   0.0));
		b = math.floor(amp * (alpha *   0.0 + beta * 255.0));
	
	if (phi >= 0.125 * PI) and (phi < 0.25 * PI):
		beta  = (phi-0.125 * PI) / (0.125 * PI);
		alpha = 1.0 - beta;
		r = math.floor(amp * (alpha * 255.0 + beta *  64.0));
		g = math.floor(amp * (alpha *   0.0 + beta *  64.0));
		b = math.floor(amp * (alpha * 255.0 + beta * 255.0));
	

	#// interpolation between blue (0.25 * Pi) and green (0.5 * Pi)
	if (phi >= 0.25 * PI) and (phi < 0.375 * PI):
		beta  = (phi - 0.25 * PI) / (0.125 * PI);
		alpha = 1.0 - beta;
		r = math.floor(amp * (alpha *  64.0 + beta *   0.0));
		g = math.floor(amp * (alpha *  64.0 + beta * 255.0));
		b = math.floor(amp * (alpha * 255.0 + beta * 255.0));
	
	if (phi >= 0.375 * PI) and (phi < 0.5 * PI):
		beta  = (phi - 0.375 * PI) / (0.125 * PI);
		alpha = 1.0 - beta;
		r = math.floor(amp * (alpha *   0.0 + beta *   0.0));
		g = math.floor(amp * (alpha * 255.0 + beta * 255.0));
		b = math.floor(amp * (alpha * 255.0 + beta *   0.0));


	#// interpolation between green (0.5 * Pi) and yellow (0.75 * Pi)
	if (phi >= 0.5 * PI) && (phi < 0.75 * PI):
		beta  = (phi - 0.5 * PI) / (0.25 * PI);
		alpha = 1.0 - beta;
		r = math.floor(amp * (alpha * 0.0   + beta * 255.0));
		g = math.floor(amp * (alpha * 255.0 + beta * 255.0));
		b = math.floor(amp * (alpha * 0.0   + beta * 0.0));

	#// interpolation between yellow (0.75 * Pi) and red (Pi)
	if (phi >= 0.75 * PI) && (phi <= PI):
		beta  = (phi - 0.75 * PI) / (0.25 * PI);
		alpha = 1.0 - beta;
		r = math.floor(amp * (alpha * 255.0 + beta * 255.0));
		g = math.floor(amp * (alpha * 255.0 + beta *   0.0));
		b = math.floor(amp * (alpha * 0.0   + beta *   0.0));


	return color(convertToByte(r), convertToByte(g), convertToByte(b));

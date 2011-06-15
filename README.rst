Signaturepad 2 Image Utility for Python
(c.) Alan Viars - Videntity Systems Inc. - 2011

This library is dual licensed.  It is realeased under the GPL licnese 
agreement and under a commercial license by Videntity systems Inc if 
you seek support or a non-free license. This library is designed to 
work with the JQuery Plugin, SigntaurePad , from Thomas J. Bradley.

http://thomasjbradley.ca/lab/signature-pad

REQUIREMENTS:
=============

Python Imaging Library (PIL) is required to use this package.
Install PIL with the following command:
::
	sudo pip install PIL

..or if you don't have PIP installed you can install it with
::
	sudo easy_install PIL

INSTALL sigpad2image:
=====================

Use easy_install to install the program.
::
	cd python-sigpad2image	
	sudo easy_install setup.py install

USING sigpad2image:
===================
The package has two functions: 's2if' and 's2i'. s2if writes the resulting image to a file.  
s2i returns an image object. s2i is ideal for most web applications where you are returning
an image to the browser. 

s2if 
-----
Action: Creates an image from the JSON string and writes it to a file.

Requires: 
~~~~~~~~~
* jsonsig - The JSON representing the signature.
* output_image- The path to the default image. Default="signature.png", 
* input_image-  The path to the input image. Default="blanksig.png",
* pin_color - the ink's color. Default=(0,0,255).  This is blue.

Returns:
~~~~~~~
* str - Astring containing the output image path.

Example:
~~~~~~~~~
A simple example using straigh-up python.
::
	from sigpad2image.sigpad2image import s2if

	j="""[{"lx":32,"ly":13,"mx":32,"my":12}..."""
	image_path=s2if(j, output_image)
	print "New signature image written to: %s " % (image_path)

s2i
---
Action: Return an image from the JSON string.  If it fails or if, force_no_sig_image=True
then it returns nosig_image, which by default is an image with the text "No Signature".

Requires: 
~~~~~~~~~
* jsonsig - The JSON representing the signature.
* output_image- The path to the default image. Default="signature.png", 
* input_image-  The path to the input image. Default="blanksig.png",
* pin_color - the ink's color. Default=(0,0,255).  This is blue.
* force_no_sig_image - Setting this to true will force the return of the no_sig image. Default=False.
* nosig_image- The image to return if no JSON is found.   Default="nosig.png"

Returns:
~~~~~~~
* An Image object. If successful it will contain an image of the signature.  If an error orccurs 
or the force_no_sig_image is set to True, it will return the nosig_image.


Example (In Django):
~~~~~~~~~~~~~~~~~~~~
Thhis illustrates building the image and returning it as an HTTP response.  
This illustration is a django view. Note the vaiables NO_SIG_IMAGE and
BLANK_SIG_IMAGE are being imported from the settings file.
:: 

	from sigpad2image.sigpad2image import s2i
	from django.http import HttpResponse
	from models import Signature
	from django.conf import settings

	def render_signature(request, user_id):
		#create a response objects and set its mimetype to image/png
    		response = HttpResponse(mimetype="image/png")
    		try:
			#Get the JSON Signature from the database        		
			s=Signature.objects.get(user=user_id)
			#build the new image
			image = s2i(s.signature, input_image=settings.BLANK_SIG_IMAGE)
        	except(Signature.DoesNotExist):
			#If it wasn't in the database, then return the nosig image
        		image = s2i("", force_no_sig_image=True, nosig_image=settings.NO_SIG_IMAGE)
		#return the HttpResponse object to the client.    		
		image.save(response, "PNG")
    		return response


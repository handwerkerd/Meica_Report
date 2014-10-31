#!/usr/bin/env python
"""
Gutierrez, B.  Contains all functions for creating the figures
of the mecia report
"""
import matplotlib as mpl
mpl.use('Agg')

from matplotlib.colors import LinearSegmentedColormap
from numpy.core.umath_tests import inner1d
from matplotlib.ticker import MaxNLocator
from matplotlib import gridspec
import matplotlib.pyplot as plt
import nibabel as ni
import numpy as np
import subprocess
import sys
import ast
import os

#frequently used green yellow red color map
cdict = {'red':  			((0.0,  0.0, 0.0),
						    (0.2, 0.6, 0.6),
						    (0.35, 0.9, 0.9),
						    (0.5, 1.0, 1.0),
		                    (1.0, 1.0, 1.0)),

		         'green':   ((0.0, 1.0, 1.0),
		         		    (0.5, 1.0, 1.0),
		         		    (0.65, 0.9, 0.9),
		                    (0.9, 0.5, 0.5),
		                    (1.0, 0.0, 0.0)),

		         'blue':    ((0.0, 0.0, 0.0),
		                    (1.0, 0.0, 0.0))
		        }

GYR = LinearSegmentedColormap('GYR', cdict)
"""
Check that the MNI coordinates of the ROI's are within the image MNI range
ROI: array of MNI coordinates
setname: path of directory containing the TED directory
description: string describing ROI to be ouputted to the user
"""
def check_ROI(ROI, TED, description):
	fails = 0
	if ROI != []:
		beta = ni.load('%s/betas_hik_OC.nii' % TED).get_data()
		beta_hdr = ni.load('%s/betas_hik_OC.nii' % TED).get_header()
		corners = np.zeros((3,1,2))
		cord_matrix = beta_hdr.get_best_affine()[0:3,0:3]
		corners[:,:,0] = np.array([[beta_hdr['qoffset_x']], [beta_hdr['qoffset_y']], [beta_hdr['qoffset_z']]])
		corners[:,:,1] = np.dot(cord_matrix,np.array([[beta.shape[0]],[beta.shape[1]],[beta.shape[2]]])) + corners[:,:,0]
		for i in range(len(ROI)):
			if ROI[i][0]<corners[0,0,0] or ROI[i][0]> corners[0,0,1]:
				fails += 1
			if ROI[i][1]<corners[1,0,0] or ROI[i][1]> corners[1,0,1]:
				fails += 1
			if ROI[i][2]<corners[2,0,0] or ROI[i][2]> corners[2,0,1]:
				fails += 1
	if fails != 0:
		print '*+ EXITING.  MNI coordinates (%s,%s,%s) not within bounds of image' % (ROI[i][0],ROI[i][1],ROI[i][2])
		sys.exit()
	else:
		print '++ %s MNI coordinates within image bounds' % description
"""
Make a figure of the FFT for the ICA component across the time series
series: path to time series data
i: integer component number
N: string component number with zeros in front to make all component numbers all the same length
startdir: string starting directory path
setname: path of directory containing the TED directory
TED: TED directory from tedana.py
"""
def FFT(TED, series, i, N):
	path = '%s/betas_OC.nii' % TED
	p = subprocess.Popen(['3dinfo','-tr', path], stdout = subprocess.PIPE, stderr = subprocess.PIPE)# retrieve TR
	TR, err = p.communicate()

	sample = np.loadtxt(series)
	t = sample[:,i]

	FFT = abs(np.fft.fft(t))
	FFT = np.fft.fftshift(FFT)
	
	freq = np.fft.fftfreq(t.size,float(TR[:-2]))# Replace '1.6'  with the correct TR .
	freq = np.fft.fftshift(freq)
	fig = plt.figure(figsize= (8,4))
	gs1 = gridspec.GridSpec(1,1)
	if (t.size % 2) ==0:
		plt.plot(freq[t.size/2:],FFT[t.size/2:])

	else:
		plt.plot(freq[(t.size+1)/2:],FFT[(t.size+1)/2:])
	plt.title('FFT of the Time Series', fontsize = 15)
	plt.xlabel('Frequency(Hz)' , fontsize = 15)
	plt.ylabel('Amplitude' , fontsize = 15)
	fig.subplots_adjust(bottom = 0.15, top = .90)
	plt.savefig('FFT_Component_' + N)
	plt.close()
"""
Seperates the components into their respective bins.
TED: TED directory from tedana.py
returns component numbers from accepted, rejected, middle kappa, and ignored bin along with their kappa, rho, and variance explained
"""
def components(TED):
	accept_ = np.array(ast.literal_eval('['+ open('%s/accepted.txt' % TED).readline() + ']'))
	reject_ = np.array(ast.literal_eval('['+ open('%s/rejected.txt' % TED).readline() + ']'))
	middle_ = np.array(ast.literal_eval('['+ open('%s/midk_rejected.txt' % TED).readline() + ']'))
	ignore_ = []
	ctab = np.loadtxt('%s/comp_table.txt' % TED)
	for i in ctab[:,0]:
		if not((int(i) in accept_) or (int(i) in reject_) or (int(i) in middle_)):
			ignore_.append(int(i))
	accept = np.zeros(shape = (len(accept_),5))
	reject = np.zeros(shape = (len(reject_),5))
	middle = np.zeros(shape = (len(middle_),5))
	ignore = np.zeros(shape = (len(ignore_),5))

	a = b = c = d = 0
	for i in ctab[:,0]:
		if i in accept_:
			accept[a,:] = ctab[i,:]
			a = a + 1
		elif i in reject_:
			reject[b,:] = ctab[i,:]
			b = b + 1
		elif i in middle_:
			middle[c,:] = ctab[i,:]
			c = c + 1
		elif i in ignore_:
			ignore[d,:] = ctab[i,:]
			d = d + 1

	return (accept,reject,middle,ignore)
"""
Removes two dimensional slices from 3d matrix image that contain all zero elements
image: three dim array
axis: axial that the two dimensional plane fixes, i.e. (0,1) fixes z
"""
def mask(image, axis):
	im_mask = np.zeros(image.shape)
	image[np.isnan(image)] = 0
	im_mask[image != 0] = 1
	lower = 0
	upper = 0
	if axis == (0,1):
		im_mask = np.sum(im_mask, axis = 0)
		im_mask = np.sum(im_mask, axis = 0)
		i = im_mask[0]
		j = im_mask[im_mask.shape[0]-1]
		while i == 0:
			lower += 1
			i = im_mask[lower]
		while j == 0:
			upper += 1
			j = im_mask[im_mask.shape[0]-1-upper]
		return (image[:,:,im_mask > 0], lower,im_mask.shape[0]-1-upper)
	if axis == (1,2):
		im_mask = np.sum(im_mask, axis = 1)
		im_mask = np.sum(im_mask, axis = 1)
		i = im_mask[0]
		j = im_mask[im_mask.shape[0]-1]
		while i == 0:
			lower += 1
			i = im_mask[lower]
		while j == 0:
			upper += 1
			j = im_mask[im_mask.shape[0]-1-upper]
		return (image[im_mask > 0,:,:],lower,im_mask.shape[0]-1-upper)
	if axis == (0,2):
		im_mask = np.sum(im_mask, axis = 0)
		im_mask = np.sum(im_mask, axis = 1)
		i = im_mask[0]
		j = im_mask[im_mask.shape[0]-1]
		while i == 0:
			lower += 1
			i = im_mask[lower]
		while j == 0:
			upper += 1
			j = im_mask[im_mask.shape[0]-1-upper]
		return (image[:,im_mask > 0,:],lower,im_mask.shape[0]-1-upper)
"""
set up floodfill algorithm.  acts as a clustering algorithm.  x,y,z designates where to begin algorithm in matrix
matrix: 2D array
x: integer index of matrix
y: integer index of matrix
z: integer index of matrix
"""
def flood(matrix, x, y, z, flood_num):
	N = 0
	itemindex = [[],[],[]]
	original = matrix.copy()
	N = floodfill(matrix, x, y, z, N, itemindex, flood_num)
	if N >= flood_num: #
		return original
	else:
		return matrix
"""
Rest of the flood fill algorithm.
itemindex: array containing location of non-zero elements of matrix next to (x,y,z)
"""
def floodfill(matrix, x, y, z, N, itemindex, flood_num):
	itemindex[0] = itemindex[0][1:len(itemindex[0]) + 1]
	itemindex[1] = itemindex[1][1:len(itemindex[0]) + 1]
	itemindex[2] = itemindex[2][1:len(itemindex[0]) + 1]
	N += np.sum(matrix[max(x-1,0):min(x+2,matrix.shape[0]),max(y-1,0):min(y+2,matrix.shape[1]),max(z-1,0):min(z+2,matrix.shape[2])])
	if N <= flood_num -1:
		matrix[x,y,z] = 0
		test = np.where(matrix[max(x-1,0):min(x+2,matrix.shape[0]-1),max(y-1,0):min(y+2,matrix.shape[1]-1),max(z-1,0):min(z+2,matrix.shape[2]-1)] == 1)
		itemindex[0].extend(test[0]+ x + (2 - (min(x+2,matrix.shape[0]) - max(x - 1,0)))) #(2-...) is a fudge factor for being on the edge of the matrix
		itemindex[1].extend(test[1]+ y + (2 - (min(y+2,matrix.shape[1]) - max(y - 1,0))))
		itemindex[2].extend(test[2]+ z + (2 - (min(z+2,matrix.shape[2]) - max(z - 1,0))))
		matrix[max(x-1,0):min(x+2,matrix.shape[0]),max(y-1,0):min(y+2,matrix.shape[1]),max(z-1,0):min(z+2,matrix.shape[2])] = 0
		if len(itemindex[0])>0:#ensures that if no more 1's around (x,y,z) not calling function again
			N = floodfill(matrix,itemindex[0][0],itemindex[1][0],itemindex[2][0], N, itemindex, flood_num)
	return N
"""
Collects data from the anatomical, overlay, and threshold data sets.  
Also collects the header from the anatomical and overlay.
anatomical: path to anatomical image
overlay: path to overlay mefl.nii.gz 
threshold_map: path to feats_OC2.nii
"""
def collect_data(startdir,label,TED,anatomical, overlay, threshold_map):
	tsoc = '%s/ts_OC.nii' % TED
	medn = '%s/dn_ts_OC.nii' % TED
	subprocess.call('3daxialize -overwrite -prefix %s/%s/axialized_nifti/tsoc.nii.gz %s' % (startdir,label,tsoc), shell = True)
	subprocess.call('3daxialize -overwrite -prefix %s/%s/axialized_nifti/medn.nii.gz %s' % (startdir,label,medn), shell = True)
	subprocess.call('3daxialize -overwrite -prefix %s/%s/axialized_nifti/mefl.nii.gz %s' % (startdir,label,overlay), shell = True)
	overlay = '%s/%s/axialized_nifti/mefl.nii.gz' % (startdir,label)
	overlay = ni.load(overlay)
	overlay_data = overlay.get_data()
	overlay_hdr = overlay.get_header()
	overlay_quat = overlay_hdr.get_qform_quaternion()

	if anatomical != '':
		anat_name = anatomical[len(os.path.dirname(anatomical))+1:]
		subprocess.call('3daxialize -prefix %s/%s/axialized_nifti/%s %s' % (startdir,label,anat_name,anatomical), shell = True)
		anatomical = ni.load('%s/%s/axialized_nifti/%s' % (startdir,label,anat_name))
		anat_data = anatomical.get_data()
		anat_hdr = anatomical.get_header()
		anat_quat = anat_hdr.get_qform_quaternion()
		anat_orient = np.zeros(shape = (3,2))

		overlay_corners = np.zeros((3,1,2))
		anat_corners = np.zeros((3,1,2))

		overlay_R, overlay_q_fac = Rotation_matrix(overlay_hdr.get_qform_quaternion())
		overlay_corners[:,:,0] = np.array([[overlay_hdr['qoffset_x']] ,[overlay_hdr['qoffset_y']], [overlay_hdr['qoffset_z']]])# calculate extremes of overlay
		overlay_corners[:,:,1] = (np.dot(overlay_R,np.array([[overlay.shape[0]*overlay_hdr['pixdim'][1]], [overlay.shape[1]*overlay_hdr['pixdim'][2]],
			[overlay_q_fac*overlay.shape[2]*overlay_hdr['pixdim'][3]]])) + overlay_corners[:,:,0])

		anat_R, anat_q_fac = Rotation_matrix(anat_hdr.get_qform_quaternion())
		anat_corners[:,:,0] = np.array([[anat_hdr['qoffset_x']], [anat_hdr['qoffset_y']], [anat_hdr['qoffset_z']]])
		anat_corners[:,:,1] = (np.dot(anat_R,np.array([[anatomical.shape[0]*anat_hdr['pixdim'][1]], [anatomical.shape[1]*anat_hdr['pixdim'][2]], 
			[anat_q_fac*anatomical.shape[2]*anat_hdr['pixdim'][3]]])) + anat_corners[:,:,0])
	else:
		anat_data = ''
	 	anat_corners = ''
	 	overlay_corners = ''
	if threshold_map != '':
		subprocess.call('3daxialize -overwrite -prefix %s/%s/axialized_nifti/betas.nii.gz %s' % (startdir,label,threshold_map), shell = True)
		threshold_map = '%s/%s/axialized_nifti/betas.nii.gz' % (startdir,label)
		threshold = ni.load(threshold_map)
		threshold_data = threshold.get_data()
	else:
		threshold = ''
		threshold_data = ''
	return(anat_data, overlay_data, threshold_data, anat_corners, overlay_corners)
"""
Calculate the rotaion matrix for image alignment.  Uses the coordinates already associated with dataset and anatomical
"""
def Rotation_matrix(quaternion):
	R = ni.quaternions.quat2mat(quaternion).astype('float64')
	if np.linalg.det(R) == -1:
		q_fac = -1
	else:
		q_fac = 1

	return(R, q_fac)
"""
Creates a montage of greyscale 10 images of axial, Sagittal and coronal views of meica components along with a time series of the component.
accepted components also get overlayed onto the anatomical image and floodfill is performed on statiscially significant voxels.
maps: array of 5 elements [anat dataset, mefl dataset, feats dataset, anat header, overlay header]
accept: array accepted components
threshold: float statiscial threshold
alpha: float alpha blending value
series: string meica_mix.1D path
Axial: true or false. plot axial or not
Sagittal: true or false. plot sagittal or not
Coronal: true or false. plot coronal or not
"""
def montage(maps, accept, threshold, alpha, TED, Axial, Sagittal, Coronal, flood_num, contrast):
	series = '%s/meica_mix.1D' % TED
	anat = maps[0]
	overlay = maps[1]
	threshold_data = maps[2]
	anat_corners = maps[3]
	overlay_corners = maps[4]
	l = 0
	for i in range(overlay.shape[3]):
		N = str(i)
		while len(N) < len(str(overlay.shape[3])):
			N = '0' + N
		fig = plt.figure(figsize = (3.2*4,3 + (Axial + Sagittal + Coronal)*2.5))
		if anat != '' and i in accept[:,0] and Axial + Sagittal + Coronal != 0 and threshold_data != '':#if anatomcial specified and i in accept place overlay over the anatomcial
			overlay_acc = np.absolute(threshold_data[:,:,:,l])
			
			overlay_acc[overlay_acc < threshold] = 0 #threshold mefl.nii.gz by feats dataset
			overlay_mask = np.zeros(overlay_acc.shape)
			overlay_mask[overlay_acc != 0] = 1# 
			if flood_num != 0:
				itemindex = np.where(overlay_mask == 1)
				for j in range(len(itemindex[0])):
					overlay_mask = flood(overlay_mask,itemindex[0][j],itemindex[1][j],itemindex[2][j],flood_num)#flood fill algorithm

			overlay_acc[overlay_mask == 0] = np.nan

			#accounts for variability in choices of axial, sagittal, cornoal images in final figure
			if (Axial + Sagittal + Coronal) ==3:
				height = [1.25,1,1,.75]
				width = [2,.05]
			elif (Axial + Sagittal + Coronal) ==2:
				if Sagittal:
					height = [1.25,1,.75]
				else:
					height = [1,1,.75]
				width = [3,.05]
			elif (Axial + Sagittal + Coronal) ==1:
				height = [1,.75]
				width = [3,.05]
			gs0 = gridspec.GridSpec((Axial + Sagittal + Coronal)+1,2, height_ratios = height, width_ratios = width)
			gs0.update(left = .05, right = 1.03)

			contrast_ = overlay[overlay[:,:,:,i] != 0,i]#fix contrast overlay_z (makes no difference which overlay_'' choosen)
			maximum = np.percentile(contrast_,100 - contrast)
			minimum = np.percentile(contrast_,contrast)
			tmp,lower,upper = mask(overlay[:,:,:,i],(0,1))
			ax_montage_spacing = np.linspace(lower,upper,10)/overlay.shape[2]
			tmp,lower,upper = mask(overlay[:,:,:,i],(1,2))
			sag_montage_spacing = np.linspace(lower,upper,10)/overlay.shape[0]
			tmp,lower,upper = mask(overlay[:,:,:,i],(1,2))
			cor_montage_spacing = np.linspace(lower,upper,10)/overlay.shape[1]
			for j in range(10):#plot montage of accept component onto anatomical
				if Axial:#plot axial
					gs01 = gridspec.GridSpecFromSubplotSpec(2, 10, subplot_spec=gs0[0,0], hspace = 0.0, wspace = 0)
					ax1 = fig.add_subplot(gs01[0,j])
					plt.imshow(anat[:,:,(anat.shape[2]-1)*ax_montage_spacing[j]].T, cmap = 'Greys_r', 
						interpolation = 'nearest', extent = [anat_corners[0,0,0], anat_corners[0,0,1], anat_corners[1,0,0], anat_corners[1,0,1]])
					bar = plt.imshow(overlay_acc[:,:,(overlay_acc.shape[2]-1)*ax_montage_spacing[j]].T, cmap = GYR, extent = [overlay_corners[0,0,0], overlay_corners[0,0,1],
						overlay_corners[1,0,0], overlay_corners[1,0,1]], alpha = alpha, interpolation = 'gaussian', vmin = threshold, vmax = 5)
					plt.axis('off')
					ax1 = fig.add_subplot(gs01[1,j])
					plt.imshow(overlay[:,:,(overlay_acc.shape[2]-1)*ax_montage_spacing[j],i].T, cmap = 'Greys_r', vmin = minimum, vmax = maximum)
					plt.axis('off')
				if Sagittal:#plot sagittal
					gs02 = gridspec.GridSpecFromSubplotSpec(2, 10, subplot_spec=gs0[Axial,0], hspace = 0.0, wspace = 0.0)
					ax2 = fig.add_subplot(gs02[0,j])
					plt.imshow(anat[(anat.shape[0]-1)*sag_montage_spacing[j],:,::-1].T, cmap = 'Greys_r', 
						interpolation = 'nearest', extent = [anat_corners[1,0,0], anat_corners[1,0,1], anat_corners[2,0,0], anat_corners[2,0,1]])
					bar = plt.imshow(overlay_acc[(overlay_acc.shape[0]-1)*sag_montage_spacing[j],:,::-1].T, cmap = GYR, extent = [overlay_corners[1,0,0], overlay_corners[1,0,1],
						overlay_corners[2,0,0], overlay_corners[2,0,1]], alpha = alpha, interpolation = 'gaussian', vmin = threshold, vmax = 5)
					plt.axis('off')
					ax2 = fig.add_subplot(gs02[1,j])
					plt.imshow(overlay[(overlay.shape[0]-1)*sag_montage_spacing[j],:,::-1,i].T, cmap = 'Greys_r', vmin = minimum, vmax = maximum)
					plt.axis('off')
				if Coronal:#plot coronal
					gs03 = gridspec.GridSpecFromSubplotSpec(2, 10, subplot_spec=gs0[Axial + Sagittal,0], hspace = 0.0, wspace = 0)
					ax3 = fig.add_subplot(gs03[0,9-j])
					plt.imshow(anat[:,(anat.shape[1]-1)*cor_montage_spacing[j],::-1].T, cmap = 'Greys_r', 
						interpolation = 'nearest', extent = [anat_corners[0,0,0],anat_corners[0,0,1],anat_corners[2,0,0],anat_corners[2,0,1]])
					bar = plt.imshow(overlay_acc[:,(overlay_acc.shape[1]-1)*cor_montage_spacing[j],::-1].T, cmap = GYR, extent = [overlay_corners[0,0,0],overlay_corners[0,0,1],
						overlay_corners[2,0,0], overlay_corners[2,0,1]], alpha = alpha, interpolation = 'gaussian', vmin = threshold, vmax =5)
					plt.axis('off')
					ax3 = fig.add_subplot(gs03[1,9-j])
					plt.imshow(overlay[:,(overlay.shape[1]-1)*cor_montage_spacing[j],::-1,i].T, cmap = 'Greys_r', vmin = minimum, vmax = maximum)
					plt.axis('off')
			gs04 = gridspec.GridSpecFromSubplotSpec(1, 1, subplot_spec=gs0[Axial + Sagittal + Coronal,0])
			ax4 = fig.add_subplot(gs04[0,0])#formatting

			time_series = np.loadtxt(series)#plots time series of the component
			plt.plot(np.arange(time_series.shape[0]),time_series[:,i])
			plt.xlabel('Time (TR)', fontsize = 12)
			plt.ylabel('Arbitrary BOLD units', fontsize = 12)
	
			cbar_ax = fig.add_axes([.94,.3,.01,.65])
			fig.colorbar(bar, cax = cbar_ax)
			plt.ylabel('Absoulte z-score', fontsize = 12, rotation = 270, labelpad=20)
			plt.savefig('Component_' + N)
			plt.close()
			l += 1# index of feats_OC2.nii differs from mefl.nii.gz this accounts for this
		else:
			gs_montage(overlay, Axial, Sagittal, Coronal, series, i, N, contrast)
		FFT(TED, series, i, N)
		print ('++ figures created for Component %s' % N)
		plt.show()
"""
Creates a montage of greyscale 10 images of axial, Sagittal and coronal views of meica components along with a time series of the component.
accepted components also get overlayed onto the anatomical image and floodfill is performed on statiscially significant voxels.
maps: array of 5 elements [anat dataset, mefl dataset, feats dataset, anat header, overlay header]
overlay: mefl dataset
Axial: true or false. plot axial or not
Sagittal: true or false. plot sagittal or not
Coronal: true or false. plot coronal or not
series: string meica_mix.1D path
i: component number
N: component number as string of standardized length
"""
def gs_montage(overlay, Axial, Sagittal, Coronal, series, i, N, contrast):
	fig = plt.figure(figsize = (3.2*4,3 + (Axial + Sagittal + Coronal)*2))
	gs0 = gridspec.GridSpec((Axial + Sagittal + Coronal)+1,1)
	gs0.update(left = .05, right = .95)
	if Axial + Sagittal + Coronal != 0:
		overlay_z,lower,upper = mask(overlay[:,:,:,i],(0,1))#remove z slices with all zero terms
		overlay_x,lower,upper = mask(overlay[:,:,:,i],(1,2))
		overlay_y,lower,upper = mask(overlay[:,:,:,i],(0,2))
		contrast_ = overlay_z[overlay_z != 0]#fix contrast overlay_z (makes no difference which overlay_'' choosen)
		maximum = np.percentile(contrast_, 100 - contrast)
		minimum = np.percentile(contrast_, contrast)

	for j in range(10):#plot greyscale component montage
		if Axial:#plot axial
			gs01 = gridspec.GridSpecFromSubplotSpec(1, 10, subplot_spec = gs0[0,0], hspace = 0.0, wspace = 0)
			ax1 = fig.add_subplot(gs01[0,j])
			plt.imshow(overlay_z[:,:,overlay_z.shape[2]*j*.1].T, cmap = 'Greys_r', vmin = minimum, vmax = maximum)
			plt.axis('off')
		if Sagittal:#plot sagittal
			gs02 = gridspec.GridSpecFromSubplotSpec(1, 10, subplot_spec = gs0[Axial,0], hspace = 0.0, wspace = 0.0)
			ax2 = fig.add_subplot(gs02[0,j])
			plt.imshow(overlay_y[overlay_y.shape[0]*j*.1,:,::-1].T, cmap = 'Greys_r', vmin = minimum, vmax = maximum)
			plt.axis('off')
		if Coronal:#plot coronal
			gs03 = gridspec.GridSpecFromSubplotSpec(1, 10, subplot_spec = gs0[Axial + Sagittal,0], hspace = 0.0, wspace = 0)
			ax3 = fig.add_subplot(gs03[0,9-j])
			plt.imshow(overlay_x[:,overlay_x.shape[1]*j*.1,::-1].T, cmap = 'Greys_r', vmin = minimum, vmax = maximum)
			plt.axis('off')
	gs04 = gridspec.GridSpecFromSubplotSpec(1, 1, subplot_spec = gs0[Axial + Sagittal + Coronal,0])
	ax4 = fig.add_subplot(gs04[0,0])#formatting
	time_series = np.loadtxt(series)
 	plt.plot(np.arange(time_series.shape[0]), time_series[:,i])
 	plt.xlabel('Time (TR)', fontsize = 12)
	plt.ylabel('Arbitrary BOLD units', fontsize = 12)
	plt.savefig('Component_' + N)
	plt.close()
	plt.close()
"""
Create a figure of the corregistration of the overlay onto the anatomcial image
setname: path of directory containing the TED directory
anat: path of the anatomcial image
"""
def coreg(startdir, setname, figures, anat, coreg_anat):
	fig = plt.figure(figsize = (3.2*5,4))
	gs0 = gridspec.GridSpec(1,3)
	os.chdir(setname)
	subprocess.call('rm -f %s/ocv_uni_vrm*' % setname, shell = True)
	anat = anat[len(os.path.dirname(anat)):]
	fails = 0
	if coreg_anat != '':
		anat = coreg_anat
	if '.nii.gz' in anat[-7:]:
		anat_name = anat[:-7]
	if '.nii' in anat[-4:]:
		anat_name = anat[:-4]
	if '/' in anat_name[0]:
		anat_name = anat_name[1:]
		anat = anat[1:]
	if not os.path.isfile(anat_name + '.nii.gz') and not os.path.isfile(anat + '.nii'):
		if os.path.isfile(anat_name[:-2] + 'ns.nii.gz'):
			anat_name = anat_name[:-2]
		elif os.path.isfile(anat_name[:-5] + 'ns.nii.gz'):
			anat_name = anat_name[:-5] + 'ns'
		elif os.path.isfile(anat_name + '_ns.nii.gz'):
			anat_name = anat_name + '_ns'
		else:
			print '+* Can\'t find anatomical ,%s, to perform corregistration with. Coregistration will not be performed' % anat
			fails = 1

	if not fails:
		if os.path.isfile('%s.nii.gz' % anat_name):
			suffix = '.nii.gz'
			if not os.path.isfile('%s+orig.HEAD' % anat_name):
				subprocess.call('3dcopy %s.nii.gz %s' % (anat_name,anat_name), shell = True)	
		if os.path.isfile('%s.nii' % anat_name):
			suffix = '.nii'
			if not os.path.isfile('%s+orig.HEAD' % anat_name):
				subprocess.call('3dcopy %s.nii %s' % (anat_name,anat_name), shell = True)
			

		subprocess.call('3dcalc -a ocv_uni_vr.nii.gz -b eBvrmask.nii.gz -expr "step(b)*a" -prefix ocv_uni_vrm', shell = True)
		if os.path.isfile('ocv_uni_vrm+tlrc.BRIK'):
			subprocess.call('3drefit -view orig ocv_uni_vrm+tlrc', shell = True)
		subprocess.call('@AddEdge ocv_uni_vrm+orig %s+orig' % anat_name, shell = True)
		subprocess.call('3dcalc -a ocv_uni_vrm_e3+orig -expr "a" -prefix ocv_uni_vrm_e3.nii', shell = True)
		subprocess.call('3daxialize -overwrite -prefix axialized_%s%s %s%s'% (anat_name,suffix,anat_name,suffix), shell = True)
		subprocess.call('3daxialize -overwrite -prefix ocv_uni_vrm_e3.nii ocv_uni_vrm_e3.nii', shell = True)
		overlay = ni.load('ocv_uni_vrm_e3.nii').get_data()

		anatomical = ni.load('axialized_%s%s' % (anat_name,suffix)).get_data()
		tmp,lower,upper = mask(overlay,(0,1))
		overlay[overlay == 0] = np.nan
		ax_montage_spacing = np.linspace(lower,upper,10)/overlay.shape[2]
		fig = plt.figure(figsize = (3.2*5,4))
		gs0 = gridspec.GridSpec(1,10)
		for i in range(10):#plot montage of corregistration onto anatomcial
			ax1 = fig.add_subplot(gs0[0,i])
			plt.imshow(anatomical[:,:,(anatomical.shape[2]-1)*ax_montage_spacing[i]].T, cmap = 'Greys_r')
			plt.imshow(overlay[:,:,(overlay.shape[2]-1)*ax_montage_spacing[i]].T, cmap = GYR, alpha = 0.8)
			plt.axis('off')
		gs0.tight_layout(fig, w_pad = -2)
		fig.subplots_adjust(right = 0.9)
		os.chdir('%s/%s' % (startdir,figures))
		plt.savefig('coregistration')
		plt.close()
		print '++ finished corregistration figure'

"""
Makes TSNR figures of medn, tsoc, and medn/tsoc datasets
tsoc: string path to tsoc dataset
medn: string path to medn dataset
"""
def tsnr(tsoc,medn):
	medn_data = ni.load(medn).get_data()
	tsoc_data = ni.load(tsoc).get_data()
	medn_data[medn_data == 0] = np.nan
	tsoc_data[tsoc_data == 0] = np.nan

	medn_tsnr = medn_data.mean(-1)/medn_data.std(-1)
	tsoc_tsnr = tsoc_data.mean(-1)/tsoc_data.std(-1)
	frac = medn_tsnr/tsoc_tsnr

	medn_tsnr,lower,upper = mask(image = medn_tsnr, axis = (0,1))#remove z slices without nonzero elements
	tsoc_tsnr,lower,upper = mask(image = tsoc_tsnr, axis = (0,1))
	frac_tsnr,lower,upper = mask(image = frac, axis = (0,1))#remove z slices without nonzero elements
	medn_tsnr[medn_tsnr == 0] = np.nan
	tsoc_tsnr[tsoc_tsnr == 0] = np.nan
	frac_tsnr[frac_tsnr == 0] = np.nan
	background = np.zeros((medn_tsnr[:,:,0].T).shape)
	tsnr_options = [medn_tsnr,tsoc_tsnr,frac_tsnr]
	for j in range(3):
		tsnr = tsnr_options[j]
		fig = plt.figure(figsize = (3.2*5,4)) #medn tsnr figure
		gs0 = gridspec.GridSpec(1,10)
		#plot montage of medn TSNR
		tsnr_mask = tsnr[np.isnan(tsnr) == False]
		if j in [0,2]: 
			maximum = np.percentile(tsnr_mask,95)
			minimum = np.percentile(tsnr_mask,5)
		for i in range(0,10):
			ax1 = fig.add_subplot(gs0[0,i])#plot montage
			plt.imshow(background, cmap = 'Greys_r')
			plot = plt.imshow(tsnr[:,:,i*.1*tsnr.shape[2]].T, vmin = minimum, vmax = maximum, cmap = GYR)
			plt.axis('off')
		gs0.tight_layout(fig, w_pad = -1, rect = [0,0,0.95,1])
		cbar = fig.add_axes([(gs0.right + ((gs0.right + 1)/2 - gs0.right)/2), .2875, .01, .425])
		fig.subplots_adjust(right = 0.9)
		fig.colorbar(plot, cax = cbar)
		if j == 0:
			plt.savefig('medn_tsnr')
		elif j ==1:
			plt.savefig('tsoc_tsnr')
		else:
			plt.savefig('tsnr_ratio')
		plt.close()

	#plot histogram of the TSNR of medn
	medn_mask = medn_tsnr[np.isnan(medn_tsnr) == False]
	tsoc_mask = tsoc_tsnr[np.isnan(tsoc_tsnr) == False]
	frac_mask = frac_tsnr[np.isnan(frac_tsnr) == False]
	fig = plt.figure()
	plt.hist(medn_mask, bins = 100, range = [np.percentile(medn_mask,0.01),np.percentile(medn_mask,99.99)])
	plt.title('TSNR medn', fontsize = 15)
	plt.xlabel('TSNR', fontsize = 15)
	plt.ylabel('Frequency', fontsize = 15)
	plt.savefig('medn_tsnr_hist')
	plt.close()

	fig = plt.figure()
	plt.hist(tsoc_mask, bins = 100, range = [np.percentile(tsoc_mask,0.01),np.percentile(tsoc_mask,99.99)])
	plt.title('TSNR tsoc', fontsize = 15)
	plt.xlabel('TSNR', fontsize = 15)
	plt.ylabel('Frequency', fontsize = 15)
	plt.savefig('tsoc_tsnr_hist')
	plt.close()

	#plot histogram of the TSNR ratio of medn/tsnr
	fig = plt.figure()
	plt.hist(frac_mask, bins = 100, range = [np.percentile(frac_mask,0.01),np.percentile(frac_mask,99.99)])
	plt.title('TSNR medn / TSNR tsoc', fontsize = 15)
	plt.xlabel('TSNR ratio', fontsize = 15)
	plt.ylabel('Frequency', fontsize = 15)
	plt.savefig('tsnr_ratio_hist')
	plt.close()
	print '++ finished tsnr figures'
"""
calculates the statistical correlation between a voxel and the rest of the brain
and makes a montage image of it.  MNI option must have been stippulated
when running meica.py
startdir: path of the starting directory
setname: name of directory containing the TED directory
nsmprgae: path to the anatomical image
threshold: z-score to threshold data at.  data symmetrically thresholded about zero with threshold
"""
def correlation(startdir, label, figures, nsmprage, ROI_default, ROI_attention, ROI_refference, User_ROI, threshold):
	cdict = {'red':  	  ((0.0, 0.0, 0.0),
						   (0.6, 0.0, 0.0),
						   (0.7, 0.6, 0.6),
						   (0.75, 0.9, 0.9),
						   (0.8, 1.0, 1.0),
		                   (1.0, 1.0, 1.0)),

		         'green': ((0.0, 0.0, 0.0),
		         		   (0.6, 1.0, 1.0),
		         		   (0.8, 1.0, 1.0),
		         		   (0.85, 0.9, 0.9),
		                   (0.95, 0.5, 0.5),
		                   (1.0, 0.0, 0.0)),

		         'blue':  ((0.0, 1.0, 1.0),
		         		   (0.5, 0.0, 0.0),
		                   (1.0, 0.0, 0.0))
		        }

	BGYR = LinearSegmentedColormap('BGYR', cdict)
	beta = ni.load('%s/%s/axialized_nifti/betas_hik_OC.nii' % (startdir,label)).get_data()
	beta_hdr = ni.load('%s/%s/axialized_nifti/betas_hik_OC.nii' % (startdir,label)).get_header()
	anat = ni.load(nsmprage).get_data()
	anat_hdr = ni.load(nsmprage).get_header()

	beta_corners = np.zeros((3,1,2))
	anat_corners = np.zeros((3,1,2))
	cord_matrix = beta_hdr.get_best_affine()[0:3,0:3]
	anat_cord_matrix = anat_hdr.get_best_affine()[0:3,0:3]

	beta_corners[:,:,0] = np.array([[beta_hdr['qoffset_x']], [beta_hdr['qoffset_y']], [beta_hdr['qoffset_z']]])
	beta_corners[:,:,1] = np.dot(cord_matrix,np.array([[beta.shape[0]], [beta.shape[1]], [beta.shape[2]]])) + beta_corners[:,:,0]

	anat_corners[:,:,0] = np.array([[anat_hdr['qoffset_x']], [anat_hdr['qoffset_y']], [anat_hdr['qoffset_z']]])
	anat_corners[:,:,1] = np.dot(anat_cord_matrix,np.array([[anat.shape[0]], [anat.shape[1]], [anat.shape[2]]])) + anat_corners[:,:,0]

	for k in range(4):
		ROI = [ROI_default, ROI_attention, ROI_refference, User_ROI]
		ROI = ROI[k]
		for i in range(len(ROI)):
			MNI = np.asarray(ROI[i][:3]).astype('float64')
			MNI.shape = (3,1)
			ext = np.zeros(8)
			
			native = np.dot(np.linalg.inv(cord_matrix),MNI - np.array([[beta_hdr['srow_x'][3]], [beta_hdr['srow_y'][3]], [beta_hdr['srow_z'][3]]]))
			seed = beta[native[0,0], native[1,0], native[2,0],:]
			seed = np.asarray([seed])

			seed_location = np.zeros(beta[:,:,:,0].shape)
			seed_location[seed_location == 0] = np.nan
			seed_location[native[0,0]-1:native[0,0]+1, native[1,0]-1:native[1,0]+1, native[2,0]] = 1
			fig = plt.figure(figsize = (2.5,2.5))
			gs1 = gridspec.GridSpec(1,1)
			plt.imshow(anat[:,:,int(anat.shape[2]*native[2,0]/beta.shape[2])].T, cmap = 'Greys_r', 
					extent = [anat_corners[0,0,0], anat_corners[0,0,1], anat_corners[1,0,0], anat_corners[1,0,1]])
			plt.imshow(seed_location[:,:,native[2,0]].T, cmap = 'autumn', extent = [beta_corners[0,0,0],beta_corners[0,0,1],
					beta_corners[1,0,0], beta_corners[1,0,1]])
			plt.axis('off')
			if len(ROI[i]) > 3:
				plt.savefig('%s_seed' % ROI[i][3])
			else:
				plt.savefig('(%s,%s,%s)_seed' % (ROI[i][0], ROI[i][1], ROI[i][2]))
			plt.close()
			
			mask = beta.prod(-1) != 0
			beta_mask = beta[mask]
			norm = np.array([np.sqrt(inner1d(beta_mask,beta_mask))]).T
			norm_seed = np.sqrt(np.dot(seed,seed.T))
			beta_norm= np.divide(beta_mask,norm)
			R = np.array([inner1d(beta_norm,seed/norm_seed)]).T
			z = np.arctanh(R)*np.sqrt((beta.shape[3] - 3)) #z_value 1D array
			z[np.isnan(z)] = 5
			z[z > 5] = 5# cap at 5 and -5
			z[z < -5] = -5

			z_scores = np.zeros(mask.shape)
			z_threshold = np.zeros(mask.shape)
			z_scores[mask == True] = z[:,0]
			z_threshold[np.absolute(z_scores) > threshold] = 1

			itemindex = np.where(z_threshold == 1)
			for j in range(len(itemindex[0])):
				z_threshold = flood(z_threshold, itemindex[0][j], itemindex[1][j], itemindex[2][j])#floodfill
			bottom = 0		
			top = z_scores.shape[2]
			while np.sum(np.sum(z_scores, axis = 0), axis = 0)[bottom] == 0:
				bottom += 1
			while np.asarray(np.sum(np.sum(z_scores, axis = 0), axis = 0))[top-1] == 0:
				top += -1
			z_scores[z_threshold == 0 ] = np.nan
			fig = plt.figure(figsize = (3.2*5,4))
			gs0 = gridspec.GridSpec(1,10)
			minimum = min(z_scores[np.isnan(z_scores) == False])
			maximum = max(z_scores[np.isnan(z_scores) == False])
			N = 0
			for j in np.linspace(float(bottom)/z_scores.shape[2], float(top)/z_scores.shape[2],10):#plot montage of accept component onto
				ax1 = fig.add_subplot(gs0[0,N])
				if j == 1:
					j = (float(anat.shape[2]-1))/anat.shape[2]
				plt.imshow(anat[:,:,int(anat.shape[2]*j)].T, cmap = 'Greys_r', 
					extent = [anat_corners[0,0,0],anat_corners[0,0,1],anat_corners[1,0,0],anat_corners[1,0,1]])
				if j == (float(anat.shape[2]-1))/anat.shape[2]:
					j = float(z_scores.shape[2]-1)/z_scores.shape[2]
				plot = plt.imshow(z_scores[:,:,int(z_scores.shape[2]*j)].T, alpha = 0.8, cmap = BGYR , extent = [beta_corners[0,0,0], beta_corners[0,0,1],
					beta_corners[1,0,0],beta_corners[1,0,1]], interpolation = 'gaussian', vmin = minimum, vmax = maximum)
				plt.axis('off')
				N += 1
			gs0.tight_layout(fig, w_pad = -2.7, rect = [0,0,0.95,1])
			cbar = fig.add_axes([(gs0.right + ((gs0.right + 1)/2 - gs0.right)/2), gs0.bottom, .01, gs0.top - gs0.bottom])
			fig.colorbar(plot, cax = cbar)
			plt.ylabel('z score', fontsize = 12, rotation = 270)
			if len(ROI[i]) > 3:
				plt.savefig('%s_correlation' % ROI[i][3])
				print '++ %s correlation complete'  % ROI[i][3]
			else:
				plt.savefig('(%s,%s,%s)_correlation' % (ROI[i][0], ROI[i][1], ROI[i][2]))
				print '++ (%s,%s,%s) correlation complete'  % (ROI[i][0], ROI[i][1], ROI[i][2])
			plt.close()
"""
plot kappa vs rho and represent percent varaince by the size of the markers.
accept: array of all accepted components
reject: array of all rejected components
middle: array of all middle kappa components
ignore: array of all ignore components
"""
def kappa_vs_rho_plot(accept,reject,middle,ignore):
	plt.figure(2)# this simple figure is created and removed in order to take the legend from it.  
	#plt.legend has issue where marker size in legend is propoertional to marker size in plot
	trial_1 = plt.scatter(1,1, c = 'r', marker = 'o')
	trial_2 = plt.scatter(1,1, c = 'b', marker = '^')
	trial_3 = plt.scatter(1,1, c = 'g', marker = 'v')
	trial_4 = plt.scatter(1,1, c = 'c', marker = '*')
	plt.close(2)
	fig = plt.figure()
	plt.title('ME-ICA Analysis, ' + r'$\kappa$' + ' vs ' + r'$\rho$', fontsize = 14)
	ACC = plt.scatter(accept[:,1], accept[:,2], c = 'r', marker = 'o', s = 50 * accept[:,4]) 
	REJ = plt.scatter(reject[:,1], reject[:,2], c = 'b', marker = '^', s = 50 * reject[:,4])
	MID = plt.scatter(middle[:,1], middle[:,2], c = 'g', marker = 'v', s = 50 * middle[:,4])
	IGN = plt.scatter(ignore[:,1], ignore[:,2], c = 'c', marker = '*', s = 50 * ignore[:,4])
	plt.legend((trial_1, trial_2, trial_3, trial_4),('Accepted','Rejected','Middle',
		'Ignore'), scatterpoints = 1, loc = 'upper right', markerscale = 2)
	plt.gca().xaxis.set_major_locator(MaxNLocator(nbins = 5))
	plt.tick_params(axis = 'x', which = 'both', top = 'off')
	plt.tick_params(axis = 'y', which = 'both', right = 'off')
	plt.xlabel(r'$\kappa$', fontsize = 15)
	plt.ylabel(r'$\rho$', fontsize = 15)
	plt.savefig('kappa_vs_rho')
	plt.close()
	print '++ finished kappa vs rho figure'
"""
plot kappa and rho vs their component number.
comptable title: path to the ctab file
"""
def kr_vs_component(comp_table_title):
	fig = plt.figure()
	components = np.loadtxt(comp_table_title)
	plt.title('ME-ICA Analysis, ' + r'$\kappa$' + ' and ' + r'$\rho$' + ' vs Component Rank', fontsize = 14)
	plt.ylabel(r'$\kappa$' ', ' + r'$\rho$', fontsize = 15)
	plt.xlabel('Component Rank', fontsize = 15)
	kappa = plt.plot(components[:,0], components[:,1])
	rho = plt.plot(components[:,0], components[:,2])
	plt.legend((r'$\kappa$', r'$\rho$'))
	plt.savefig('kappa_rho_vs_components')
	plt.close()	
	print '++ finished kappa and rho vs component number figure'

def motion(startdir,figures,setname):
	os.chdir(setname)
	motion = np.loadtxt('motion.1D')
	if os.path.isfile('e.norm.1D'):
		subprocess.call('rm -f e.norm.1D', shell = True)
	subprocess.call('1d_tool.py -infile motion.1D -set_nruns 1 -derivative -collapse_cols euclidean_norm -write e.norm.1D', shell = True)
	deriv = np.loadtxt('e.norm.1D')

	os.chdir('%s/%s' % (startdir,figures))
	plt.figure()
	fig, ax = plt.subplots(nrows=6, ncols=1, sharex=True, sharey = True)
	ax[0].set_title('Subject Motion', fontsize = 14)
	plt.xlabel('Time (TR)', fontsize = 14)
	plt.ylabel('distance (mm)', fontsize = 14)
	label = ['x', 'y', 'z', 'pitch', 'roll', 'yaw']
	for i in range(6):
		ax[i].plot(np.arange(motion.shape[0]),motion[:,5-i])
		ax[i].plot(np.arange(motion.shape[0]),np.zeros(shape = (motion.shape[0],1)), ls = '--', c = 'k')
		ax[i].set_ylabel(label[i])

	ax[0].set_yticks([ax[0].get_ylim()[0], 0, ax[0].get_ylim()[1]])
	plt.setp([a.get_xticklabels() for a in fig.axes[:-1]], visible=False)
	plt.savefig('motion_plot')
	plt.close()

	plt.figure()
	plt.plot(np.arange(motion.shape[0]),deriv[:])
	plt.xlabel('Time (TR)', fontsize = 14)
	plt.ylabel('rate (mm/TR)', fontsize = 14)
	plt.title('rate of motion')
	plt.savefig('motion_rate')
	plt.close()

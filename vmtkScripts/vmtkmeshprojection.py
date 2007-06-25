#!/usr/bin/env python

## Program:   VMTK
## Module:    $RCSfile: vmtkmeshprojection.py,v $
## Language:  Python
## Date:      $Date: 2006/07/17 09:53:14 $
## Version:   $Revision: 1.1 $

##   Copyright (c) Luca Antiga, David Steinman. All rights reserved.
##   See LICENCE file for details.

##      This software is distributed WITHOUT ANY WARRANTY; without even 
##      the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR 
##      PURPOSE.  See the above copyright notices for more information.


import vtk
import vtkvmtk
import sys

import pypes

vmtkmeshprojection = 'vmtkMeshProjection'

class vmtkMeshProjection(pypes.pypeScript):

    def __init__(self):

        pypes.pypeScript.__init__(self)
        
        self.ReferenceMesh = None
        self.Mesh = None
        self.Tolerance = 1E-8

        self.SetScriptName('vmtkmeshprojection')
        self.SetScriptDoc('interpolates the point data of a reference mesh onto the input mesh')
        self.SetInputMembers([
            ['Mesh','i','vtkUnstructuredGrid',1,'','the input mesh','vmtkmeshreader'],
            ['ReferenceMesh','r','vtkUnstructuredGrid',1,'','the reference mesh','vmtkmeshreader'],
            ['Tolerance','tolerance','double',1,'','locator tolerance']
            ])
        self.SetOutputMembers([
            ['Mesh','o','vtkUnstructuredGrid',1,'','the output mesh','vmtkmeshwriter']
            ])

    def Execute(self):

        if self.Mesh == None:
            self.PrintError('Error: No Mesh.')

        if self.ReferenceMesh == None:
            self.PrintError('Error: No ReferenceMesh.')

        self.PrintLog('Computing projection.')
        meshProjection = vtkvmtk.vtkvmtkMeshProjection()
        meshProjection.SetInput(self.Mesh)
        meshProjection.SetReferenceMesh(self.ReferenceMesh)
        meshProjection.SetTolerance(self.Tolerance)
        meshProjection.Update()
        self.Mesh = meshProjection.GetOutput()

if __name__=='__main__':
    main = pypes.pypeMain()
    main.Arguments = sys.argv
    main.Execute()

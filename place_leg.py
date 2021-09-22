'''
place_leg.py
part of an modular auto-rig module
contain class for building simple ik leg joint chain

import module_leg
import module_leg.place_leg as pl

pl.Setup_Leg()

'''

import pymel.core as pm

class Setup_Leg:

    def __init__(self):
        self.hip_placer = pm.spaceLocator(n='hip_placer')
        self.knee_placer = pm.spaceLocator(n='knee_placer')
        self.ankle_placer = pm.spaceLocator(n='ankle_placer')
        

        self.hip_placer.translate.set(0, 20, 0)
        self.knee_placer.translate.set(0, 12, 4)
        self.ankle_placer.translate.set(0, 4, 0)

        self.hip_placer_grp = pm.group(em=True, name='hip_placer_grp')
        self.knee_placer_grp = pm.group(em=True, name='knee_placer_grp')
        self.ankle_placer_grp = pm.group(em=True, name='ankle_placer_grp')

        pm.matchTransform(self.hip_placer_grp, self.hip_placer)
        pm.parent(self.hip_placer, self.hip_placer_grp)
        pm.matchTransform(self.knee_placer_grp, self.knee_placer)
        pm.parent(self.knee_placer, self.knee_placer_grp)
        pm.matchTransform(self.ankle_placer_grp, self.ankle_placer)
        pm.parent(self.ankle_placer, self.ankle_placer_grp)

        pm.parentConstraint(self.hip_placer, self.ankle_placer, self.knee_placer_grp, w=1, mo=1)

        hip_pos = self.hip_placer.translate.get()
        knee_pos = self.knee_placer.translate.get()
        ankle_pos = self.ankle_placer.translate.get()

        pm.curve(n='guide_crv', p=[(hip_pos),(knee_pos),(ankle_pos)])

        pm.connectAttr('hip_placerShape.worldPosition','guide_crv.controlPoints[0]')
        pm.connectAttr('knee_placerShape.worldPosition','guide_crv.controlPoints[1]')
        pm.connectAttr('ankle_placerShape.worldPosition','guide_crv.controlPoints[2]')


        

        


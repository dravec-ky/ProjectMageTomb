import maya.cmds as mc
import maya as ma

# mc.copySkinWeights(ss= , ds= ,nm=true,sm=false, sa="closestPoint",ia="closestPoint")
objList = mc.ls(sl=True, l=True)
print(len(objList))
sourceObj = objList[0];
mc.select(objList[1], hi=True);
allObjects = mc.ls(sl=True, l=True);

sourceSkin = ma.mel.eval('findRelatedSkinCluster '+sourceObj)
for obj in allObjects:
        destSkin = ma.mel.eval('findRelatedSkinCluster '+obj)
        if(len(destSkin)>0):
            mc.copySkinWeights(ss=sourceSkin, ds=destSkin,nm=True,sm=False, sa="closestComponent",ia="closestJoint")
import os
from fbx import *


def main():
    obj_path = "resources/obj"
    fbx_path = "resources/fbx"
    paths = os.listdir(obj_path)
    for path in paths:
        sourcePath = obj_path + "/" + path
        targetPath = fbx_path + "/" + path.split('.')[0] + ".fbx"
        # Create
        manager = FbxManager.Create()
        scene = FbxScene.Create(manager, "fbxScene")
        importer = FbxImporter.Create(manager, "")
        exporter = FbxExporter.Create(manager, "")
        # Import the file to the scene
        importer.Initialize(sourcePath, -1)
        importer.Import(scene)
        # Export the scene to the file.
        exporter.Initialize(targetPath, -1)
        exporter.Export(scene)
        # Destroy
        exporter.Destroy()
        importer.Destroy()
        scene.Destroy()
        manager.Destroy()


if __name__ == '__main__':
    main()

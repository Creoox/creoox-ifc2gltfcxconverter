# creoox-ifc2gltfcxconverter
Public repository of Creoox &amp; XeoKit conversion Tool

## Compatibility to convert2xkt.js
https://github.com/xeokit/xeokit-convert

|  cxconverter    | convert2xkt.js    |
|  :---:    | :---:    |
|  5.4.5 | >=1.3.0   |
|  5.3.1   | 1.3.0   |
|  5.2.6   | 1.1.25   |
|  5.1.7   | 1.1.25   |
|  5.1.6   | 1.1.25   |
|  5.1.3   | 1.1.25   |
|  5.1.2   | 1.1.25   |
|  5.0.1   | 1.1.25   |
|  4.34.1   | 1.1.23   |
|  4.34 beta   | 1.1.23   |
|  4.33   | 1.1.23   |
|  4.27  | 1.1.23   |
|  4.16  | 1.1.22   |


## Features include:
-  Extraction of the element tree structure from the IFC model and export as a scene graph, preserving GUIDs to enable metadata linking in XeoKit.

-  Conversion of all geometric representations from IFC to points, polylines, triangle meshes and text labels for GPU rendering.

-  Configurable export settings via a configuration file.

-  Filtering to exclude elements by type or GUID.

-  Filtering to include only specified types or GUIDs.

-  Mesh deduplication (compression).

-  Element sorting by type and size to improve mesh compression.

-  File splitting to handle large models efficiently.

-  Metadata export (property sets, element quantities, types, units, etc.), configurable via the input configuration file.

-  Extract group/zone associations from the IFC model, and export to the meta data JSON file.

-  Visualization of opening elements in IFC models, which are normally not visible in IFC viewers.

-  Tested for compatibility with XeoKit.

-  Binary version for Windows and Linux for batch processing of files.
  
-  Native C++ application, fast and efficient conversion of IFC files.

-  Professional support for all sorts of issues which are common with IFC files.


<!-- The converter acts like an adapter to IFC, which hides the complexity of many different geometric representation methods, combined with complex hierarchies of coordinate systems, and boolean operations (CSG) between any of those geometric items.
The converter exposes the simplest possible common denominator for geometry - points, polygons and triangles.  -->

You can use the converter for testing without license. The generated glb files will have a watermark. After purchasing a license and adding the license key to the input config file, the watermark is not generated any more.


<img width="2475" height="1276" alt="image" src="https://github.com/user-attachments/assets/8fba68e3-7f34-4a9c-9ef0-8061871e03d1" />


# Extract Outer Shape

`extractOuterShape` reduces the size of IFC-derived GLB models by exporting mainly the surfaces that are visible from the outside.
This is useful for large GIS, city, campus, and map-based viewers where the user usually needs the external building shape rather
than every internal construction detail.

The feature is designed to make large IFC models easier to load, transfer, and render while preserving the overall model bounds and
the metadata objects created during conversion.

## Configuration

Enable the feature in the converter configuration:

```json
{
  "inputParameters": {
    "extractOuterShape": 1
  }
}
```

Available values:

| Value | Behavior |
|---|---|
| 0 | Disabled. The full model is exported. |
| 1 | Keeps the detected outer shape. Recommended default. |
| 2 | Keeps the detected outer shape and merges compatible output geometry by color. |

For most customer-facing GIS exports, start with "extractOuterShape": 1

## Method

The converter analyzes the completed GLB model from multiple outside view directions and keeps surfaces that contribute to the
externally visible shape. Open surface meshes, such as terrain, are handled so that connected visible surface regions can be kept
together instead of being treated like closed building solids.

This is not a generic mesh simplifier. It does not reshape or approximate the visible shell. Instead, it removes geometry that is
hidden from the outside and keeps the original triangles that are part of the detected outer model.

## Converter version

`5.11.2` and later versions

## Example Result

The following result compares the Duplex sample (https://github.com/Creoox/engine_web-ifc/blob/develop/tests/ifcfiles/public/duplex.ifc) exported once as a full GLB and once with "extractOuterShape": 1.

Full export files:

- `test/Duplex.glb`
- `test/Duplex.json`
- `test/Duplex.manifest.json`

Export with `extractOuterShape` enabled:

- `test/Duplex_extractOuterShape.glb`
- `test/Duplex_extractOuterShape.json`
- `test/Duplex_extractOuterShape.manifest.json`



Both exports created `246` metadata objects. The metadata JSON file size is unchanged because the object metadata is preserved.
The reported bounds are identical for the exported building geometry; `IfcSpace` elements are intentionally omitted from the
outer-shape export and can therefore affect bounds reported for the full model.
After removing hidden inner triangles, the outer-shape export also deduplicates identical remaining mesh and accessor data.
Empty hierarchy nodes left behind by removed geometry are removed recursively.

| Metric | Full export | With `extractOuterShape` | Reduction |
|---|---:|---:|---:|
| GLB file size | 308,572 bytes, 0.29 MiB | 55,432 bytes, 0.05 MiB | 82.04% |
| Metadata JSON file size | 438,221 bytes | 438,221 bytes | 0.00% |
| glTF nodes | 1,010 | 193 | 80.89% |
| glTF accessors | 356 | 94 | 73.60% |
| glTF accessors, including reused | 1,426 | 238 | 83.31% |
| glTF meshes | 235 | 60 | 74.47% |
| glTF meshes, including reused | 713 | 119 | 83.31% |
| glTF vertices | 5,399 | 747 | 86.16% |
| glTF vertices, including reused | 14,863 | 1,351 | 90.91% |
| glTF triangles | 7,228 | 731 | 89.89% |
| glTF triangles, including reused | 25,920 | 1,777 | 93.14% |

In this example, the exported GLB file became more than 82% smaller, while the number of referenced triangles was reduced by more
than 93%.

## Notes And Limitations

The benefit depends on the model. Buildings with many hidden interior surfaces usually reduce strongly. Models where nearly every
triangle is already visible from outside, such as some stadium or terrain-heavy models, may reduce less or even not at all.

Always visually check the result for new model types before using it in production workflows.

# Frequently Asked Questions

## What size of a machine do I need for cxconverter?

The hardware requirements depend on the size and complexity of your IFC models.

**Minimum requirements** (used for most of our internal tests):
- CPU: 2 cores
- RAM: 4 GB
- Disk: 10 GB free space

**Recommended for typical production use:**
- CPU: 2+ cores
- RAM: 8+ GB
- Disk: SSD with sufficient free space for input/output files (typically 5–10x the size of the input IFC file)
- Usually 8 GB RAM + 24 GB swap should be sufficient.

## Stats from our internal tests of IFC to GLB conversion

### cxconverter v5.8.14 — 21 models tested

| Model | IFC Size | GLB Size | Compression | Time | Peak RAM | Meshes | Vertices | Triangles | Materials | Nodes |
|-------|----------|----------|-------------|------|----------|--------|----------|-----------|-----------|-------|
| BAKU OLYMPIC STADIUM | 2.00 GB | 246.0 MB | 88.0% | 38.2 s | 15.0 GB | 18,413 | 3,830,199 | 7,627,294 | 16 | 1,007,640 |
| Model 01 | 509.1 MB | 50.9 MB | 90.0% | 14.0 s | 2.5 GB | 2,326 | 1,604,303 | 2,802,938 | 9 | 4,878 |
| Model 02 | 327.8 MB | 24.2 MB | 92.6% | 16.4 s | 2.0 GB | 13,243 | 252,019 | 442,038 | 16 | 284,817 |
| Model 03 | 286.6 MB | 102.9 MB | 64.1% | 11.2 s | 2.5 GB | 2 | 3,000,441 | 5,994,341 | 3 | 8 |
| Model 04 | 221.7 MB | 35.2 MB | 84.1% | 1m 20s | 1.3 GB | 1,099 | 242,765 | 439,117 | 15 | 313,547 |
| Model 05 | 104.9 MB | 7.6 MB | 92.8% | 4.0 s | 731 MB | 6,310 | 48,631 | 67,006 | 39 | 59,472 |
| Model 06 | 64.0 MB | 16.1 MB | 74.8% | 2.7 s | 539 MB | 1,644 | 592,543 | 868,298 | 43 | 11,220 |
| Model 07 | 37.6 MB | 6.3 MB | 83.1% | 2.0 s | 315 MB | 6,112 | 63,498 | 97,632 | 50 | 38,027 |
| Model 08 | 36.0 MB | 3.7 MB | 89.7% | 1.3 s | 222 MB | 1,952 | 91,121 | 175,186 | 16 | 8,498 |
| Model 09 | 32.4 MB | 3.7 MB | 88.5% | 1.2 s | 205 MB | 1,057 | 107,804 | 200,715 | 28 | 3,956 |
| Model 10 | 29.8 MB | 10.9 MB | 63.5% | 2.8 s | 325 MB | 9,393 | 110,101 | 149,732 | 44 | 89,159 |
| Model 11 | 23.6 MB | 1.8 MB | 92.3% | 850 ms | 138 MB | 408 | 49,494 | 89,193 | 31 | 1,566 |
| Model 12 | 18.8 MB | 4.7 MB | 75.1% | 2.4 s | 156 MB | 2,377 | 72,538 | 132,615 | 22 | 18,465 |
| Model 13 | 18.8 MB | 7.9 MB | 58.0% | 2.2 s | 308 MB | 1,908 | 349,442 | 690,846 | 16 | 27,804 |
| Model 14 | 18.8 MB | 7.9 MB | 58.0% | 2.2 s | 308 MB | 1,908 | 349,442 | 690,846 | 16 | 27,804 |
| Model 15 | 9.5 MB | 724.2 KB | 92.6% | 470 ms | 71 MB | 344 | 7,259 | 12,737 | 10 | 4,760 |
| Model 16 | 8.3 MB | 2.0 MB | 75.4% | 3.0 s | 139 MB | 135 | 48,349 | 96,379 | 6 | 4,021 |
| Model 17 | 6.2 MB | 457.9 KB | 92.8% | 180 ms | 37 MB | 88 | 14,087 | 22,670 | 7 | 311 |
| Model 18 | 1.9 MB | 376.0 KB | 80.2% | 90 ms | 21 MB | 82 | 9,168 | 17,855 | 14 | 273 |
| Model 19 | 1.5 MB | 384.9 KB | 74.5% | 70 ms | 19 MB | 158 | 9,112 | 17,431 | 24 | 362 |
| Model 20 | 659.6 KB | 116.1 KB | 82.4% | 30 ms | 12 MB | 57 | 2,474 | 4,246 | 9 | 171 |

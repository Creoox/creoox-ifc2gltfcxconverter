# Metadata Schema Validation

This directory contains the JSON Schema for xeokit metadata files and a validation tool.

## Files

- `metadata.schema.json` - JSON Schema (Draft 7) for validating metadata files
- `example_metadata.json` - Example metadata file demonstrating the schema structure
- `validate_metadata.py` - Python script for validating metadata files against the schema
- `pyproject.toml` - Python project configuration with dependencies

## Quick Start

### Using uv (recommended)

1. Install dependencies:
   ```bash
   cd specification
   uv sync
   ```

2. Run validation on the example file:
   ```bash
   uv run python validate_metadata.py
   ```

3. Validate a custom file:
   ```bash
   uv run python validate_metadata.py metadata.schema.json your_file.json
   ```

### Using standard Python venv

1. Create and activate virtual environment:
   ```bash
   cd specification
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install jsonschema
   ```

3. Run validation:
   ```bash
   python validate_metadata.py
   ```

## Validation Script Usage

```bash
python validate_metadata.py [schema_file] [metadata_file]
```

**Arguments:**
- `schema_file` (optional) - Path to schema file (default: `metadata.schema.json`)
- `metadata_file` (optional) - Path to metadata file to validate (default: `example_metadata.json`)

**Examples:**

```bash
# Validate example file (uses defaults)
python validate_metadata.py

# Validate custom file against default schema
python validate_metadata.py metadata.schema.json my_metadata.json

# Use custom schema
python validate_metadata.py my_custom_schema.json my_metadata.json
```

## Output

### Successful Validation
```
✅ Validation PASSED for example_metadata.json

The metadata file is valid according to the schema!

File Statistics:
  - ID: building_project_2024
  - Project ID: 2hk9fGH$H4Pxj3f8v_Dxg7
  - Schema: IFC4
  - Meta Objects: 6
  - Properties: 4
  - Property Sets: 2
  - Units: 6
  - Groups: 0
```

### Failed Validation
When validation fails, the script provides detailed error messages including:
- The path to the problematic field
- A description of what went wrong
- The validator that failed

## Schema Overview

The metadata schema validates xeokit metadata files with the following structure:

### Required Fields
- `id` - Unique identifier for the model
- `metaObjects` - Array of metadata objects (minimum 1)

### Optional Fields
- `projectId` - Project identifier (e.g., IFC project GUID)
- `author` - Author of the model or metadata
- `createdAt` - Creation timestamp (ISO 8601 format)
- `schema` - Schema version (IFC4, IFC2X3, IFC4X3, custom)
- `creatingApplication` - Software that created the model
- `properties` - Global property definitions
- `propertySets` - Property set definitions
- `units` - Unit definitions from the IFC model
- `projectUnits` - Project-wide unit type mappings
- `groups` - Groups for organizing objects

See `metadata.schema.json` for complete schema details.

#!/usr/bin/env python3
"""
Validate metadata JSON files against the metadata schema.
"""
import json
import sys
from jsonschema import validate, ValidationError, Draft7Validator

def validate_metadata(schema_path, metadata_path):
    """Validate a metadata file against the schema."""

    # Load schema
    with open(schema_path, 'r') as f:
        schema = json.load(f)

    # Load metadata
    with open(metadata_path, 'r') as f:
        metadata = json.load(f)

    # Create validator
    validator = Draft7Validator(schema)

    # Collect all errors
    errors = list(validator.iter_errors(metadata))

    if errors:
        print(f"❌ Validation FAILED for {metadata_path}")
        print(f"\nFound {len(errors)} error(s):\n")
        for i, error in enumerate(errors, 1):
            print(f"Error {i}:")
            print(f"  Path: {' -> '.join(str(p) for p in error.path) or 'root'}")
            print(f"  Message: {error.message}")
            if error.validator:
                print(f"  Validator: {error.validator}")
            print()
        return False
    else:
        print(f"✅ Validation PASSED for {metadata_path}")
        print("\nThe metadata file is valid according to the schema!")

        # Print some stats
        print(f"\nFile Statistics:")
        print(f"  - ID: {metadata.get('id', 'N/A')}")
        print(f"  - Project ID: {metadata.get('projectId', 'N/A')}")
        print(f"  - Schema: {metadata.get('schema', 'N/A')}")
        print(f"  - Meta Objects: {len(metadata.get('metaObjects', []))}")
        print(f"  - Properties: {len(metadata.get('properties', []))}")
        print(f"  - Property Sets: {len(metadata.get('propertySets', []))}")
        print(f"  - Units: {len(metadata.get('units', []))}")
        print(f"  - Groups: {len(metadata.get('groups', []))}")

        return True

if __name__ == "__main__":
    schema_path = sys.argv[1] if len(sys.argv) > 1 else "specification/metadata.schema.json"
    metadata_path = sys.argv[2] if len(sys.argv) > 2 else "specification/example_metadata.json"

    try:
        is_valid = validate_metadata(schema_path, metadata_path)
        sys.exit(0 if is_valid else 1)
    except FileNotFoundError as e:
        print(f"❌ Error: File not found - {e}")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"❌ Error: Invalid JSON - {e}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)

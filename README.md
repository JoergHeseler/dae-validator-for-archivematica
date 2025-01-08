# DAE Validator for Archivematica

This repository provides a script that enables [Archivematica](https://www.archivematica.org/) to validate COLLADA Digital Asset Exchange (DAE) files.

## Installation

To install this script, follow these steps:

### 1. Download the official DAE schemas

- Create a folder `/usr/share/schemes` and a subfolder `/usr/share/schemes/dae`.
- Download the [DAE schema 1.4.1](https://www.khronos.org/files/collada_schema_1_4_1.xsd) and [DAE schema 1.5.0](https://www.khronos.org/files/collada_schema_1_5_0.xsd) from the official [DAE website](https://www.khronos.org/api/collada) and put them in the `/usr/share/schemes/dae/` folder.

### 2. Create a new validation command

- In the Archivematica frontend, navigate to **Preservation planning** > **Validation** > **Commands** > **Create new command** or go directly to [this link](http://10.10.10.20/fpr/fpcommand/create/).
- Fill in the following fields:
  - **The related tool**: Select **Archivematica script**.
  - **Description**: Enter `Validate using dae-validator`.
  - **Command**: Paste the entire content of the [**dae-validator.py**](./src/dae-validator.py) file.
  - **Script type**: Select **Python script**.
  - **Command usage**: Select **Validation**.
  - Leave all other input fields and combo boxes untouched.
- Click **Save**.

### 3. Create a new validation rule for ASCII based glTF 1.0

- In the Archivematica frontend, navigate to **Preservation planning** > **Validation** > **Rules** > **Create new rule** or go directly to [this link](http://10.10.10.20/fpr/fprule/create/).
- Fill in the following fields:
  - **Purpose**: Select **Validation**.
  - **The related format**: Select **Model: COLLADA Digital Asset Exchange (DAE): COLLADA DAE (fmt/1209)**.
  - **Command**: Select **Validate using dae-validator**.
- Click **Save**.

## Test

To test this validator, you can use the sample DAE files located [here](https://github.com/JoergHeseler/3d-sample-files-for-digital-preservation-testing/tree/main/dae).

### In Archivematica:

You can view the error codes and detailed validation results in the Archivmatica frontend after starting a transfer by expanding the `▸ Microservice: Validation` section and clicking on the gear icon of `Job: Validate formats`.

Files with no errors end with `valid` in their name and should pass validation with this script (i. e. return error code **0**). However, all other files contain errors and should fail validation (i. e. return error code **1**).

### In the command line:

You can use the validator at the command line prompt by typing `python dae-validator.py <DAE file to validate> --schemes-path=<path to DAE schemes>`.

## Dependencies

[Archivematica 1.13.2](https://github.com/artefactual/archivematica/releases/tag/v1.13.2), the [DAE schema 1.4.1](https://www.khronos.org/files/collada-schema-1-4-1.xsd) and [DAE schema 1.5.0](https://www.khronos.org/files/collada-schema-1-5) were used to analyze, design, develop and test this script.

## Background

As part of the [NFDI4Culture](https://nfdi4culture.de/) initiative, efforts are underway to enhance the capabilities of open-source digital preservation software like Archivematica to identify, validate and preserve 3D file formats. This repository provides a script to enable COLLADA Digital Asset Exchange (DAE) file validation in Archivematica, which is not supported by default in version 1.13.2, enhancing its 3D content preservation capabilities.

## Related projects

- [3D Sample Files for Digital Preservation Testing](https://github.com/JoergHeseler/3d-sample-files-for-digital-preservation-testing)
- [glTF Metadata Extractor for Archivematica](https://github.com/JoergHeseler/gltf-metadata-extractor-for-archivematica)
- [glTF Validator for Archivematica](https://github.com/JoergHeseler/gltf-validator-for-archivematica)
- [Siegfried Falls Back on Fido Identifier for Archivematica](https://github.com/JoergHeseler/siegfried-falls-back-on-fido-identifier-for-archivematica)
  <!-- - [STL Cleaner](https://github.com/JoergHeseler/stl-cleaner) -->
- [STL Metadata Extractor for Archivematica](https://github.com/JoergHeseler/stl-metadata-extractor-for-archivematica)
- [STL Validator for Archivematica](https://github.com/JoergHeseler/stl-validator-for-archivematica)
- [X3D Validator for Archivematica](https://github.com/JoergHeseler/x3d-validator-for-archivematica)

## Acknowledgments

Special thanks to the IT colleagues at the SLUB Dresden for their support and valuable feedback during development.

## Imprint

[NFDI4Culture](https://nfdi4culture.de/) – Consortium for Research Data on Material and Immaterial Cultural Heritage

NFDI4Culture is a consortium within the German [National Research Data Infrastructure (NFDI)](https://www.nfdi.de/).

Author: [Jörg Heseler](https://orcid.org/0000-0002-1497-627X)

This repository is licensed under a [Creative Commons Attribution 4.0 International License (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/).

NFDI4Culture is funded by the German Research Foundation (DFG) – Project number – [441958017](https://gepris.dfg.de/gepris/projekt/441958017).

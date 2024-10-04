# dae-validator-for-archivematica

**dae-validator-for-archivematica** is a script that enables [Archivematica](https://www.archivematica.org/) to validate COLLADA Digital Asset Exchange (DAE) files.

## Installation

To install the **dae-validator-for-archivematica** script, follow these steps:

### 1. Download the official DAE schemas 

- Create a folder `/usr/share/schemes` and a subfolder `/usr/share/schemes/dae`.
- Download the [DAE schema 1.4.1](https://www.khronos.org/files/collada-schema-1-4-1.xsd) and [DAE schema 1.5.0](https://www.khronos.org/files/collada-schema-1-5-0.xsd) from the official [DAE website](https://www.khronos.org/api/collada) and put them in the `/usr/share/schemes/dae/` folder.

### 2. Create a new validation command
- In the Archivematica frontend, navigate to **Preservation planning** > **Validation** > **Commands** > **Create new command** or go directly to [this link](http://10.10.10.20/fpr/fpcommand/create/).
- Fill in the following fields:
    - **The related tool**: Select **Archivematica script**.
    - **Description**: Enter `Validate using dae-validator`.
    - **Script**: Paste the entire content of the [**dae-validator.py**](./src/dae-validator.py) file.
    - **Script type**: Select **Python script**.
    - **Command usage**: Select **Validation**.
- Click **Save**.

### 3. Create a new validation rule for ASCII based glTF 1.0
- In the Archivematica frontend, navigate to **Preservation planning** > **Validation** > **Rules** > **Create new rule** or go directly to [this link](http://10.10.10.20/fpr/fprule/create/).
- Fill in the following fields:
    - **Purpose**: Select **Validation**.
    - **The related format**: Select **Model: COLLADA Digital Asset Exchange (DAE): COLLADA DAE (fmt/1209)**.
    - **Command**: Select **Validate using dae-validator**.
- Click **Save**.

## Test

To test this validator, you can use the sample DAE files located in the [`test`](./test/) folder.

You can view the error codes and detailed validation results in the Archivmatica frontend after starting a transfer by expanding the `▸ Microservice: Validation` section and clicking on the gear icon of `Job: Validate formats`.

Files with no errors end with the filename `-valid` and should pass validation with this script (i. e. return error code **0**). However, all other files contain errors and should fail validation (i. e. return error code **1**).

## Dependencies

[Archivematica 1.13.2](https://github.com/artefactual/archivematica/releases/tag/v1.13.2), the [DAE schema 1.4.1](https://www.khronos.org/files/collada-schema-1-4-1.xsd) and [DAE schema 1.5.0](https://www.khronos.org/files/collada-schema-1-5) were used to analyze, design, develop and test this script.

## Background

As part of the [NFDI4Culture](https://nfdi4culture.de/) initiative, efforts are underway to enhance the capabilities of open-source digital preservation software like Archivematica to identify, validate and preserve 3D file formats. This repository provides the **dae-validator-for-archivematica** script to enable COLLADA Digital Asset Exchange (DAE) file validation in Archivematica, which is not supported by default in version 1.13.2, enhancing its 3D content preservation capabilities.

## Related projects

- [3d-sample-files-for-digital-preservation-testing](https://github.com/JoergHeseler/3d-sample-files-for-digital-preservation-testing)
- [gltf-validator-for-archivematica](https://github.com/JoergHeseler/gltf-validator-for-archivematica)
- [siegfried-falls-back-on-fido-identifier-for-archivematica](https://github.com/JoergHeseler/siegfried-falls-back-on-fido-identifier-for-archivematica)
- [stl-validator-for-archivematica](https://github.com/JoergHeseler/stl-validator-for-archivematica)
- [x3d-validator-for-archivematica](https://github.com/JoergHeseler/x3d-validator-for-archivematica)

## Imprint

[NFDI4Culture](https://nfdi4culture.de/) – Consortium for Research Data on Material and Immaterial Cultural Heritage

NFDI4Culture is a consortium within the German [National Research Data Infrastructure (NFDI)](https://www.nfdi.de/).

Author: [Jörg Heseler](https://orcid.org/0000-0002-1497-627X)

This project is licensed under a [Creative Commons Attribution 4.0 International License (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).

NFDI4Culture is funded by the German Research Foundation (DFG) – Project number – [441958017](https://gepris.dfg.de/gepris/projekt/441958017).
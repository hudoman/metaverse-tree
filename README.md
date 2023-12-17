# Bigtime Metaverse Tree

Generate metaverse tree like structure based on Spaces and Utilities.
Space (land/room) has multiple doors/exits which can connect another Space or Utility.

<img width="277" alt="space" src="https://github.com/hudoman/metaverse-tree/assets/153922791/cff4af6f-13be-4970-8f50-cc6def20e56b">

## Design

Feature is build with use of Composition design pattern.
Generators are used to loop through nested structures.

## Usage
Example usage can be found in tests.py

## Flaws
There are some known issues with blocked exits which this feature is not accounting for. 


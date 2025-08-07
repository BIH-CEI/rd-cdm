#!/usr/bin/env python3
import ruamel.yaml

yaml = ruamel.yaml.YAML()
base_path = "src/rd_cdm/instances/v2_0_0/"

with open(base_path + "code_systems.yaml") as f:
    cs = yaml.load(f)
with open(base_path + "data_elements.yaml") as f:
    de = yaml.load(f)
with open(base_path + "value_sets.yaml") as f:
    vs = yaml.load(f)

merged = {
    "code_systems": cs["code_systems"],
    "data_elements": de["data_elements"],
    "value_sets": vs["value_sets"],
}

with open(base_path + "rd_cdm_full.yaml", "w") as f:
    yaml.dump(merged, f)

print("Wrote rd_cdm_full.yaml")

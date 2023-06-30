#!/bin/bash 

common=""
common="${common} --layout 'grid; rows: 2; cols: 2; space: 2mm'"
common="${common} --tabs   'fixed; width: 3mm; vcount: 2'"
common="${common} --cuts   'mousebites; drill: 0.5mm; spacing: 1mm; offset: 0.2mm; prolong: 0.5mm'"
common="${common} --framing 'frame; width: 5mm; space: 3mm; cuts: h'"
common="${common} --fiducials '3fid; hoffset: 5mm; voffset: 2.5mm; coppersize: 2mm; opening: 1mm;'"
common="${common} --post 'millradius: 1mm'"

eval kikit panelize "${common}" ../LEDPulser/LEDPulser.kicad_pcb                    panel_LEDPulser.kicad_pcb
eval kikit panelize "${common}" ../RPiHat/RPiHatHVLVPower/RPiHatHVLVPower.kicad_pcb panel_HVLVPower.kicad_pcb
eval kikit panelize "${common}" ../RPiHat/RPiHatSensor/RPiHatSensor.kicad_pcb       panel_Sensor.kicad_pcb


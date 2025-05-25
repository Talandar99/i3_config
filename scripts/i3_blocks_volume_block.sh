#!/usr/bin/bash

if [[ -n "$BLOCK_BUTTON" ]]; then
    pavucontrol &>/dev/null &
fi
bash -c " echo 'VOL:$(pulsemixer --get-volume | cut -d' ' -f1)%' "


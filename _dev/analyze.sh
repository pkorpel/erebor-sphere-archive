#!/bin/bash

pushd paket
paket restore
popd

wine ./paket/packages/SphereSharp.Cli/tools/spheresharp.cli.exe analyze -s ./../shard.settings.json

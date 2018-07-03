cd paket
paket.exe restore
cd ..

@paket\packages\SphereSharp.Cli\tools\spheresharp.cli.exe analyze -s .\..\shard.settings.json
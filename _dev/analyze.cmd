cd paket
paket.exe restore
cd ..

if "%~1"=="" goto blank

@paket\packages\SphereSharp.Cli\tools\spheresharp.cli.exe analyze -s .\..\shard.settings.json "%~1"
goto done

:blank
@paket\packages\SphereSharp.Cli\tools\spheresharp.cli.exe analyze -s .\..\shard.settings.json
goto done

:done
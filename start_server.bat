@echo off
if "%~1" neq "_start_" (
	call winhttpjs.bat "http://localhost:5000/server-start"  -method GET  -saveTo response.txt
	start /wait .\factorio.exe --start-server .\saves/hackadise.zip --config .\config-server.ini --server-settings .\server-settings.json
	cmd /c "%~f0" _start_ %*
	call winhttpjs.bat "http://localhost:5000/server-stop" -method GET  -saveTo response.txt
	exit /b
)
shift /1

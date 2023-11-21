set tts_path=C:\Users\Demensdeum\Documents\Sources\Coqui2RVC\build\tts.wav
set index_path=C:\Users\Demensdeum\Documents\Sources\3rdParty\RVC1006Nvidia\logs\goblin\added_IVF2148_Flat_nprobe_1_goblin_v2.index
set opt_path=C:\Users\Demensdeum\Documents\Sources\Coqui2RVC\build\output.wav
set model_name=goblin.pth
set is_russian=True
set speed=1.6
set emotion=Neutral
set f0up_key=-15
set input_path=%tts_path%

python sayTTS.py %tts_path% %emotion% %speed% %is_russian%

@echo off
if %ERRORLEVEL% neq 0 (
    @echo on
    echo TTS problem! Check params!!!
@echo off
    exit %ERRORLEVEL%
)

cd C:\Users\Demensdeum\Documents\Sources\3rdParty\RVC1006Nvidia

set f0method=pm
set device=device:cuda:0
set is_half=False

runtime\python.exe tools\infer_cli.py ^
                --input_path %input_path% ^
                --index_path %index_path% ^
                --f0method %f0method% ^
                --opt_path %opt_path% ^
                --model_name %model_name% ^
                --is_half %is_half% ^
                --f0up_key %f0up_key%

@echo off
if %ERRORLEVEL% neq 0 (
    @echo on
    echo Coqui problem! Check params!!!
@echo off
    exit %ERRORLEVEL%
)

explorer %opt_path%
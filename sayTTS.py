import torch
import sys
from TTS.api import TTS

# Get device
device = "cuda" if torch.cuda.is_available() else "cpu"

# List available 🐸TTS models
print(TTS().list_models())

russian = False

if russian == False:
    message = "OK! THAT IS IT! THIS IS THE FINAL STRAAAAAAAW! I’VE HAD IT WITH ALL YOU FRICKIN’ TROLLS AND ALL YOU FRICKIN’ HATERS AND ALL YOU FRICKIN SONIC FAN FRICKS. YOU GUYS ARE THE ONES THAT RUINED SONIC FOR EVERYONE! CAN'T YOU SEE THAT? WHAT THE FRICK ARE YOU GUYS DOING! ASKING FOR ALL THIS FRICKING GARBAGE- WHY DO WE NEED SONIC ADVENTURE 3? WHY DO WE NEED SONIC HEROES 2? WHY DO WE NEED ANOTHER BOOST TO WIN TITLE? WHY DO WE NEED A SONIC 2006 SEQUEL? WHY DO WE NEED ALL THAT? CANT WE HAVE A 3D-ENVIRONMENT CLASSIC SONIC GAME FOR CRYING OUT FRICKIN LOUD! YOU GUYS KILLED THE SONIC SERIES ALL YOU FRICKIN FAN FRICKS AND YOUR FRICKIN FANTASIES SPEWED OUT AT YOU BY FRICKIN POO MERCHANTS!!! I’M TIRED OF ALL YOU FRICKS! I’M SO FRICKIN MAD! I’M SO FRICKIN MAD- I MEAN, YOU GUYS- YOU GUYS HAVE OFFICIALLY MADE ME LOSE MY MARBLES! WHY CANT YOU GUYS JUST ASK FOR A 3D ENVIRONMENT CLASSIC SONIC GAME! THIS IS A NIGHTMARE! [THROWS CHAIR] I’M SURE NO SONIC FAN PREDICT- WOULD PREDICT- THAT THE ADVENTURE- THE ADVENTURE FANTASIZERS WOULD RUIN EVERYTHING! [BREATHING HEAVILY] AND NOW- AND NOW I BET BY NOW THAT SEGA HAS GOT A FRICKIN SONIC ADVENTURE 3 IN DEVELOPMENT- WITH FRICKIN SONIC TEAM. CUZ YOU FRICKIN FRICKS! JUST CAN’T EVER, BE QUENCHED. YOUR- YOUR FANTASIES CAN’T EVER BE QUENCHED- CAN THEY? YOU FRICKIN FRICKS. WHEN WILL YOU LEARN.. WHEN WILL YOU LEARN THAT YOUR ACTIONS HAVE CONSEQUENCES!? YOU GUYS KEEP ON ASKING FOR SONIC ADVENTURE 3! YOU’RE RUINING THE SONIC SERIES- HASN’T IT ALREADY SUFFERED ENOUGH!? "
else:
    message = ""

message = message.lower()

print(message)

tts = TTS(model_name="tts_models/en/ljspeech/vits", progress_bar=True, gpu=True)

tts.tts_to_file(text=message, file_path=sys.argv[1], emotion=sys.argv[2], speed=sys.argv[3])
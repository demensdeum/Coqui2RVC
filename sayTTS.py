import sys

is_russian = sys.argv[4] == "True"
speed = sys.argv[3] * 80
output_filepath = sys.argv[1]

print(f"is_russian = {is_russian}")

if is_russian:
    import pyttsx3
else:
    import torch
    from TTS.api import TTS
    print(TTS().list_models())
    device = "cuda" if torch.cuda.is_available() else "cpu"

if is_russian == True:
    model_name = "tts_models/rus/fairseq/vits"
    message = "Здраствуйте. Я, Кирилл. Хотел бы чтобы вы сделали игру, 3Д-экшон суть такова... Пользователь может играть лесными эльфами, охраной дворца и злодеем. И если пользователь играет эльфами то эльфы в лесу, домики деревяные, набигают солдаты дворца и злодеи. Можно грабить корованы... И эльфу раз лесные то сделать так что там густой лес... А движок можно поставить так что вдали деревья картинкой, когда подходиш они преобразовываются в 3-хмерные деревья. Можно покупать и т.п. возможности как в Daggerfall. И враги 3-хмерные тоже, и труп тоже 3д. Можно прыгать и т.п. Если играть за охрану дворца то надо слушаться командира, и защищать дворец от злого (имя я не придумал) и шпионов, партизанов эльфов, и ходит на набеги на когото из этих (эльфов, злого…). Ну а если за злого… то значит шпионы или партизаны эльфов иногда нападают, пользователь сам себе командир может делать что сам захочет прикажет своим войскам с ним самим напасть на дворец и пойдет в атаку."
    message = message.lower()
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.setProperty('voice', "Microsoft Irina Desktop")    
    engine.save_to_file(message, output_filepath)
    engine.runAndWait()
else:
    model_name = "tts_models/en/ljspeech/vits"
    message = "OK! THAT IS IT! THIS IS THE FINAL STRAAAAAAAW! I’VE HAD IT WITH ALL YOU FRICKIN’ TROLLS AND ALL YOU FRICKIN’ HATERS AND ALL YOU FRICKIN SONIC FAN FRICKS. YOU GUYS ARE THE ONES THAT RUINED SONIC FOR EVERYONE! CAN'T YOU SEE THAT? WHAT THE FRICK ARE YOU GUYS DOING! ASKING FOR ALL THIS FRICKING GARBAGE- WHY DO WE NEED SONIC ADVENTURE 3? WHY DO WE NEED SONIC HEROES 2? WHY DO WE NEED ANOTHER BOOST TO WIN TITLE? WHY DO WE NEED A SONIC 2006 SEQUEL? WHY DO WE NEED ALL THAT? CANT WE HAVE A 3D-ENVIRONMENT CLASSIC SONIC GAME FOR CRYING OUT FRICKIN LOUD! YOU GUYS KILLED THE SONIC SERIES ALL YOU FRICKIN FAN FRICKS AND YOUR FRICKIN FANTASIES SPEWED OUT AT YOU BY FRICKIN POO MERCHANTS!!! I’M TIRED OF ALL YOU FRICKS! I’M SO FRICKIN MAD! I’M SO FRICKIN MAD- I MEAN, YOU GUYS- YOU GUYS HAVE OFFICIALLY MADE ME LOSE MY MARBLES! WHY CANT YOU GUYS JUST ASK FOR A 3D ENVIRONMENT CLASSIC SONIC GAME! THIS IS A NIGHTMARE! [THROWS CHAIR] I’M SURE NO SONIC FAN PREDICT- WOULD PREDICT- THAT THE ADVENTURE- THE ADVENTURE FANTASIZERS WOULD RUIN EVERYTHING! [BREATHING HEAVILY] AND NOW- AND NOW I BET BY NOW THAT SEGA HAS GOT A FRICKIN SONIC ADVENTURE 3 IN DEVELOPMENT- WITH FRICKIN SONIC TEAM. CUZ YOU FRICKIN FRICKS! JUST CAN’T EVER, BE QUENCHED. YOUR- YOUR FANTASIES CAN’T EVER BE QUENCHED- CAN THEY? YOU FRICKIN FRICKS. WHEN WILL YOU LEARN.. WHEN WILL YOU LEARN THAT YOUR ACTIONS HAVE CONSEQUENCES!? YOU GUYS KEEP ON ASKING FOR SONIC ADVENTURE 3! YOU’RE RUINING THE SONIC SERIES- HASN’T IT ALREADY SUFFERED ENOUGH!? "
    message = message.lower()
    tts = TTS(model_name=model_name, progress_bar=True, gpu=True)
    tts.tts_to_file(text=message, file_path=output_filepath, emotion=sys.argv[2], speed=speed)



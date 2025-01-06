import random
import os
import importlib.util
from highrise import*
from highrise import BaseBot,Position
from highrise.models import SessionMetadata

louca = ["🤪Your Madness Livel is: 100%","🤪Your Madness Livel is: 99%","🤪Your Madness Livel is: 50%","🤪Your Madness Livel is: 0%" ,"🤪Your Madness Livel is: 1%","🤪Your Madness Livel is: 2%","🤪Your Madness Livel is: 64%","🤪Your Madness Livel is: 22 %","🤪Your Madness Livel is: 19%","🤪Your Madness Livel is: 88%","🤪Your Madness Livel is: 39%","🤪Your Madness Livel is: : 40%","🤪Your Livel Of Madness is : 92%","🤪Your Livel Of Madness is : 74%","🤪Your Livel Of Madness is : 10%","🤪Your Livel Of Madness is: 9%","🤪Your Livel of Madness is: 77%","🤪Your Livel of Madness is: 82%","🤪Your Livel of Madness is: 66%","🤪Your Livel Madness is: 11%","🤪Your Madness Livel is: 15%"]
        
casa = ["I Marry You 💍","Of course I do 💍❤️","I don't want to 💍💔","Of course I don't 💍💔","I Love You Of course I marry you 💍 "]


curativo = ["🔴You Used the Bandage Your Life Is at: 100%🔴","🔴You Used the Bandage Your Life Is at: 50%🔴","🔴You Used the Bandage Your Life Is at: 60%🔴","🔴You You Used the Bandage Your Life Is at: 75% Bandage Your Life is at: 90% Life is at: 91%🔴 "]
         
bomba = ["💣🧟‍♂️ You Threw a Bomb on 1x Boss Zombie 🧟‍♀️💣","💣🧟 You Threw a Bomb on 3x Boss Zombie 🧟💣","💣🧟‍♂️ You Threw a Bomb on 2x Boss Zombie 💣🧟‍","💣🧟‍♂️ You Threw a Bomb on 7x Boss Zombie 💣🧟‍♂️","💣🧟 You Threw a Bomb on 4x Boss Zombie 🧟💣 "]

facada = ["🧟🔪 You Stabbed 1x Zombie 🔪🧟","🧟🔪 You Stabbed 6x Zombie 🔪🧟","🧟🔪 You Stabbed 7x Zombie 🔪🧟","🧟‍♂️🔪🧟‍♂️ You Stabbed or 8x Zombie 🔪🧟‍♂️", "🧟🔪 You Stabbed 10x Zombie 🔪🧟","🧟🔪 You Stabbed 9x Zombie 🔪🧟","🧟‍♀️🔪🧟‍♂️ You Stabbed 3x Zombie 🧟‍♂️🔪🧟"]

atirar = ["🧟You Shot 5x Zombie🧟","🧟You Shot 1x Zombie🧟","🧟You Shot 8x Zombie🧟","🧟You Shot 3x Zombie🧟","🧟‍♂️You Shot 5x Zombie🧟‍ ♂️","🧟‍♀️You Shot 10x Zombie🧟‍♀️","🧟🧟‍♀️You Shot 9x Zombie🧟🧟‍♀️"]

play = ["🔴Your Life Is At 50% use : /curative","🔴Your Life Is At 20% use : /curative","🔴Your Life Is At 40% use : /curative","🧟The Zombies Are Coming Use : / stab or /shoot","🧟🧟‍♂️ There Are Many Zombies 🧟‍♀️🧟 🛡 Use : /shield 🛡","🧟The Zombie Boss Is Coming Use : /bomb ","🧟The Zombies Are Coming Use : /stab or /shoot","🧟🧟‍♂️ There are a lot of Zombies 🧟‍♀️🧟 🛡 Use: /shield 🛡","🔴Your Life is at 60% use: /bandage","🔴Your Life is at 10% use: /bandage ","🧟The Zombies Are Coming Use : /stab or /shoot" ,"🧟The Zombies Are Coming Use : /stab or /shoot","🧟The Zombies Are Coming Use : /stab or /shoot","🧟The Zombies Are Coming Use : /stab or /shoot","🧟The Zombies Are Coming Use : /stab or /shoot","🧟The Zombies Are Coming Use : /stab or /shoot "]

pescar = ["🥈YOU WON THE MEDAL: SILVER FISHERMAN🥈","🥉YOU WON THE MEDAL: BRONZE FISHERMAN🥉","🥉YOU WON THE MEDAL: BRONZE FISHERMAN🥉","🥉YOU WON THE MEDAL: BRONZE FISHERMAN🥉","🥉 YOU WON THE MEDAL: BRONZE FISHERMAN🥉","🟡Event: /carp 🟡","⚫️You Fished 3x Night Moon⚫️(+150 POINTS)","⚫️You Fished 2x Night Moon⚫️(+100 POINTS)", "⚫️You Fished 1x Night Moon⚫️(+50 POINTS)","🟡You Fished 1x Golden Shrimp 🟡 (MULTIPLE POINT)","🟡You Fished 1x Golden Flounder🟡 (MULTIPLE POINT)","🪼🌈You Fished 1x Rainbow Octopus🪼🌈 (EXTRA POINTS)","🐢You Caught 3x Turtle 🐢 (LOSS OF POINTS)","🦑You Caught 1x Giant Squid 🦑 (LEGENDARY)","🦀You Caught 6x Crab 🦀 (COMMON)" ,"🦀You Caught 2x Crab 🦀 (COMMON)","🦀You Caught 8x Crab 🦀 (COMMON)","🪼You Caught 1x Sea Octopus🪼(EPIC)","🦈You Caught 2x Shark🦈 (EPIC)" ,"🦈You Fished 5x Sharks🦈 (EPIC)","🦈You Fished 8x Sharks🦈 (EPIC)","🦈You Fished 1x Sharks🦈 (EPIC)","🐠You Fished 1x Sea Tuna🐠 (LEGENDARY)" ,"🐠You Caught 3x Clown Fish🐠 (LEGENDARY)","🐠You Caught 3x Sea Tuna🐠 (LEGENDARY)","🐠You Caught 1x Clown Fish🐠 (LEGENDARY)","🐠You Caught 8x Clown Fish🐠 ( LEGENDARY)","🐠You Caught 10x Clown Fish🐠 (LEGENDARY)","🐟You Caught 1x Salmon🐟 (RARE)","🧜🏼‍♀️You Caught 5x Mermaid🧜🏼‍♀️(EPIC)","🧜🏼 ‍♀️You Caught 2x Mermaid🧜🏼‍♀️(EPIC)","🧜🏼‍♀️You Caught 1x Mermaid🧜🏼‍♀️(EPIC)","🐟You Caught 3x Salmon🐟 (RARE)","🟡You Fish 1x Golden Tilapia🟡 (MULTIPLE POINT)","☠️🐋You Caught 3x Dead Whale☠️🐋 (LOSS OF POINTS)","🐋You Caught 11x Sea Whale🐋(COMMON)","🐋🌈You Caught 1x Rainbow Whale 🌈🐋 (EXTRA POINTS)","🥈YOU WON THE MEDAL: SILVER FISHERMAN🥈","🥇YOU WON THE MEDAL: GOLD FISHERMAN🥇","🏅YOU WON THE MEDAL: STAR FISHERMAN🏅","💎Event: /shrimp 💎 "]

cantada = ["Can I take a picture of you? It's to show Santa what I want as a gift.","If black was passion and white was affection, what I feel for you would be plaid.","What's the police number? Unfortunately, I'll have to report you for stealing my heart.","My friends bet me that I wouldn't be able to start a conversation with the most beautiful person here. How should we spend their money?","Nice to meet you, I'm a thief. I'm here to steal your heart.","Research shows that being together is a mistake in grammar, but being apart is a mistake of destiny.","If nothing lasts forever, do you want to be my nothing?","Your name Is it Wi-Fi? Because I'm feeling a connection here.","See that star over there? I had it hung for you.","So besides leaving me breathless, what else do you do?","Wow, I have a pain in my chest! I hope it's love, because if it's a heart attack, I'll never see you again!","Roses are red, violets are blue, I don't know how to rhyme, but can I date you?","You were made with candles, honey, red ribbons and roses? Because I found you cute. "]

piada = ["What is Thor's favorite dish? Thorresmo","What did the horse do at the pay phone? Passing a trot","What is the sourest river in the world? The Solimões River","What is the best place in Brazil? The backlands.","What is the wine that doesn't have alcohol? Quail egg "]

hate = ["People hate you 0%","People hate you 20%","People hate you 100%","People hate you 50%","People hate you 45%","People hate you 99 %","People hate you 95%","People hate you 34%","People hate you 77%","People hate you 80%","People hate you 66%","The people hate you 39%","People hate you 20%","People hate you 22%","People hate you 49% "]

amor = ["People love you 0%❤️","People love you 20%❤️","People love you 100%❤️","People love you 50%❤️","People love you 45%❤️"," People love you 99%❤️","People love you 95%❤️","People love you 34%❤️","People love you 77%❤️","People love you 80%❤️"," People love you 66%❤️","People love you 39%❤️","People love you 20%❤️","People love you 22%❤️","People love you 49%❤️ "]


class Bot(BaseBot):
    async def on_start(self, session_metadata: SessionMetadata) -> None:
        print("funcionando")
        await self.highrise.walk_to(Position(11.5, 0.5 , 6.5 , "FrontRight"))
    async def on_user_join(self, user: User, position: Position | AnchorPosition) -> None:
        print(f"{user.username} entrou na sala")   
        await self.highrise.send_whisper(user.id,f"Welcome {user.username} 🤍")
           
        await self.highrise.send_emote("emote-blowkisses")
      
        await self.highrise.send_emote("idle-floating",user.id) 
      
    async def on_chat(self, user: User, message: str) -> None:
        print(f"{user.username}: {message}")  

        if message.startswith("/fish "):
            await self.highrise.send_whisper(user.id,"Are you fishing  🎣...")
          
        if message.lower() == "/fish":
           frase = random.choice(pescar)
           await self.highrise.send_whisper(user.id,frase)
        
        if message.lower() == "/bomb":
           frase = random.choice(bomba)
           await self.highrise.send_whisper(user.id,frase)
        if message.lower() == "/stab":
           frase = random.choice(facada)
           await self.highrise.send_whisper(user.id,frase)
        if message.lower() == "/curative":
           frase = random.choice(curativo)
           await self.highrise.send_whisper(user.id,frase)
        if message.lower() == "/play":
           frase = random.choice(play)
           await self.highrise.send_whisper(user.id,frase)
        if message.lower() == "/shoot":
           frase = random.choice(atirar)
           await self.highrise.send_whisper(user.id,frase)

        if message.lower() == "/my level of madness":
           frase = random.choice(louca)
           await self.highrise.send_whisper(user.id,frase)

        if message.lower() == "/marry me?":
           frase = random.choice(casa)
           await self.highrise.chat(frase)
             
        if message.startswith("/fish"):
           await self.highrise.react("clap",user.id)

        if message.startswith("/carp"):
           await self.highrise.react("clap",user.id)
           await self.highrise.send_whisper(user.id,"🟡You Caught 1x Golden Carp🟡 YOU WON THE MEDAL: (MEGA FISHERMAN)")
          
        if message.startswith("/shrimp"):
           await self.highrise.react("clap",user.id)
           await self.highrise.send_whisper(user.id,"💎You Caught 1x Diamond Shrimp💎YOU WON THE MEDAL: (DIAMANTE MASTER FISHERMAN  )")                                
        if message.startswith("/curative"):
           await self.highrise.react("heart",user.id)

        if message.startswith("/shield"):
           await self.highrise.react("heart",user.id)
           await self.highrise.send_whisper(user.id,f"@{user.username} 🛡 You Used The Shield🛡 ")

        if message.lower() == "/how many people love me":
           frase = random.choice(amor)
           await self.highrise.send_whisper(user.id,frase)
        if message.lower() == "/how many people hate me":
           frase = random.choice(hate)
           await self.highrise.send_whisper(user.id,frase)
      
        if message.lower() == "/joke":
           frase = random.choice(piada)
           await self.highrise.chat(frase)

        if message.lower() == "/sung":
           frase = random.choice(cantada)
           await self.highrise.chat(frase)
          
        if        message.startswith("/tele") or              message.startswith("/tp") or              message.startswith("/fly") or     message.startswith("!tele") or      message.startswith("!tp") or     message.startswith("!fly"):
          if user.username == "Spores, Atekinz, HurIrey, L.O.B.O, Punk_jamie, Roseax, xkeii":            await self.teleporter(message)

        if        message.startswith("/") or              message.startswith("-") or              message.startswith(".") or          message.startswith("!"):
            await self.command_handler(user, message)
          
        if message.startswith("!emoteall"):
          await self.highrise.send_whisper(user.id,"Fashion All , Wrong All , Cutey All , Superpose All , Punk All , Tiktok2 All, Tiktok8 All , Tiktok9 All , Tiktok10 All , Gagging All , Blackpink All , Creepy All , Revelation All , Bashful All , Arabesque All , Party All")

        if message.startswith("!emoteall"):
          await self.highrise.send_whisper(user.id,"Pose3 All , Pose7 All , Pose5 All , Pose1 All , Enthused All , Pose8 All , Sing All , Teleport All , Telekinesis All , Casual All , Icecream All , Watch All")

        if message.startswith("!emoteall"):
          await self.highrise.send_whisper(user.id,"Zombie All , Celebrate All , Kiss All , Bow All , Snowangel All , Confused All , Charging All , Wei All , Cursing All , Greedy All , Russian All , Shop All , Model All , Ren All , Tiktok4 All , Snake All , Uwu All")

        if message.startswith("!emoteall"):
          await self.highrise.send_whisper(user.id,"Skating All , Time All , Gottago All  , Scritchy All , Bitnervous All , Jingle All , Curtsy All , Hot All , Hyped All ,Sleigh All , Surprise All, Repose All , Kawaii All , Touch All , Gift All , Pushit All , Tiktok All , Smooch All , Launch All")
          
        if message.startswith("/emote-id"):
          await self.highrise.send_whisper(user.id,"emote-gravity , idle-uwu , idle-enthusiastic , emote-kiss , emote-float , idle_singing , emote-cute , emote-pose7 , emote-pose8 , emote-fashionista , emote-creepycute , emote-headblowup , emote-shy2 , emote-celebrate , idle-nervous , idle-wild")

        if message.startswith("/emote-id"):
          await self.highrise.send_whisper(user.id,"emote-gift , dance-touch , dance-employee , dance-tiktok11 , emote-salute")
          
        if        message.startswith("!lista") or               message.startswith("!list"):
            await self.highrise.send_whisper(user.id,"!angry ,!thumbsup , !cursing , !flex , !gagging , !celebrate , !blackpink , !tiktok2 , !tiktok9 , !pennywise , !russian , !shop , !enthused , !singing ,!wrong , !guitar , !pinguin , !astronaut , !saunter , !flirt , !creepy , !watch , !revelation")
          
        if        message.startswith("!lista") or               message.startswith("!list"):
            await self.highrise.send_whisper(user.id,"!tiktok10 ,!tiktok8 , !cutey , !pose3 , !pose5 , !pose1 , !pose8 , !pose7  !pose9 , !cute , !superpose , !frog , !snake , !energyball , !maniac , !teleport , !float , !telekinesi , !fight , !wei , !fashion , !boxer , !bashful , !arabesque , !party")
          
        if        message.startswith("!lista") or               message.startswith("!list"):
            await self.highrise.send_whisper(user.id,"!confused , !charging , !snowangel , !hot , !snowball , !curtsy , !bow ,!model , !greedy , !tired , !shy , !wave , !hello , !lau ,!yes , !sad , !no , !kiss , !casual , !ren , !sit , !punk , !zombie , !gravity , !icecream ,!uwu , !sayso , !star")

        if        message.startswith("!lista") or               message.startswith("!list"):
          await self.highrise.send_whisper(user.id,"!skating , !bitnervous , !scritchy , !timejump , !gottago , !jingle , !hyped , !sleigh , !surprise , !repose , !kawaii , !touch , !gift , !pushit , !tiktok , !salute , !attention , !smooch , !launch")
          
        if        message.startswith("/lista") or               message.startswith("/list"):
            await self.highrise.send_whisper(user.id,"/angry ,/thumbsup , /cursing , /flex , /gagging , /celebrate , /blackpink , /tiktok2 , /tiktok9 , /pennywise , /russian , /shop , /enthused , /singing , /wrong , /guitar , /pinguin , /astronaut , /saunter , /flirt , /creepy , /watch , /revelation")
          
        if        message.startswith("/lista") or               message.startswith("/list"):
            await self.highrise.send_whisper(user.id,"/tiktok10 , /tiktok8 , /cutey , /pose3 , /pose5 , /pose1 , /pose8 , /pose7  /pose9 , /cute , /superpose , /frog , /snake , /energyball , /maniac , /teleport , /float , /telekinesi , /fight , /wei , /fashion , /boxer , /bashful , /arabesque , /party")
          
        if        message.startswith("/lista") or               message.startswith("/list"):
            await self.highrise.send_whisper(user.id,"/confused , /charging , /snowangel , /hot , /snowball , /curtsy , /bow ,/model , /greedy , /lust , /tired , /shy , /wave , /hello , /lau , /yes , /sad , /no , /kiss , /casual , /ren ,   /sit , /punk , /zombie , /gravity , /icecream ,/uwu , /sayso , /star")

        if        message.startswith("/lista") or               message.startswith("/list"):
          await self.highrise.send_whisper(user.id,"/skating , /bitnervous , /scritchy , /timejump , /gottago , /jingle , /hyped , /sleigh , /surprise , /repose , /kawaii /touch , /pushit , /gift , /tiktok , /salute , /attention , /smooch , /launch")
        
        if        message.startswith("/lista") or         message.startswith("!emoteall") or message.startswith("!lista"):
            await self.highrise.send_emote("dance-floss")

        if        message.startswith("Ugly") or      message.startswith("ugly") or      message.startswith("deer") or message.startswith("Deer"):
            await self.highrise.chat(f"REPEAT!!! {user.username} 🤬🤬")
            await self.highrise.send_emote("emote-swordfight")

        if        message.startswith("horn") or      message.startswith("Horn") or      message.startswith("Tramp") or message.startswith("tramp"):
            await self.highrise.chat(f"YOUR FATHER!!!  {user.username} 🤬🤬")
            await self.highrise.send_emote("emote-swordfight")

        if        message.startswith("/peoples") or      message.startswith("!peoples"):
            room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"There is   {len(room_users)} peoples in the room")
            await self.highrise.send_emote("dance-floss")
                      
        if        message.startswith("tasty") or      message.startswith("Tasty") or      message.startswith("TASTY"):
            await self.highrise.send_emote("emote-blowkisses")
            await self.highrise.send_emote("idle-uwu", user.id)
            await self.highrise.chat(f"You're hot too  {user.username} 😳👉👈")

        if             message.startswith("!emotes") or message.startswith("/emotes"):
            await self.highrise.send_emote("emote-robot")
            await self.highrise.send_whisper(user.id,f"emotes available from number 1 to 97")

        if        message.startswith("Help") or      message.startswith("/help") or      message.startswith("!help") or message.startswith("help"):
            await self.highrise.chat(f"/lista  , /peoples ,  /emotes, /userinfo  , /emote-id")
            await self.highrise.chat(f"{user.username} all activation codes must be used ( ! or / ) ")
            await self.highrise.send_emote("dance-floss")
          
        if        message.startswith("Beautiful") or      message.startswith("BEAUTIFUL") or      message.startswith("beautiful"):
            await self.highrise.react("heart",user.id,)
            await self.highrise.chat(f"you are very beautiful too, {user.username} 🥰🥰")
            await self.highrise.send_emote("emote-shy",user.id)
            await self.highrise.send_emote("emote-blowkisses")

        if message.startswith("!palma"):
            await self.highrise.react("clap",user.id)
          
        if        message.startswith("Good morning ") or      message.startswith("Good morning") or      message.startswith("good morning") or message.startswith("GOOD MORNING"):
            await self.highrise.send_emote("emote-blowkisses")
            await self.highrise.send_whisper(user.id,f"Good morning {user.username} 😊🌅")

        if        message.startswith("Goodnight") or      message.startswith("goodnight") or      message.startswith("Goodnight") or message.startswith("GOODNIGHT"):
            await self.highrise.send_emote("emote-blowkisses")
            await self.highrise.send_whisper(user.id,f"Goodnight {user.username} 😊🌃🌉")

        if        message.startswith("Good afternoon") or      message.startswith("good afternoon") or      message.startswith("Good afternoon") or message.startswith("GOOD AFTERNOON"):
            await self.highrise.send_emote("emote-blowkisses")
            await self.highrise.send_whisper(user.id,f"Good afternoon {user.username} ☀️")

        if        message.startswith("😡") or      message.startswith("🤬") or      message.startswith("😤") or             message.startswith("🤨") or             message.startswith("😒") or message.startswith("🙄"):
            await self.highrise.send_emote("emote-boxer",user.id)
   
        if        message.startswith("🤔") or      message.startswith("🧐") or      message.startswith("🥸") or             message.startswith("🫤") or message.startswith("😕"):
            await self.highrise.send_emote("emote-confused",user.id)

        if        message.startswith("🤣") or      message.startswith("😂") or             message.startswith("ja") or             message.startswith("Ha") or         message.startswith("Ka") or           message.startswith("Ja") or           message.startswith("ha") or          message.startswith("ks") or             message.startswith("kk") or             message.startswith("Kk") or message.startswith("😁") or message.startswith("😀"):
            await self.highrise.send_emote("emote-laughing",user.id)

        if        message.startswith("😗") or      message.startswith("😘") or      message.startswith("😙") or             message.startswith("💋") or             message.startswith("😚"):
            await self.highrise.send_emote("emote-kiss",user.id)
            await self.highrise.send_emote("emote-blowkisses")

        if        message.startswith("😊") or      message.startswith("🥰") or      message.startswith("😳") or message.startswith("🤗"):
            await self.highrise.send_emote("idle-uwu",user.id)
            await self.highrise.send_emote("emote-blowkisses")

        if        message.startswith("🤢") or      message.startswith("🤮") or      message.startswith("🤧") or             message.startswith("😵‍💫") or message.startswith("🤒"):
            await self.highrise.send_emote("emoji-gagging",user.id)

        if        message.startswith("😱") or      message.startswith("😬") or      message.startswith("😰") or             message.startswith("😫") or message.startswith("😨"):
            await self.highrise.send_emote("idle-nervous",user.id)

        if message.startswith("🤯"):
            await self.highrise.send_emote("emote-headblowup",user.id)

        if        message.startswith("☺️") or      message.startswith("🫣") or       message.startswith("😍") or      message.startswith("🥺") or message.startswith("🥹"):
            await self.highrise.send_emote("emote-shy2",user.id)

        if        message.startswith("😏") or message.startswith("😈"):
            await self.highrise.send_emote("emote-lust",user.id)           

        if        message.startswith("🥵") or message.startswith("🫠"):
            await self.highrise.send_emote("emote-hot",user.id)
          
        if        message.startswith("/thumbs") or        message.startswith("👍") or      message.startswith("!thumbs") or      message.startswith("Thumbs") or message.startswith("Like"):
            await self.highrise.chat(f"👍 For {user.username}")
            await self.highrise.react("thumbs",user.id)                        
        if        message.startswith("/clap") or      message.startswith("!clap") or      message.startswith("Clap") or           message.startswith("👏") or message.startswith("Palma"):
            await self.highrise.react("clap",user.id)
            await self.highrise.chat(f"👏 For {user.username}")
          
        if        message.startswith("/wave") or      message.startswith("!wave") or          message.startswith("👋") or      message.startswith("wave") or message.startswith("Tchau"):
            await self.highrise.react("wave",user.id)
            await self.highrise.chat(f"👋 For {user.username}")
      
        if        message.startswith("/heart") or      message.startswith("!heart") or      message.startswith("Heart") or          message.startswith("❤️") or message.startswith("Amor"):
            await self.highrise.react("heart",user.id)
            await self.highrise.chat(f"❤️ For {user.username}")
          
        if        message.startswith("/wink") or      message.startswith("!wink") or      message.startswith("wink") or           message.startswith("😉") or message.startswith("Piscar"):
            await self.highrise.react("wink",user.id)
            await self.highrise.chat(f"😉 For {user.username}")
          
        if        message.startswith("!wrong") or      message.startswith("/wrong") or      message.startswith("Wrong") or message.startswith("1"):
            await self.highrise.send_emote("dance-wrong",user.id)
            await self.highrise.chat(f" You will like this emote {user.username} 😍")

        if        message.startswith("/fashion") or      message.startswith("fashion") or       message.startswith("!fashion") or      message.startswith("Fashion") or message.startswith("2"):
            await self.highrise.send_emote("emote-fashionista",user.id)
            await self.highrise.chat(f" You will like this emote {user.username} 😍")

        if        message.startswith("/gravity") or      message.startswith("gravity") or       message.startswith("!gravity") or      message.startswith("Gravity") or message.startswith("3"):
            await self.highrise.send_emote("emote-gravity",user.id)
            await self.highrise.chat(f" You will like this emote {user.username} 😍")

        if        message.startswith("/icecream") or      message.startswith("!icecream") or      message.startswith("Icecream") or message.startswith("4"):
            await self.highrise.send_emote("dance-icecream",user.id)
            await self.highrise.chat(f" You will like this emote {user.username} 😍")

        if        message.startswith("/casual") or      message.startswith("!casual") or      message.startswith("Casual") or message.startswith("5"):
            await self.highrise.send_emote("idle-dance-casual",user.id)
            await self.highrise.chat(f" You will like this emote {user.username} 😍")

        if        message.startswith("/kiss") or      message.startswith("!kiss") or      message.startswith("Kiss") or message.startswith("6"):
            await self.highrise.send_emote("emote-kiss",user.id)
            await self.highrise.chat(f" You will like this emote {user.username} 😍")

        if        message.startswith("/no") or      message.startswith("no") or            message.startswith("!no") or      message.startswith("No") or message.startswith("7"):
            await self.highrise.send_emote("emote-no",user.id)
            await self.highrise.chat(f" You will like this emote {user.username} 😍")

        if        message.startswith("/sad") or      message.startswith("!sad") or      message.startswith("Sad") or message.startswith("8"):
            await self.highrise.send_emote("emote-sad",user.id)
            await self.highrise.chat(f" You will like this emote {user.username} 😍")

        if        message.startswith("/yes") or      message.startswith("!yes") or      message.startswith("Yes") or message.startswith("9"):
            await self.highrise.send_emote("emote-yes",user.id)
            await self.highrise.chat(f" You will like this emote {user.username} 😍")

        if        message.startswith("/lau") or      message.startswith("!lau") or      message.startswith("Lau") or message.startswith("10"):
            await self.highrise.send_emote("emote-laughing",user.id)
            await self.highrise.chat(f" You will like this emote {user.username} 😍")

        if        message.startswith("/hello") or      message.startswith("!hello") or      message.startswith("Hello") or message.startswith("11"):
            await self.highrise.send_emote("emote-hello",user.id)
            await self.highrise.chat(f" You will like this emote {user.username} 😍")

        if        message.startswith("/wave") or      message.startswith("!wave") or      message.startswith("Wave") or message.startswith("12"):
            await self.highrise.send_emote("emote-wave",user.id)
            await self.highrise.chat(f" You will like this emote {user.username} 😍")

        if        message.startswith("/shy") or      message.startswith("!shy") or      message.startswith("Shy") or message.startswith("13"):
            await self.highrise.send_emote("emote-shy",user.id)
            await self.highrise.chat(f" You will like this emote {user.username} 😍")

        if        message.startswith("/Tired") or      message.startswith("!Tired") or      message.startswith("Tired") or message.startswith("14"):
            await self.highrise.send_emote("emote-tired",user.id)
            await self.highrise.chat(f" You will like this emote {user.username} 😍")

        if        message.startswith("/flirt") or      message.startswith("!flirt") or      message.startswith("Flirt") or          message.startswith("/Flirty") or           message.startswith("!Flirty") or           message.startswith("Flirty") or       message.startswith("!flirtywave") or    message.startswith("/flirtywave") or    message.startswith("Flirtywave") or message.startswith("15"):
            await self.highrise.send_emote("emote-lust",user.id)
            await self.highrise.chat(f" You will like this emote {user.username} 😍")

        if        message.startswith("/greedy") or      message.startswith("!greedy") or      message.startswith("Greedy") or message.startswith("16"):
            await self.highrise.send_emote("emote-greedy",user.id)
            await self.highrise.chat(f" You will like this emote {user.username} 😍")

        if        message.startswith("/model") or      message.startswith("!model") or      message.startswith("Model") or message.startswith("17"):
            await self.highrise.send_emote("emote-model",user.id)
            await self.highrise.chat(f" You will like this emote {user.username} 😍")

        if        message.startswith("/bow") or      message.startswith("!bow") or      message.startswith("Bow") or message.startswith("18"):
            await self.highrise.send_emote("emote-bow",user.id)
            await self.highrise.chat(f" You will like this emote {user.username} 😍")

        if        message.startswith("/curtsy") or      message.startswith("!curtsy") or      message.startswith("Curtsy") or message.startswith("19"):
            await self.highrise.send_emote("emote-curtsy",user.id)
            await self.highrise.chat(f" You will like this emote {user.username} 😍")

        if        message.startswith("/snowball") or      message.startswith("!snowball") or      message.startswith("Snowball") or message.startswith("20"):
            await self.highrise.send_emote("emote-snowball",user.id)
            await self.highrise.chat(f" You will like this emote {user.username} 😍")

        if        message.startswith("/hot") or      message.startswith("!hot") or      message.startswith("Hot") or message.startswith("21"):
            await self.highrise.send_emote("emote-hot",user.id)
            await self.highrise.chat(f" You will like this emote {user.username} 😍")

        if        message.startswith("/snowangel") or      message.startswith("!snowangel") or      message.startswith("Snowangel") or message.startswith("22"):
            await self.highrise.send_emote("emote-snowangel",user.id)
            await self.highrise.chat(f" You will like this emote {user.username} 😍")

        if        message.startswith("/charging") or      message.startswith("!charging") or      message.startswith("Charging") or message.startswith("23"):
            await self.highrise.send_emote("emote-charging",user.id)
            await self.highrise.chat(f" You will like this emote {user.username} 😍")

        if        message.startswith("/confused") or      message.startswith("!confused") or      message.startswith("Confused") or message.startswith("24"):
            await self.highrise.send_emote("emote-confused",user.id)
            await self.highrise.chat(f" You will like this emote {user.username} 😍")

        if        message.startswith("/telekinesis") or      message.startswith("!telekinesis") or      message.startswith("Telekinesis") or message.startswith("25"):
            await self.highrise.send_emote("emote-telekinesis",user.id)
            await self.highrise.chat(f" You will like this emote {user.username} 😍")

        if        message.startswith("/float") or      message.startswith("!float") or      message.startswith("Float") or message.startswith("26"):
            await self.highrise.send_emote("emote-float",user.id)
            await self.highrise.chat(f" You will like this emote {user.username} 😍")

        if        message.startswith("/teleport") or      message.startswith("!teleport") or      message.startswith("Teleport") or message.startswith("27"):
            await self.highrise.send_emote("emote-teleporting",user.id)
            await self.highrise.chat(f" You will like this emote {user.username} 😍")

        if        message.startswith("/maniac") or      message.startswith("!maniac") or      message.startswith("Maniac") or message.startswith("28"):
            await self.highrise.send_emote("emote-maniac",user.id)
            await self.highrise.chat(f" You will like this emote {user.username} 😍")

        if        message.startswith("/energyball") or      message.startswith("!energyball") or      message.startswith("Energyball") or message.startswith("29"):
            await self.highrise.send_emote("emote-energyball",user.id)
            await self.highrise.chat(f" You will like this emote {user.username} 😍")

        if        message.startswith("/snake") or      message.startswith("!snake") or      message.startswith("Snake") or message.startswith("30"):
            await self.highrise.send_emote("emote-snake",user.id)
            await self.highrise.chat(f" You will like this emote {user.username} 😍")

        if        message.startswith("/frog") or      message.startswith("!frog") or      message.startswith("Frog") or message.startswith("31"):
            await self.highrise.send_emote("emote-frog",user.id)
            await self.highrise.chat(f" You will like this emote {user.username} 😍")

        if        message.startswith("/superpose") or      message.startswith("!superpose") or      message.startswith("Superpose") or message.startswith("32"):
            await self.highrise.send_emote("emote-superpose",user.id)
            await self.highrise.chat(f" You will like this emote {user.username} 😍")

        if        message.startswith("/cute") or      message.startswith("!cute") or      message.startswith("Cute") or message.startswith("33"):
            await self.highrise.send_emote("emote-cute",user.id)
            await self.highrise.chat(f" You will like this emote {user.username} 😍")

        if        message.startswith("/pose7") or      message.startswith("!pose7") or      message.startswith("Pose7") or message.startswith("34"):
            await self.highrise.send_emote("emote-pose7",user.id)
            await self.highrise.chat(f" You will like this emote {user.username} 😍")

        if        message.startswith("/pose8") or      message.startswith("!pose8") or      message.startswith("Pose8") or message.startswith("35"):
            await self.highrise.send_emote("emote-pose8",user.id)
            await self.highrise.chat(f" You will like this emote {user.username} 😍")

        if        message.startswith("/pose1") or      message.startswith("!pose1") or      message.startswith("Pose1") or message.startswith("36"):
            await self.highrise.send_emote("emote-pose1",user.id)
            await self.highrise.chat(f" You will like this emote {user.username} 😍")

        if        message.startswith("/pose5") or      message.startswith("!pose5") or      message.startswith("Pose5") or message.startswith("37"):
            await self.highrise.send_emote("emote-pose5",user.id)
            await self.highrise.chat(f" You will like this emote {user.username} 😍")

        if        message.startswith("/pose3") or      message.startswith("!pose3") or      message.startswith("Pose3") or message.startswith("38"):
            await self.highrise.send_emote("emote-pose3",user.id)
            await self.highrise.chat(f" You will like this emote {user.username} 😍")

        if        message.startswith("/cutey") or      message.startswith("!cutey") or      message.startswith("Cutey") or message.startswith("39"):
            await self.highrise.send_emote("emote-cutey",user.id)
            await self.highrise.chat(f" You will like this emote {user.username} 😍")
        if        message.startswith("/tik10") or      message.startswith("!tik10") or      message.startswith("Tik10") or message.startswith("40"):
            await self.highrise.send_emote("dance-tiktok10",user.id)
            await self.highrise.chat(f" You will like this emote {user.username} 😍")

        if        message.startswith("/sing") or      message.startswith("!sing") or          message.startswith("Sing") or           message.startswith("Singing") or       message.startswith("/singing") or   message.startswith("!singing") or message.startswith("41"):
            await self.highrise.send_emote("idle_singing",user.id)
            await self.highrise.chat(f" You will like this emote {user.username} 😍")

        if        message.startswith("/enthused") or      message.startswith("!enthused") or      message.startswith("Enthused") or message.startswith("42"):
            await self.highrise.send_emote("idle-enthusiastic",user.id)
            await self.highrise.chat(f" You will like this emote {user.username} 😍")

        if        message.startswith("/shop") or      message.startswith("!shop") or      message.startswith("Shop") or message.startswith("43"):
            await self.highrise.send_emote("dance-shoppingcart",user.id)
            await self.highrise.chat(f" You will like this emote {user.username} 😍")

        if        message.startswith("/russian") or      message.startswith("!russian") or      message.startswith("Russian") or message.startswith("44"):
            await self.highrise.send_emote("dance-russian",user.id)
            await self.highrise.chat(f" You will like this emote {user.username} 😍")

        if        message.startswith("/pennywise") or      message.startswith("!pennywise") or      message.startswith("Pennywise") or message.startswith("45"):
            await self.highrise.send_emote("dance-pennywise",user.id)
            await self.highrise.chat(f" You will like this emote {user.username} 😍")

        if        message.startswith("/tik2") or      message.startswith("!tik2") or      message.startswith("Tik2") or message.startswith("46"):
            await self.highrise.send_emote("dance-tiktok2",user.id)
            await self.highrise.chat(f" You will like this emote {user.username} 😍")

        if        message.startswith("/blackpink") or      message.startswith("!blackpink") or      message.startswith("Blackpink") or message.startswith("47"):
            await self.highrise.send_emote("dance-blackpink",user.id)
            await self.highrise.chat(f" You will like this emote {user.username} 😍")

        if        message.startswith("/celebrate") or      message.startswith("!celebrate") or      message.startswith("Celebrate") or message.startswith("48"):
            await self.highrise.send_emote("emoji-celebrate",user.id)
            await self.highrise.chat(f" You will like this emote {user.username} 😍")

        if        message.startswith("/gagging") or      message.startswith("!gagging") or      message.startswith("Gagging") or message.startswith("49"):
            await self.highrise.send_emote("emoji-gagging",user.id)
            await self.highrise.chat(f" You will like this emote {user.username} 😍")

        if        message.startswith("/flex") or      message.startswith("!flex") or      message.startswith("Flex") or message.startswith("50"):
            await self.highrise.send_emote("emoji-flex",user.id)
            await self.highrise.chat(f" You will like this emote {user.username} 😍")

        if        message.startswith("/cursing") or      message.startswith("!cursing") or      message.startswith("Cursing") or message.startswith("51"):
            await self.highrise.send_emote("emoji-cursing",user.id)
            await self.highrise.chat(f" You will like this emote {user.username} 😍")

        if        message.startswith("/thumbsup") or      message.startswith("!thumbsup") or      message.startswith("Thumbsup") or message.startswith("52"):
            await self.highrise.send_emote("emoji-thumbsup",user.id)
            await self.highrise.chat(f" You will like this emote {user.username} 😍")

        if        message.startswith("/angry") or      message.startswith("!angry") or      message.startswith("Angry") or message.startswith("53"):
            await self.highrise.send_emote("emoji-angry",user.id)
            await self.highrise.chat(f" You will like this emote {user.username} 😍")

        if        message.startswith("/punk") or      message.startswith("!punk") or      message.startswith("Punk") or message.startswith("54"):
            await self.highrise.send_emote("emote-punkguitar",user.id)
            await self.highrise.chat(f" You will like this emote {user.username} 😍")

        if        message.startswith("/zombie") or      message.startswith("!zombie") or      message.startswith("Zombie") or message.startswith("55"):
            await self.highrise.send_emote("emote-zombierun",user.id)
            await self.highrise.chat(f" You will like this emote {user.username} 😍")

        if        message.startswith("/sit") or      message.startswith("!sit") or      message.startswith("Sit") or message.startswith("56"):
            await self.highrise.send_emote("idle-loop-sitfloor",user.id)
            await self.highrise.chat(f" You will like this emote {user.username} 😍")

        if        message.startswith("/fight") or      message.startswith("!fight") or      message.startswith("Fight") or message.startswith("57"):
            await self.highrise.send_emote("emote-swordfight",user.id)
            await self.highrise.chat(f" You will like this emote {user.username} 😍")

        if        message.startswith("/ren") or      message.startswith("!ren") or      message.startswith("Ren") or message.startswith("58"):
            await self.highrise.send_emote("dance-macarena",user.id)
            await self.highrise.chat(f" You will like this emote {user.username} 😍")

        if        message.startswith("/wei") or      message.startswith("!wei") or      message.startswith("Wei") or message.startswith("59"):
            await self.highrise.send_emote("dance-weird",user.id)
            await self.highrise.chat(f" You will like this emote {user.username} 😍")

        if        message.startswith("/tik8") or      message.startswith("!tik8") or      message.startswith("Tik8") or           message.startswith("/savage") or           message.startswith("!savage") or           message.startswith("Savage") or message.startswith("60"):
            await self.highrise.send_emote("dance-tiktok8",user.id)
            await self.highrise.chat(f" You will like this emote {user.username} 😍")

        if        message.startswith("/tik9") or      message.startswith("!tik9") or      message.startswith("Tik9") or           message.startswith("/viral") or           message.startswith("!viral") or           message.startswith("Viral") or  message.startswith("61"):
            await self.highrise.send_emote("dance-tiktok9",user.id)
            await self.highrise.chat(f" You will like this emote {user.username} 😍")

        if        message.startswith("/uwu") or      message.startswith("!uwu") or      message.startswith("Uwu") or message.startswith("62"):
            await self.highrise.send_emote("idle-uwu",user.id)
            await self.highrise.chat(f" You will like this emote {user.username} 😍")

        if        message.startswith("/tik4") or      message.startswith("!tik4") or      message.startswith("Tik4") or               message.startswith("/sayso") or               message.startswith("!sayso") or               message.startswith("Sayso") or message.startswith("63"):
            await self.highrise.send_emote("idle-dance-tiktok4",user.id)
            await self.highrise.chat(f" You will like this emote {user.username} 😍")

        if        message.startswith("/star") or      message.startswith("!star") or      message.startswith("Star") or message.startswith("64"):
            await self.highrise.send_emote("emote-stargazer",user.id)
            await self.highrise.chat(f" You will like this emote {user.username} 😍")

        if        message.startswith("/pose9") or      message.startswith("!pose9") or      message.startswith("Pose9") or message.startswith("65"):
            await self.highrise.send_emote("emote-pose9",user.id)
            await self.highrise.chat(f" You will like this emote {user.username} 😍")

        if        message.startswith("/boxer") or      message.startswith("!boxer") or      message.startswith("Boxer") or message.startswith("66"):
            await self.highrise.send_emote("emote-boxer",user.id)
            await self.highrise.chat(f" You will like this emote {user.username} 😍")

        if        message.startswith("/guitar") or      message.startswith("!guitar") or      message.startswith("Guitar") or message.startswith("67"):
            await self.highrise.send_emote("idle-guitar",user.id)
            await self.highrise.chat(f" You will like this emote {user.username} 😍")

        if        message.startswith("/penguin") or      message.startswith("!penguin") or      message.startswith("Penguin") or message.startswith("68"):
            await self.highrise.send_emote("dance-pinguin",user.id)
            await self.highrise.chat(f" You will like this emote {user.username} 😍")

        if        message.startswith("/astronaut") or      message.startswith("!astronaut") or      message.startswith("Astronaut") or message.startswith("69"):
            await self.highrise.send_emote("emote-astronaut",user.id)
            await self.highrise.chat(f" You will like this emote {user.username} 😍")

        if        message.startswith("/saunter") or      message.startswith("!saunter") or      message.startswith("Saunter") or               message.startswith("/anime") or               message.startswith("!anime") or               message.startswith("Anime") or   message.startswith("70"):
            await self.highrise.send_emote("dance-anime",user.id)
            await self.highrise.chat(f" You will like this emote {user.username} 😍")

        if        message.startswith("/creepy") or      message.startswith("!creepy") or      message.startswith("Creepy") or message.startswith("71"):
            await self.highrise.send_emote("dance-creepypuppet",user.id)
            await self.highrise.chat(f" You will like this emote {user.username} 😍")

        if        message.startswith("/watch") or      message.startswith("!watch") or      message.startswith("Watch") or message.startswith("72"):
            await self.highrise.send_emote("emote-creepycute",user.id)
            await self.highrise.chat(f" You will like this emote {user.username} 😍")

        if        message.startswith("/revelations") or      message.startswith("!revelations") or      message.startswith("Revelations") or message.startswith("73"):
            await self.highrise.send_emote("emote-headblowup",user.id)
            await self.highrise.chat(f" You will like this emote {user.username} 😍")

        if        message.startswith("/bashful") or      message.startswith("!bashful") or      message.startswith("Bashful") or message.startswith("74"):
            await self.highrise.send_emote("emote-shy2",user.id)
            await self.highrise.chat(f" You will like this emote {user.username} 😍")

        if        message.startswith("/arabesque") or      message.startswith("!arabesque") or      message.startswith("Arabesque") or message.startswith("75"):
            await self.highrise.send_emote("emote-pose10",user.id)
            await self.highrise.chat(f" You will like this emote {user.username} 😍")

        if        message.startswith("/party") or      message.startswith("!party") or      message.startswith("Party") or message.startswith("76"):
            await self.highrise.send_emote("emote-celebrate",user.id)
            await self.highrise.chat(f" You will like this emote {user.username} 😍")

        if        message.startswith("/skating") or      message.startswith("!skating") or      message.startswith("Skating") or message.startswith("77"):
            await self.highrise.send_emote("emote-iceskating",user.id)
            await self.highrise.chat(f" You will like this emote {user.username} 😍")

        if        message.startswith("/scritchy") or      message.startswith("!scritchy") or      message.startswith("Scritchy") or message.startswith("78"):
            await self.highrise.send_emote("idle-wild",user.id)
            await self.highrise.chat(f" You will like this emote {user.username} 😍")

        if        message.startswith("/bitnervous") or      message.startswith("!bitnervous") or      message.startswith("Bitnervous") or               message.startswith("!nervous") or               message.startswith("/nervous") or               message.startswith("Nervous") or message.startswith("79"):
            await self.highrise.send_emote("idle-nervous",user.id)
            await self.highrise.chat(f" You will like this emote {user.username} 😍")

        if        message.startswith("/timejump") or      message.startswith("!timejump") or      message.startswith("Timejump") or message.startswith("80"):
            await self.highrise.send_emote("emote-timejump",user.id)
        
        if        message.startswith("/gottago") or      message.startswith("!gottago") or      message.startswith("Gottago") or message.startswith("81"):
            await self.highrise.send_emote("idle-toilet",user.id)

        if        message.startswith("/jingle") or      message.startswith("!jingle") or      message.startswith("Jingle") or message.startswith("82"):
            await self.highrise.send_emote("dance-jinglebell",user.id)
            await self.highrise.chat(f" You will like this emote {user.username} 😍")

        if        message.startswith("/hyped") or      message.startswith("!hyped") or      message.startswith("Hyped") or message.startswith("83"):
            await self.highrise.send_emote("emote-hyped",user.id)
            await self.highrise.chat(f" You will like this emote {user.username} 😍")

        if        message.startswith("/sleigh") or      message.startswith("!sleigh") or        message.startswith("sleigh") or      message.startswith("Sleigh") or message.startswith("84"):
            await self.highrise.send_emote("emote-sleigh",user.id)
            await self.highrise.chat(f" You will like this emote {user.username} 😍")

        if        message.startswith("/surprise") or      message.startswith("!surprise") or      message.startswith("surprise") or      message.startswith("Surprise") or message.startswith("85"):
            await self.highrise.send_emote("emote-pose6",user.id)
            await self.highrise.chat(f" You will like this emote {user.username} 😍")
          
        if        message.startswith("/repose") or      message.startswith("!repose") or        message.startswith("repose") or      message.startswith("Repose") or message.startswith("86"):
            await self.highrise.send_emote("sit-relaxed",user.id)
            
        if        message.startswith("/kawaii") or      message.startswith("!kawaii") or        message.startswith("kawaii") or       message.startswith("Kawaii") or message.startswith("87"):
            await self.highrise.send_emote("dance-kawai",user.id)

        if        message.startswith("/touch") or      message.startswith("!touch") or         message.startswith("touch") or      message.startswith("Touch") or message.startswith("88"):
            await self.highrise.send_emote("dance-touch",user.id)

        if        message.startswith("/gift") or      message.startswith("!gift") or          message.startswith("gift") or      message.startswith("Gift") or message.startswith("89"):
            await self.highrise.send_emote("emote-gift",user.id)

        if        message.startswith("/pushit") or      message.startswith("!pushit") or        message.startswith("pushit") or      message.startswith("Pushit") or message.startswith("90"):
            await self.highrise.send_emote("dance-employee",user.id)

        if        message.startswith("salute") or      message.startswith("!salute") or        message.startswith("salute") or      message.startswith("Salute") or message.startswith("91"):
            await self.highrise.send_emote("emote-cutesalute",user.id)

        if        message.startswith("/attention") or      message.startswith("!attention") or        message.startswith("attention") or      message.startswith("Attention") or message.startswith("92"):
            await self.highrise.send_emote("emote-salute",user.id)                                                                   

        if        message.startswith("/tiktok") or      message.startswith("!tiktok") or        message.startswith("tiktok") or    message.startswith("Tiktok") or message.startswith("93"):
            await self.highrise.send_emote("dance-tiktok11",user.id)

        if        message.startswith("/smooch") or      message.startswith("!smooch") or        message.startswith("smooch") or    message.startswith("Smooch") or message.startswith("94"):
            await self.highrise.send_emote("emote-kissing-bound",user.id)

        if        message.startswith("/launch") or      message.startswith("!launch") or        message.startswith("launch") or   message.startswith("Launch") or message.startswith("95"):
            await self.highrise.send_emote("emote-launch",user.id)

        if        message.startswith("/fairyfloat") or      message.startswith("!fairyfloat") or        message.startswith("fairyfloat") or    message.startswith("Fairyfloat") or message.startswith("96"):
            await self.highrise.send_emote("idle-floating",user.id)

        if        message.startswith("/fairytwirl") or      message.startswith("!fairytwirl") or        message.startswith("fairytwirl") or    message.startswith("Fairytwirl") or message.startswith("97"):
            await self.highrise.send_emote("emote-looping",user.id)

        if message.startswith("Fairyfloat All"):
          if user.username == "Spores":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("idle-floating", roomUser.id)

        if message.startswith("Fairytwirl All"):
          if user.username == "Spores":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-looping", roomUser.id)

        if message.startswith("Launch All"):
          if user.username == "Spores":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-launch", roomUser.id)

        if message.startswith("Smooch All"):
          if user.username == "Spores":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-kissing-bound", roomUser.id)

        if message.startswith("Pushit All"):
          if user.username == "Spores":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-employee", roomUser.id)

        if message.startswith("Gift All"):
          if user.username == "Spores":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-gift", roomUser.id)

        if message.startswith("Attention All"):
          if user.username == "Spores":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-salute", roomUser.id)

        if message.startswith("Salute All"):
          if user.username == "Spores":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-cutesalute", roomUser.id)

        if message.startswith("Tiktok All"):
          if user.username == "Spores":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-tiktok11", roomUser.id)
          
        if message.startswith("Touch All"):
          if user.username == "Spores":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-touch", roomUser.id)
              
        if message.startswith("Kawaii All"):
          if user.username == "Spores":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-kawai", roomUser.id)
          
        if message.startswith("Hot All"):
          if user.username == "Spores":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-hot", roomUser.id)
      
      
        if message.startswith("Curtsy All"):
          if user.username == "Spores":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-curtsy", roomUser.id)

        if message.startswith("Surprise All"):
          if user.username == "Spores":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-pose6", roomUser.id)

        if message.startswith("Jingle All"):
          if user.username == "Spores":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-jinglebell", roomUser.id)

        if message.startswith("Creepy All"):
          if user.username == "Spores":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-creepypuppet", roomUser.id)

        if message.startswith("Bitnervous All"):
          if user.username == "Spores":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("idle-nervous", roomUser.id)

        if message.startswith("Scritchy All"):
          if user.username == "Spores":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("idle-wild", roomUser.id)
              
        if message.startswith("Fashion All"):
          if user.username == "Spores":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-fashionista", roomUser.id)
                
        if message.startswith("Wrong All"):
          if user.username == "Spores":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-wrong", roomUser.id)

        if message.startswith("Cutey All"):
          if user.username == "Spores":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-cutey", roomUser.id)

        if message.startswith("Hyped All"):
          if user.username == "Spores":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-hyped", roomUser.id)
                
        if message.startswith("Superpose All"):
          if user.username == "Spores":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-superpose", roomUser.id)

        if message.startswith("Punk All"):
          if user.username == "Spores":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-punkguitar", roomUser.id) 
                
        if message.startswith("Tiktok2 All"):
          if user.username == "Spores":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-tiktok2", roomUser.id)
                
        if                            message.startswith("Savage All") or   message.startswith("Tiktok8 All"):
          if user.username == "Spores":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-tiktok8", roomUser.id)
                
        if message.startswith("Tiktok10 All"):
          if user.username == "Spores":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-tiktok10", roomUser.id)
                
        if                            message.startswith("Viral All") or          message.startswith("Viralgroove All") or  message.startswith("Tiktok9 All"):
          if user.username == "Spores":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-tiktok9", roomUser.id)
                
        if message.startswith("Blackpink All"):
          if user.username == "Spores":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-blackpink", roomUser.id)             
        if message.startswith("Gagging All"):
          if user.username == "Spores":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emoji-gagging", roomUser.id)

        if message.startswith("Pose3 All"):
          if user.username == "Spores":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-pose3", roomUser.id)

        if message.startswith("Pose7 All"):
          if user.username == "Spores":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-pose7", roomUser.id)

        if message.startswith("Pose5 All"):
          if user.username == "Spores":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-pose5", roomUser.id)

        if message.startswith("Pose1 All"):
          if user.username == "Spores":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-pose1", roomUser.id)

        if message.startswith("Pose8 All"):
          if user.username == "Spores":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-pose8", roomUser.id)
     
        if message.startswith("Enthused All"):
          if user.username == "Spores":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("idle-enthusiastic", roomUser.id)
                
        if message.startswith("Sing All"):
          if user.username == "Spores":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("idle_singing", roomUser.id)

        if message.startswith("Teleport All"):
          if user.username == "Spores":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-teleporting", roomUser.id)
                
        if message.startswith("Telekinesis All"):
          if user.username == "Spores":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-telekinesis", roomUser.id)

        if message.startswith("Casual All"):
          if user.username == "Spores":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("idle-dance-casual", roomUser.id)
                
        if message.startswith("Icecream All"):
          if user.username == "Spores":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-icecream", roomUser.id)
                   
        if message.startswith("Zombie All"):
          if user.username == "Spores":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-zombierun", roomUser.id)

        if message.startswith("Celebrate All"):
          if user.username == "Spores":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emoji-celebrate", roomUser.id)

        if message.startswith("Kiss All"):
          if user.username == "Spores":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-kiss", roomUser.id)

        if message.startswith("Snowangel All"):
          if user.username == "Spores":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-snowangel", roomUser.id)

        if message.startswith("Bow All"):
          if user.username == "Spores":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-bow", roomUser.id)

        if message.startswith("Skating All"):
          if user.username == "Spores":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-iceskating", roomUser.id)

        if message.startswith("Confused All"):
          if user.username == "Spores":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-confused", roomUser.id)

        if message.startswith("Charging All"):
          if user.username == "Spores":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-charging", roomUser.id)

        if message.startswith("Wei All"):
          if user.username == "Spores":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-weird", roomUser.id)

        if message.startswith("Greedy All"):
          if user.username == "Spores":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-greedy", roomUser.id)

        if message.startswith("Cursing All"):
          if user.username == "Spores":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emoji-cursing", roomUser.id)

        if message.startswith("Russian All"):
          if user.username == "Spores":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-russian", roomUser.id)

        if message.startswith("Repose All"):
          if user.username == "Spores":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("sit-relaxed", roomUser.id)
                
        if message.startswith("Shop All"):
          if user.username == "Spores":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-shoppingcart", roomUser.id)

        if message.startswith("Ren All"):
          if user.username == "Spores":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-macarena", roomUser.id)

        if message.startswith("Snake All"):
          if user.username == "Spores":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-snake", roomUser.id)

        if message.startswith("Model All"):
          if user.username == "Spores":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-model", roomUser.id)

        if message.startswith("Sleigh All"):
          if user.username == "Spores":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-sleigh", roomUser.id)

        if message.startswith("Tiktok4 All"):
          if user.username == "Spores":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("idle-dance-tiktok4", roomUser.id)

        if message.startswith("Uwu All"):
          if user.username == "Spores":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("idle-uwu", roomUser.id)

        if message.startswith("Star All"):
          if user.username == "Spores":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-stargazer", roomUser.id)

        if message.startswith("Pose9 All"):
          if user.username == "Spores":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-pose9", roomUser.id)

        if message.startswith("Boxer All"):
          if user.username == "Spores":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-boxer", roomUser.id)

        if message.startswith("Guitar All"):
          if user.username == "Spores":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("idle-guitar", roomUser.id)

        if message.startswith("Penguin All"):
          if user.username == "Spores":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-pinguin", roomUser.id)

        if message.startswith("Zero All"):
          if user.username == "Spores":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-astronaut", roomUser.id)

        if message.startswith("Saunter All"):
          if user.username == "Spores":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-anime", roomUser.id)

        if message.startswith("Flirt All"):
          if user.username == "Spores":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-lust", roomUser.id)

        if message.startswith("Watch All"):
          if user.username == "Spores":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-creepycute", roomUser.id)

        if message.startswith("Revelation All"):
          if user.username == "Spores":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-headblowup", roomUser.id)

        if message.startswith("Bashful All"):
          if user.username == "Spores":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-shy2", roomUser.id)

        if message.startswith("Arabesque All"):
          if user.username == "Spores":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-pose10", roomUser.id)

        if message.startswith("Party All"):
          if user.username == "Spores":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-celebrate", roomUser.id)

        if message.startswith("Time All"):
          if user.username == "Atekinz":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-timejump", roomUser.id)

        if message.startswith("Gottago All"):
          if user.username == "Atekinz":
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("idle-toilet", roomUser.id)
                    
        if        message.startswith("/tp") or      message.startswith("!tp") or      message.startswith("/tele") or          message.startswith("Tp") or          message.startswith("Tele") or  message.startswith("!tele"):
          target_username =         message.split("@")[-1].strip()
          await                     self.teleport_to_user(user, target_username)

        if                            message.startswith("Summon") or         message.startswith("Summom") or         message.startswith("!summom") or        message.startswith("/summom") or        message.startswith("/summon") or  message.startswith("!summon"):
          if user.username == "Atekinz":
           target_username = message.split("@")[-1].strip()
           await self.teleport_user_next_to(target_username, user)
    
        if message.startswith("kick"):
          if user.username == "Atekinz":
              pass
          else:
              await self.highrise.chat("Voce não tem permissao para usar esse comando.")
              return
          #separete message into parts
          parts = message.split()
          #check if message is valid "kick @username"
          if len(parts) != 2:
              await self.highrise.chat("formato de banimento errado.")
              return
          #checks if there's a @ in the message
          if "@" not in parts[1]:
              username = parts[1]
          else:
              username = parts[1][1:]
          #check if user is in room
          room_users = (await self.highrise.get_room_users()).content
          for room_user, pos in room_users:
              if room_user.username.lower() == username.lower():
                  user_id = room_user.id
                  break
          if "user_id" not in locals():
              await self.highrise.chat("usuario não encontrado, porfavor arrume a cordenada do codigo")
              return
          #kick user
          try:
              await self.highrise.moderate_room(user_id, "kick")
          except Exception as e:
              await self.highrise.chat(f"{e}")
              return
          #send message to chat
          await self.highrise.chat(f"{username} Foi Banido da sala!!")

    async def teleport(self, user: User, position: Position):
        try:
            await self.highrise.teleport(user.id, position)
        except Exception as e:
            print(f"Caught Teleport Error: {e}")

    async def teleport_to_user(self, user: User, target_username: str) -> None:
        try:
            room_users = await self.highrise.get_room_users()
            for target, position in room_users.content:
                if target.username.lower() == target_username.lower():
                    z = position.z
                    new_z = z - 1
                    await self.teleport(user, Position(position.x, position.y, new_z, position.facing))
                    break
        except Exception as e:
            print(f"An error occurred while teleporting to {target_username}: {e}")

    async def teleport_user_next_to(self, target_username: str, requester_user: User) -> None:
        try:
            # Get the position of the requester_user
            room_users = await self.highrise.get_room_users()
            requester_position = None
            for user, position in room_users.content:
                if user.id == requester_user.id:
                    requester_position = position
                    break

            # Find the target user and their position
            for user, position in room_users.content:
                if user.username.lower() == target_username.lower():
                    z = requester_position.z
                    new_z = z + 1  # Example: Move +1 on the z-axis (upwards)
                    await self.teleport(user, Position(requester_position.x, requester_position.y, new_z, requester_position.facing))
                    break
        except Exception as e:
            print(f"An error occurred while teleporting {target_username} next to {requester_user.username}: {e}")
          
    async def teleporter(self, message: str)-> None:
        """
            Teleports the user to the specified user or coordinate
            Usage: /teleport <username> <x,y,z>
                                                                """
        #separates the message into parts
        #part 1 is the command "/teleport"
        #part 2 is the name of the user to teleport to (if it exists)
        #part 3 is the coordinates to teleport to (if it exists)
        try:
            command, username, coordinate = message.split(" ")
        except:
            
            return
        
        #checks if the user is in the room
        room_users = (await self.highrise.get_room_users()).content
        for user in room_users:
            if user[0].username.lower() == username.lower():
                user_id = user[0].id
                break
        #if the user_id isn't defined, the user isn't in the room
        if "user_id" not in locals():
            
            return
            
        #checks if the coordinate is in the correct format (x,y,z)
        try:
            x, y, z = coordinate.split(",")
        except:
          
            return
        
        #teleports the user to the specified coordinate
        await self.highrise.teleport(user_id = user_id, dest = Position(float(x), float(y), float(z)))

    async def command_handler(self, user: User, message: str):
        parts = message.split(" ")
        command = parts[0][1:]
        functions_folder = "functions"
        # Check if the function exists in the module
        for file_name in os.listdir(functions_folder):
            if file_name.endswith(".py"):
                module_name = file_name[:-3]  # Remove the '.py' extension
                module_path = os.path.join(functions_folder, file_name)
                
                # Load the module
                spec = importlib.util.spec_from_file_location(module_name, module_path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                
                # Check if the function exists in the module
                if hasattr(module, command) and callable(getattr(module, command)):
                    function = getattr(module, command)
                    await function(self, user, message)
        
        # If no matching function is found
        return              
               
    async def on_reaction(self, user: User, reaction: Reaction, receiver: User) -> None:
        print(f"{user.username} enviou a reação  {reaction} para {receiver.username}")

        if reaction.startswith("wink"):
              await self.highrise.send_emote("idle-uwu",receiver.id)
              await self.highrise.send_emote("emote-lust",user.id)       
              await self.highrise.send_emote("emote-ghost-idle")          
          
        if reaction.startswith("heart"):
              await self.highrise.send_emote("emote-kissing-bound",receiver.id)         
              await self.highrise.send_emote("emote-kissing-bound",user.id)
              await self.highrise.send_emote("emote-gordonshuffle")
                        
        if reaction.startswith("wave"):
              await self.highrise.send_emote("emote-confused",receiver.id)             
              await self.highrise.send_emote("emote-hello",user.id)      
              await self.highrise.send_emote("dance-smoothwalk")
              
        if reaction.startswith("thumbs"):
              await self.highrise.send_emote("emote-pose1",receiver.id)               
              await self.highrise.send_emote("dance-spiritual")   

        if reaction.startswith("clap"):
              await self.highrise.send_emote("idle-enthusiastic",receiver.id)          
              await self.highrise.send_emote("emoji-celebrate",user.id)
              await self.highrise.send_emote("dance-breakdance") 
              
    async def on_whisper(self, user: User, message: str) -> None:
        print(f"{user.username} whispered: {message}")

        if        message.startswith("/tele") or              message.startswith("/tp") or              message.startswith("/fly") or     message.startswith("!tele") or      message.startswith("!tp") or     message.startswith("!fly"):
          if user.username == "Atekinz":
            await self.teleporter(message)

        if        message.startswith("/") or              message.startswith("-") or              message.startswith(".") or          message.startswith("!"):
            await self.command_handler(user, message)

        if                            message.startswith("Summon") or         message.startswith("Summom") or         message.startswith("!summom") or        message.startswith("/summom") or        message.startswith("/summon") or  message.startswith("!summon"):
          if user.username == "Atekinz":
           target_username = message.split("@")[-1].strip()
           await self.teleport_user_next_to(target_username, user)
            
        if              message.startswith("Carteira") or       message.startswith("carteira"):
          if user.username == "Atekinz":
            wallet = (await self.highrise.get_wallet()).content
            await self.highrise.send_whisper(user.id,f"AMOUNT : {wallet[0].amount} {wallet[0].type}")
            await self.highrise.send_emote("emote-blowkisses")
            
    async def on_user_move(self, user: User, pos: Position) -> None:
        print (f"{user.username} moved to {pos}")

    async def on_emote(self, user: User, emote_id: str, receiver: User | None) -> None:
        print(f"{user.username} emoted: {emote_id}")

    async def on_user_leave(self, user: User) -> None:
        print(f"{user.username} saiu da sala")
        await self.highrise.chat(f"Görüşürüz @{user.username}! 👋🏻")
        await self.highrise.send_emote("emote-blowkisses")
# -*- coding: utf-8 -*-

# (c) @maybeslow (Github) | https://t.me/birsamil | @birsamil (Telegram)

# ==============================================================================
#
# Project: EtiketTaggerBot
# Copyright (C) 2021-2022 by maybeslow@Github, < https://github.com/maybeslow >.
#
# This file is part of < https://github.com/maybeslow/Tagger > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see <https://github.com/maybeslow >
#
# All rights reserved.
#
# ==============================================================================
#
# Proje: EtiketTaggerBot
# Telif Hakkı (C) 2021-2022 maybeslow@Github, <https://github.com/maybeslow>.
#
# Bu dosya <https://github.com/maybeslow/Tagger> projesinin bir parçası,
# ve "GNU V3.0 Lisans Sözleşmesi" kapsamında yayınlanır.
# Lütfen bkz. <https://github.com/maybeslow/Tagger >
#
# Her hakkı saklıdır.
#
# ========================================================================




import os
import heroku3
from telethon import TelegramClient, events, Button
from telethon.sync import TelegramClient, events
import random

#
# 
api_id = "14209813" #my.telegram.org/apps adresinden alabilirsiniz 
api_hash = "f6fc4af6fa07543ace7bcf771e89cdd2" #my.telegram.org/apps adresinden alabilirsiniz
bot_token = "6716666574:AAEgio4eFtQW-2KzpfI6OCiqb4m9UTsMLng" #botfatherdan alabilirsiniz

client = TelegramClient("Samil", api_id, api_hash).start(bot_token=bot_token)

USERNAME = "etiketsudenaz_bot" #botunuzun kullanıcı adı
log_qrup = -1001831099952 #log qrupunuzun idsi
startmesaj = "💌 arkadaşlarınızı nasıl etiketlemek istersiniz ...\n📚 ben gruplarınız için parliament tarafından özel geliştirilen bir botum" #start mesajınız
komutlar = "🇦🇿 Bütün etiketler ;\n\n» /utag   <  mesaj  >\n   - üyeleri 5'li etiketler .\n\n» /tag   <  mesaj  >\n   - üyeleri tek tek etiketler .\n\n» /atag   <  mesaj  >\n   - Adminleri etiketler .\n\n» /etag   <  mesaj  >\n   - üyeleri emoji ile etiketler .\n\n» /stag   <  mesaj  >\n   - üyeleri güzel söz ile etiketler .\n\n» /cancel = >\n   - etiketleme işlemi durdurulur ." #komutların olduğu mesaj
qrupstart = "• şuan aktif çalışmaktayım  . . .\n\n• üyeleri etiketlemek için grubunuza ekleyin . . ." #aktif olduğunda gruba gelen mesaj
support = "Medikalsohbettr" #destek qrupunuzun kullanıcı adı
sahib = "parliamenttr" #sahibinizin kullanıcı adı
noadmin = "➻ Üzgünüm Ama Yönetici Değilsiniz ." #yönetici olmayanlar için mesaj

#
# 
# 
# 


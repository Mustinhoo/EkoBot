import discord
from discord.ext import commands
import asyncio
import random

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'Bot olarak oturum açıldı: {bot.user}')

@bot.command()
async def CHN(ctx):
    ipuclari = [
        "Ev temizliğinde doğal ürünler kullanmayı deneyin.",
        "Gıda atıklarını kompost yaparak değerlendirin.",
        "Plastik kullanımını azaltmak için bez çanta kullanın.",
        "Kullanmadığınız elektronik cihazları kapatarak enerji tasarrufu sağlayın.",
        "Duş sırasında suyu kapatarak su israfını önleyin.",
        "Yerel parkları temizleme etkinliklerine katılın.",
        "Tek kullanımlık ürünleri azaltarak çevreyi koruyun.",
        "Bisiklete binmek veya toplu taşıma kullanmak hava kirliliğini azaltır.",
        "Evde bitki yetiştirerek havayı temizleyebilirsiniz.",
        "Çevrenizdekileri çevre konusunda bilinçlendirin.",
        "Plastik pipet yerine metal veya bambu pipetler kullanın.",
        "Geri dönüştürülemeyen ambalajları mümkün olduğunca azaltın.",
        "Yemek artıklarını yaratıcı tariflerde değerlendirin.",
        "Kendi bez torbanızı veya kumaş poşetlerinizi yaparak alışveriş yapın.",
        "Elektronik cihazları tasarruf moduna alın.",
        "Kullanılmayan ışıkları kapatmayı alışkanlık haline getirin.",
        "Gereksiz kağıt kullanımından kaçının.",
        "Musluklara su tasarrufu sağlayan aparatlar takın.",
        "Yeniden doldurulabilir su şişesi kullanın.",
        "Sürdürülebilir üretim yapan markalardan alışveriş yapın.",
        "İhtiyacınız olmayan kıyafetleri bağışlayın veya geri dönüştürün.",
        "Kullanmadığınız alanlarda elektrikli ısıtıcıları kapatın.",
        "Kaliteli ve uzun ömürlü ürünler tercih edin.",
        "İkinci el alışveriş yaparak yeni ürün alımını azaltın.",
        "Güneş enerjisi gibi yenilenebilir enerji kaynaklarına geçiş yapmayı düşünün.",
        "Biyoçözünür veya geri dönüştürülebilir ambalajlar tercih edin.",
        "Araçlarınızın bakımlarını düzenli yaparak yakıt tasarrufu sağlayın.",
        "Toplu taşıma veya bisiklet kullanarak karbon ayak izinizi azaltın.",
        "Bahçeniz varsa, yağmur suyu biriktirerek bitkileri sulayın.",
        "Fazla yemek siparişi yerine evde yemek yapmayı tercih edin.",
        "Meyve ve sebzelerinizi yerel pazarlardan temin edin.",
        "Organik veya yerel ürünler tercih edin.",
        "Yeniden kullanılabilir kahve fincanları ve kaplar kullanın.",
        "Elektrikli araç kullanımını göz önünde bulundurun.",
        "Kısa mesafelerde araç yerine yürümeyi tercih edin.",
        "Eski kıyafetlerinizi yenileyerek yeniden kullanın.",
        "Gıda alışverişinde fazla plastik kullanımından kaçının.",
        "Kendi doğal temizlik ürünlerinizi yapın.",
        "Çok fazla ambalaj içeren ürünleri satın almayın.",
        "Minimalist yaşam tarzını benimseyerek gereksiz eşyalarınızdan kurtulun.",
        "Soğuk su ile çamaşır yıkayarak enerji tasarrufu yapın.",
        "Geri dönüştürülebilir ofis malzemeleri kullanın.",
        "Balkon veya bahçede kompost yaparak bitkilerinize doğal gübre sağlayın.",
        "Cep telefonlarını ve bilgisayarları gereksiz yere şarjda bırakmayın.",
        "Kullanmadığınız kağıtları geri dönüştürün.",
        "Daha az kimyasal içeren bakım ürünleri tercih edin.",
        "Bitki tabanlı sabun ve şampuanlar kullanın.",
        "Kampanya veya ücretsiz numune almak için gereksiz ürünleri almaktan kaçının.",
        "Alışveriş yaparken çevre dostu ürünleri tercih edin.",
        "Elektronik ürünleri yeniden kullanmayı veya geri dönüştürmeyi düşünün."
    ]
    await ctx.send(random.choice(ipuclari))

@bot.command()
async def çevresel_çaba(ctx):
    await ctx.send("Çevresel çabanızın kanıtını (fotoğraf, kısa açıklama) buraya yazın.")

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    try:
        msg = await bot.wait_for('message', check=check, timeout=60)

        roles = [
            "Yeşil Başlangıç",
            "Doğa Gönüllüsü",
            "Çevre Koruyucu",
            "Sürdürülebilir Yaşam Elçisi",
            "Ekolojik Savunucu",
            "Doğa Savaşçısı",
            "Dünya Koruyucusu",
            "Eko Bilinçli",
            "Gezegen Savunucusu",
            "Çevre Şampiyonu"  
        ]

        assigned_role = None
        for role_name in roles:
            role = discord.utils.get(ctx.guild.roles, name=role_name)
            if role and role not in ctx.author.roles:
                assigned_role = role
                break

        if assigned_role:
            await ctx.author.add_roles(assigned_role)
            await ctx.send(f"Tebrikler! Çevre dostu olduğunuz için '{assigned_role.name}' rolü verildi.")
            
            if assigned_role.name == "Çevre Şampiyonu":
                await ctx.send("10. seviyeye ulaştınız! IBAN bilgilerinizi buraya yazabilirsiniz, cüzi bir ödül gönderilecektir.")

                def iban_check(m):
                    return m.author == ctx.author and m.channel == ctx.channel and len(m.content) >= 15  

                try:
                    iban_msg = await bot.wait_for('message', check=iban_check, timeout=60)
                    iban = iban_msg.content
                    await ctx.send(f"Teşekkürler! IBAN {iban} kaydedildi ve ödül gönderilecektir.")
                    
                except asyncio.TimeoutError:
                    await ctx.send("Belirtilen süre içinde IBAN bilgisi gönderilmedi.")
        else:
            await ctx.send("Tüm roller zaten atanmış durumda veya rol bulunamadı.")
    except asyncio.TimeoutError:
        await ctx.send("Belirtilen süre içinde kanıt gönderilmedi.")

bot.run('TOKEN')

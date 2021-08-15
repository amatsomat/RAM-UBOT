from platform import uname
from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================

@register(outgoing=True, pattern='^P(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("samlekom mamank...")


@register(outgoing=True, pattern='^.atg(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**GUA JAMET NIH AJARIN KEREN KYK LU DONG**")


@register(outgoing=True, pattern='^L(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("mamat ni bos...")


@register(outgoing=True, pattern='^.muka(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**muka kaya babi nyari spek cewe kaya bidadari lawak lu goblok**")


@register(outgoing=True, pattern='^.kuat(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**gak boleh lemah
semangat dong, dulu
katanya mau jadi ultraman**")


@register(outgoing=True, pattern='^sad1(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**lihatlah cantik, kau telah mematahkan hati lelaki incaran semua orang**")


@register(outgoing=True, pattern='^sad2(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**dia memang tidak selingkuh, tapi dia selalu menyepelekan hal kecil yang membuat saya kecewa**")


@register(outgoing=True, pattern='^bdt(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**ngaku nya badut, tapi semua cewe lu embat alahsiaboy**")


@register(outgoing=True, pattern='^sad3(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Dan akhirnya berhenti berekspektasi,membiarkan semuanya mengalir,tp tdk ingin mengakhiri,menahan sakit sendiri,kadang ingin pergi,tapi**")


@register(outgoing=True, pattern='^C(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**MUKA LU HINA, GAUSAH SOK KERAS YA ANJENGG!!**")


@register(outgoing=True, pattern='^S(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**GAUSAH SOKAP DEH ANJING!!**")


@register(outgoing=True, pattern='^V(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**ngakunya badut tapi semua cowo lu embat**")

@register(outgoing=True, pattern='^O(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**JANGAN MAEN BOT MULU, ALAY LU NGENTOTT,KESANNYA NORAK, CUIHHHH!!!**")


@register(outgoing=True, pattern='^G(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Gak keren lu begitu tolol, kuburan bapak lu gw gali buat dijadiin kolam renang anak paud.Cuihhhhh!!!**")

CMD_HELP.update({
    "salam":
    "P\
\nUsage: Untuk Memberi salam.\
\n\nL\
\nUsage: Untuk Menjawab Salam.\
\n\nK\
\nUsage: Untuk mengontoli mereka.\
\n\nN\
\nUsage: Kalo kesel coba aja.\
\n\nB\
\nUsage: Buat Ngatain Yang Suka Bacot.\
\n\nM\
\nUsage: Tersedak meledek.\
\n\nY\
\nUsage: Buat yang males adu bacot.\
\n\nC\
\nUsage: Buat menghujat.\
\n\nS\
\nUsage: Haha sokap."
})

CMD_HELP.update({
    "salam2":
    "V\
\nUsage: Hujat Orang caper.\
\n\nJ\
\nUsage: Hujat Jamet.\
\n\nA\
\nUsage: Hujat yang gapunya muka.\
\n\nX\
\nUsage: Ngatain Grup wkwk.\
\n\nZ\
\nUsage: teruntuk petarung.\
\n\nH\
\nUsage: Coba dewek ah.\
\n\n.atg\
\nUsage: Istighfar 1.\
\n\n.ast\
\nUsage: Istighfar 2.\
\n\nO\
\nUsage: Ngatain org norak.\
\n\nG\
\nUsage: Liat Sendiri."
})

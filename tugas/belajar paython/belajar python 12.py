# set -> () -> tidak berurutan, berubah, tidak duplikat
daftar_game = {"ml, ff", "efootball"}
game = {"elden ring", "gensin"}
print("game:",daftar_game)
print("game:",game)
# .add()->menambah kan item
daftar_game.add("valorant")
print("game:",daftar_game) # jika sudah ada dalam set maka tidak bisa muncul
# .remove()-> menghapus item
game.remove("gensin")
print("game",game)
# len()->menghitung item
print("game ada:",len(game),game)
# .union()->menggabung 2 set berdua
game_berdua = game.union(daftar_game)
print("dftar semua game nya :",len(game_berdua),game_berdua)
# intersection()->mencari item yang kembar
game_yang_sama = game .intersection(daftar_game)
print("game yang sama:",game_yang_sama)
# difference()->menvari item yang berbeda
gameYangbeda = game.difference(daftar_game)
print("game yang beda:",gameYangbeda)
# dict (dictionary) -> (key:velue) / {kunci:isinya}
animedzaky = {
    "wind_breker": "sakura",
    "red_zero": "subar",
    "waifu":{
        "red_zero":"rem"
    }
}
print(animedzaky)
print("wifu red_zero:",animedzaky["waifu"]["red_zero"])
# berurutan berdasarkan key, berubah
# key tidak boleh duplikat
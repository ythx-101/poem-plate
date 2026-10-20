# 中国古典人物画法 · AI 诗画参考（动漫角色 × 古典画法）

> 用途：AI 出人物画（任意生图模型，如 Grok Imagine、GPT Image、Gemini）+ 代码排字（竖排诗句、落款）。
> 已做过的基线：仕女图式汉服 + Art Deco 墨线 + 墨黑 / 米白 / 单金色板 + 七言判词。
> 整理日期：2026-10-21。链接全部在当天实际打开确认（HTTP 200，页面标题和内容对得上）。博物馆官网（大都会、大英、波士顿、台北故宫数位典藏、史密森尼）当天对自动访问返回 403/429，打不开就没列。所以高清图主要走维基共享资源（Commons），图源多数就是这些馆的开放图。

---

## 0. 通用规则（每段提示词都要带上）

- **防字防印**：模型一看到 "Chinese painting" 就爱自己加题跋和红印。每段都要写：
  `no text, no calligraphy, no inscription, no seal, no red stamp, no signature, no watermark, no border, no frame`
  如果模型不认负面词（Grok 基本靠正面描述），就换成正面写法：`clean uninscribed silk, blank empty background`。
- **给排字留白**：人物放一角或一侧，留 50–60% 空白，例如 `figure placed in the lower-right third, vast empty negative space on the left and top`。
- **认得出角色**：别只写角色名，把认人的特征写进去：发色、瞳色、标志道具、标志发饰。服装改成古装时，保留一两处原作配色或道具，例如蝴蝶忍的蝴蝶羽织纹、三笠的红围巾。
- **跟现有色板对齐**：每种画法都可以加一句 `restrained palette of ink black, warm rice-paper cream and a single accent of muted gold`，用来把它收进我们这套视觉系统。要做原汁原味版就去掉这句（敦煌、年画、唐仕女原本色彩很重）。
- **比例**：竖幅挂轴用 2:3 或 1:2，手卷局部用 3:2 或 16:9。

---

## 1. 十八描里最有用的几种线法（附生图英文关键词）

| 描法 | 特征 | 代表 | 英文关键词 |
|---|---|---|---|
| 高古游丝描 | 极细、匀、连绵不断，像蚕吐丝，几乎没有粗细变化 | 顾恺之 | `gossamer-thin continuous ink line, uniform hairline weight, "spring silkworm spitting silk" line, delicate unbroken contour` |
| 铁线描 | 比游丝略粗，匀而硬，转折有力，像铁丝 | 唐宋工笔、李公麟、张萱 | `iron-wire line, firm even-weight ink outline, taut unmodulated contour, precise gongbi line` |
| 琴弦描 | 直挺、紧绷、长线，像琴弦 | 宋元工笔 | `taut straight lute-string lines, long tensioned strokes` |
| 行云流水描 | 长线顺势回转，飘逸流动 | 衣袂、飘带 | `flowing cloud-and-water drapery lines, long sweeping rhythmic curves` |
| 兰叶描 | 起收细、中段鼓、有提按，像兰叶 | 吴道子 | `orchid-leaf strokes, swelling and tapering brush line, thick-thin modulated drapery, wind-blown sashes (Wu Daozi style)` |
| 钉头鼠尾描 | 落笔重顿像钉头，收笔尖细像鼠尾，速度感强 | 任伯年、明清写意人物 | `nail-head rat-tail strokes, heavy blunt entry tapering to a fine tail, swift calligraphic brushwork` |
| 折芦描 | 长线中途急转，方折尖锐，像折断的芦苇 | 梁楷；陈洪绶的方折衣纹可借这个词 | `broken-reed line, angular sharp turns, faceted angular drapery folds` |
| 减笔描 | 极少几笔概括 | 梁楷《泼墨仙人》式 | `abbreviated minimal brushstrokes, few decisive lines, spontaneous ink` |

> 最实用的四个：仙气用 **高古游丝**，工整仕女和白描用 **铁线**，飘带动势用 **兰叶 / 行云流水**，战斗角色和版画感用 **折芦 / 钉头鼠尾**。

---

## 2. 画法 / 流派（11 种）

### ① 高古游丝描 · 顾恺之（东晋）
- **代表作**：《洛神赋图》（宋摹本，北京故宫；辽宁省博物馆另有一本），《女史箴图》（唐摹本，大英博物馆）。
- **视觉特征**：游丝线细匀连绵。设色很淡，只在衣带上点朱、石青。人比山水大，山水像布景。人物身形修长，面容静穆，衣带和飘带向上飞扬（"春蚕吐丝"）。
- **适合角色**：仙气、长寿、非人或神女型角色：芙莉莲（《葬送的芙莉莲》）、各类精灵、女神、白发少女。
- **提示词骨架**：
```
A celestial woman in the style of Gu Kaizhi's "Nymph of the Luo River" handscroll, Eastern Jin dynasty painting on aged silk.
{CHARACTER} reimagined as a river goddess: {hair color / eye color / signature accessory}, flowing layered robes with long ribbons floating upward.
Gossamer-thin continuous ink lines of uniform weight ("silk-thread line"), very pale mineral washes, faint vermilion and azurite accents,
serene distant expression, slender elongated proportions, archaic stylized waves and small schematic trees.
Figure placed in the lower-right third, vast empty silk background.
Clean uninscribed silk; no text, no calligraphy, no seal, no signature, no border.
```
- **高清图**：
  - Commons｜洛神赋图分类：https://commons.wikimedia.org/wiki/Category:Nymph_of_the_Luo_River
  - Commons｜女史箴图分类：https://commons.wikimedia.org/wiki/Category:Admonitions_Scroll
  - 中文维基《洛神赋图》（含故宫宋摹本、辽宁本大图）：https://zh.wikipedia.org/wiki/洛神赋图

### ② 吴带当风 · 吴道子白描道释（唐）
- **代表作**：《八十七神仙卷》（传吴道子，徐悲鸿纪念馆）。
- **视觉特征**：纯墨白描，兰叶描粗细起伏，衣带被风兜起（"吴带当风"）。常画成群仙行列，人物前后叠压，有节奏。基本不上色。
- **适合角色**：群像、仙人队列、法师；适合一组角色同框（一整个战队或乐队）。
- **提示词骨架**：
```
A procession of celestial immortals in Tang dynasty baimiao ink line drawing, in the manner of Wu Daozi's "Eighty-seven Celestials" scroll.
{CHARACTERS} as Daoist immortal maidens, each recognizable by {hair / accessory}, holding banners, lotus and instruments,
robes and sashes billowing as if caught in wind ("Wu's sashes in the wind"), orchid-leaf brush strokes swelling and tapering,
pure black ink on pale silk, no color, rhythmic overlapping figures moving left to right, empty space above.
No text, no calligraphy, no seal, no signature.
```
- **高清图**：
  - Commons｜八十七神仙卷：https://commons.wikimedia.org/wiki/Category:Scroll_of_Eighty-Seven_Immortals
  - 中文维基《八十七神仙卷》：https://zh.wikipedia.org/wiki/八十七神仙卷
  - Commons｜吴道子（含大都会藏传吴道子观音）：https://commons.wikimedia.org/wiki/Category:Wu_Daozi

### ③ 唐代绮罗仕女 · 张萱 / 周昉
- **代表作**：张萱《捣练图》（宋徽宗摹本，波士顿美术馆），周昉《簪花仕女图》（辽宁省博物馆）。
- **视觉特征**：人物丰腴，"圆脸、蛾眉、长项、削肩"，高髻簪花，低胸长裙，披帛。铁线勾勒，平涂重彩：朱红、石绿、赭黄，纱衣透明叠色。背景大多留空，只点一两只小狗、仙鹤或几朵花。
- **适合角色**：宫廷、贵族、雍容型角色：《药屋少女的呢喃》里的玉叶妃、猫猫，大小姐、女王型角色。
- **提示词骨架**：
```
Tang dynasty court lady painting in the style of Zhou Fang's "Court Ladies Adorning Their Hair with Flowers", ink and color on silk.
{CHARACTER} as a plump elegant Tang court lady: round face, moth-feather eyebrows, high chignon with a large peony hairpin,
low-cut long skirt with a translucent gauze outer robe and a long silk shawl, {signature colors kept in the robe pattern}.
Iron-wire fine outlines, flat opaque mineral colors (vermilion, malachite green, ochre), transparent layered gauze,
calm languid pose, a small dog or crane as the only prop, plain empty silk background, figure on the right side.
No text, no seal, no calligraphy, no signature.
```
- **高清图**：
  - 中文维基《簪花仕女图》：https://zh.wikipedia.org/wiki/簪花仕女图
  - 英文维基《捣练图》：https://en.wikipedia.org/wiki/Court_Ladies_Preparing_Newly_Woven_Silk
  - Commons｜张萱（含捣练图、虢国夫人游春图）：https://commons.wikimedia.org/wiki/Category:Zhang_Xuan_(Tang_dynasty)

### ④ 敦煌飞天壁画（北魏 → 盛唐）
- **代表作**：莫高窟第 320 窟盛唐飞天、第 112 窟"反弹琵琶"伎乐，榆林窟第 15 窟吹笛飞天。
- **视觉特征**：横向飞翔或俯冲的身体，长飘带盘旋拉出动势。土红起稿，石青、石绿、赭红叠色，晕染立体。颜料氧化后肤色发黑，墙面有斑驳肌理。手里拿乐器或花，周围散花和云。
- **适合角色**：会飞的、跳舞的、与音乐有关的角色：初音未来（反弹琵琶正好对应她的乐器属性），《孤独摇滚》乐队成员，偶像。
- **提示词骨架**：
```
Dunhuang Mogao cave mural of a flying apsara (feitian), High Tang style.
{CHARACTER} as a celestial musician flying horizontally, {hair color} hair in a topknot, bare arms with jewelry,
long swirling silk ribbons trailing in looping arcs, playing a pipa held behind her back,
scattered falling flowers and stylized clouds, red-ochre underdrawing lines, azurite blue, malachite green and earth red,
soft shading, weathered plaster texture with flaking pigment and age cracks,
figure in the upper-left, wide empty ochre wall space.
No text, no inscription, no seal.
```
（要收进单金色板时，把颜色那段换成 `rendered as a monochrome mural in ink black and cream with gold-leaf ribbons`。）
- **高清图**：
  - 数字敦煌（敦煌研究院官方；洞窟高清全景和开放素材库）：https://www.e-dunhuang.com/
  - 中文维基《飛天 (佛教)》（含榆林窟 15 窟吹笛飞天图）：https://zh.wikipedia.org/wiki/飛天_(佛教)

### ⑤ 李公麟白描（北宋）
- **代表作**：《五马图》（东京国立博物馆）。李公麟把白描从"画稿"提升成独立画种。
- **视觉特征**：纯墨线，不设色，只在必要处略加淡墨。铁线和行云流水结合，线条干净、理性、克制。人和马结构准确，比例写实，构图疏朗。
- **适合角色**：冷静克制的角色，有坐骑的角色：三笠（《进击的巨人》，骑马加调查兵团）、阿尔托莉雅（Fate）、骑士型角色。跟现有"墨线"路线最接近，出图稳定。
- **提示词骨架**：
```
Northern Song baimiao (plain ink line) drawing in the manner of Li Gonglin's "Five Horses" scroll.
{CHARACTER} as a Song dynasty rider standing beside a horse, {short hair / scarf / blade}, plain robe with precise folds.
Pure fine ink outlines only, iron-wire and flowing-water lines, no color except faint light ink wash,
accurate restrained anatomy, calm dignified posture, generous empty paper, figure at the lower left.
No text, no seal, no inscription, no signature.
```
- **高清图**：
  - Commons｜五马图：https://commons.wikimedia.org/wiki/Category:Five_Horses_Scroll
  - Commons｜李公麟：https://commons.wikimedia.org/wiki/Category:Li_Kung-lin

### ⑥ 明代吴门工笔重彩仕女 · 唐寅 / 仇英
- **代表作**：唐寅《王蜀宫妓图》（北京故宫，又名《四美图》），仇英《汉宫春晓图》（台北故宫）。
- **视觉特征**：工笔重彩。额、鼻、下巴敷白（"三白法"），头戴金冠，衣裙满是云霞纹样。人物比唐代瘦，体态端丽。仇英多画宫苑楼阁，工整的界画里放很多人物，群像很热闹。
- **适合角色**：多人群像：五等分的花嫁五姐妹（对应《四美图》的格式），《【推しの子】》B小町，后宫或宫廷题材。
- **提示词骨架**：
```
Ming dynasty gongbi heavy-color painting of palace ladies, in the manner of Tang Yin's "Court Ladies of the Former Shu".
{N} women based on {CHARACTERS}, each identified by {hair color / hair ornament}, wearing gold lotus crowns and Daoist robes with cloud-patterned brocade,
"three whites" makeup (white on forehead, nose and chin), slender graceful proportions,
fine iron-wire outlines, rich mineral colors with gold details, arranged in a loose group on the right,
plain silk background with a large empty area. No text, no seal, no calligraphy, no signature.
```
- **高清图**：
  - 中文维基《王蜀宫妓图》：https://zh.wikipedia.org/wiki/王蜀宫妓图
  - Commons｜汉宫春晓图（台北故宫）：https://commons.wikimedia.org/wiki/Category:Spring_Morning_in_the_Han_Palace
  - Commons｜仇英（另有《人物故事图册》等）：https://commons.wikimedia.org/wiki/Category:Qiu_Ying

### ⑦ 陈洪绶变形人物 · 《水浒叶子》（明末）
- **代表作**：《水浒叶子》《博古叶子》（酒牌木刻），《陶渊明故事图》《宣文君授经图》。
- **视觉特征**：故意的"古拙变形"：头大身短，脸长，五官怪异，带点冷笑。衣纹方折、成块，像刻出来的。线条硬，"高古奇骇"。版画是单人立像加一件标志道具，背景全空。
- **适合角色**：战斗少女，气场怪、有危险感的角色：蝴蝶忍、甘露寺蜜璃（《鬼灭之刃》），玛奇玛（《电锯人》），钉崎野蔷薇（《咒术回战》）。
- **提示词骨架**：
```
Late Ming figure painting in the eccentric archaic style of Chen Hongshou, like his "Water Margin" playing-card woodcuts.
{CHARACTER} as a wandering swordswoman: deliberately stylized distorted proportions (large head, elongated face, compact body),
uncanny calm smile, holding {signature weapon}, robe with angular faceted folds in broken-reed lines,
crisp black woodblock-like contours, minimal flat color (ink black with one muted accent),
single standing figure, totally empty background, figure off-center to the right.
No text, no seal, no character labels, no inscription.
```
- **高清图**：
  - Commons｜陈洪绶叶子（酒牌，含水浒人物）：https://commons.wikimedia.org/wiki/Category:Playing_cards_by_Chen_Hongshou
  - Commons｜陈洪绶绘画：https://commons.wikimedia.org/wiki/Category:Paintings_by_Chen_Hongshou
  - 英文维基 Chen Hongshou（含大都会藏《准提佛母法像图》等）：https://en.wikipedia.org/wiki/Chen_Hongshou

### ⑧ 明清绣像 / 人物版画（《无双谱》等）
- **代表作**：清初金古良绘、朱圭刻《无双谱》（四十位历史人物像）；明清小说卷首"绣像"（一人一像）。
- **视觉特征**：黑白木刻线，线条刚硬、粗细均匀。单人全身立像，旁边配兵器或器物。背景是空的，或者只有一块石、一棵树。很适合做成"一人一张"的系列卡。
- **适合角色**：系列化的角色卡：鬼灭"柱"、咒术回战、海贼王女角；适合配"一人一首"的判词。
- **提示词骨架**：
```
Qing dynasty woodblock-printed book portrait (xiuxiang) in the style of "Wushuang Pu" (Table of Peerless Heroes).
{CHARACTER} as a full-length standing figure in Ming-Qing costume, {signature weapon or object} beside her,
bold even black woodcut lines, carved-wood texture, no shading, black ink on cream paper,
a single rock or bare tree as the only setting, figure in the lower half, large blank top area.
No text, no title, no caption, no seal, no border.
```
- **高清图**：
  - Commons｜无双谱：https://commons.wikimedia.org/wiki/Category:Wu_Shuang_Pu
  - Commons｜中国木刻总类（含《十竹斋书画谱》等）：https://commons.wikimedia.org/wiki/Category:Woodcuts_from_China

### ⑨ 清代纤弱仕女 · 改琦 / 费丹旭
- **代表作**：费丹旭《十二金钗图册》（北京故宫），改琦《红楼梦图咏》（木刻本）。
- **视觉特征**：削肩、柳腰、瓜子脸、细眉小口，神情哀愁。淡彩，线细而柔。常配芭蕉、湖石、竹、窗棂，背景大片留白，整体是"病美人"感。
- **适合角色**：哀愁、清冷、文学气的角色：绫波丽（EVA），雪之下雪乃（《春物》），后藤一里（《孤独摇滚》，反差萌）。**跟已做的"七言判词"同源**：判词本来就出自《红楼梦》金陵十二钗，可以直接做一组"动漫十二钗"。
- **提示词骨架**：
```
Qing dynasty beauty painting in the style of Fei Danxu's "Twelve Beauties of Jinling" album, light color on paper.
{CHARACTER} as a fragile melancholic young lady: sloping narrow shoulders, willow-thin waist, oval face, delicate brows,
pensive downcast gaze, {hair color} hair in a simple bun with one hairpin, pale layered robes,
soft fine ink lines, very light washes of grey-blue and pale pink, a banana leaf and a garden rock as the only props,
figure small in the lower corner, wide empty paper. No text, no poem, no seal, no signature.
```
- **高清图**：
  - Commons｜费丹旭《十二金钗图册》（故宫藏，逐开大图）：https://commons.wikimedia.org/wiki/Category:Album_of_the_Twelve_Beauties_of_Jinling_by_Fei_Danxu
  - Commons｜改琦：https://commons.wikimedia.org/wiki/Category:Gai_Qi
  - Commons｜金陵十二钗（各角色历代图像汇总）：https://commons.wikimedia.org/wiki/Category:Twelve_Beauties_of_Jinling

### ⑩ 海派人物 · 任伯年（晚清）
- **代表作**：《群仙祝寿图》，"风尘三侠"、钟馗、关公等人物画。
- **视觉特征**：兼工带写，钉头鼠尾描，用笔快而有力。色彩鲜亮，大块用花青、胭脂。构图像抓拍，动态感强。
- **适合角色**：侠女、杀手、动作感强的角色：约尔·福杰（《间谍过家家》，可以对应红拂女或聂隐娘），两仪式（《空之境界》）。
- **提示词骨架**：
```
Late Qing Shanghai School figure painting in the manner of Ren Bonian, ink and bright color on paper.
{CHARACTER} as a wandering heroine (xianü) mid-motion, {signature weapon}, cloak swirling,
swift nail-head rat-tail brushstrokes, mix of precise face and loose expressive drapery,
vivid indigo and rouge washes, dynamic diagonal composition, snapshot-like gesture,
figure on the right, empty paper on the left. No text, no inscription, no seal, no signature.
```
- **高清图**：
  - Commons｜任伯年：https://commons.wikimedia.org/wiki/Category:Ren_Bonian
  - 英文维基 Ren Bonian：https://en.wikipedia.org/wiki/Ren_Bonian

### ⑪ 木版年画 · 杨柳青 / 桃花坞
- **代表作**：天津杨柳青年画（如《连生贵子》），苏州桃花坞，以及门神、美人、娃娃题材。
- **视觉特征**：粗黑木刻轮廓，大红、桃红、翠绿、明黄套色，对称构图，胖脸，喜庆吉祥纹（莲、鱼、牡丹）。杨柳青是先印线版再手绘填色，脸部晕染细腻。
- **适合角色**：Q版、可爱、节庆题材：阿尼亚（《间谍过家家》）；双人角色做成一对门神，比如蕾姆和拉姆（《Re:0》）。很适合春节限定。
- **提示词骨架**：
```
Chinese New Year woodblock print (nianhua), Yangliuqing style, hand-colored.
{CHARACTER} as a chubby auspicious figure holding a lotus and a carp, {hair color} hair in twin buns,
bold black woodblock outlines, flat saturated vermilion, peach pink, emerald green and yellow,
symmetrical festive composition, peony and cloud motifs, slightly uneven registration and paper texture.
No text, no characters, no couplets, no seal.
```
（年画本来常带吉祥字。"no couplets / no characters" 一定要写。）
- **高清图**：
  - Commons｜年画总类：https://commons.wikimedia.org/wiki/Category:Nianhua
  - 英文维基 New Year picture（含杨柳青康熙年画）：https://en.wikipedia.org/wiki/Nianhua
  - 英文维基 Yangliuqing New Year pictures：https://en.wikipedia.org/wiki/Yangliuqing_New_Year_pictures

---

## 3. 建议：先做哪 3 种

| 顺序 | 画法 | 配哪些角色 | 理由（一句） |
|---|---|---|---|
| 1 | **⑨ 费丹旭 / 改琦纤弱仕女** | 绫波丽、雪之下雪乃、芙莉莲，往后扩成"动漫金陵十二钗"系列 | 七言判词本来就出自十二钗，现有的米白、单金、留白排版几乎不用改，一个系列能连发十二张。 |
| 2 | **⑦ 陈洪绶 / 水浒叶子** | 蝴蝶忍、甘露寺蜜璃、玛奇玛、钉崎野蔷薇 | 跟仕女路线反差最大：战斗少女配古拙变形加方折线，第一眼就有"怪而高级"的辨识度，叶子"一人一牌"的格式也正好配一首诗。 |
| 3 | **④ 敦煌飞天** | 初音未来（反弹琵琶）、《孤独摇滚》乐队成员 | 飘带动势最上镜，音乐角色和伎乐飞天一一对应。单金色板可以直接做成"金箔飘带"，传播性最强。 |

备选：做骑马或剑士题材时，⑤ 李公麟白描最稳（纯墨线，跟现有墨线风格无缝衔接）；春节档用 ⑪ 年画。

---

## 4. 已知限制
- 博物馆官方页面（大都会、大英、波士顿美术馆、台北故宫数位典藏、史密森尼弗利尔馆）当天对自动访问返回 403/429，没能确认，所以没列。浏览器手动访问通常可以打开。
- 北京故宫"数字文物库"没找到能稳定访问的具体条目链接，没列。
- 《水浒叶子》在 Commons 没有单独分类，挂在"陈洪绶叶子"分类里，里面混有《博古叶子》。
- 提示词骨架还没实测，模型对"no text"的服从度要小样试跑后再调。

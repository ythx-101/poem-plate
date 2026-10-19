---
name: poem-plate
description: 诗画合成：用 AI 生图模型画人物，再用代码把画缩到一侧、留出大片纸色空白、竖排古诗原文与出处、加落款，做成可直接发小红书/X 的 3:4 诗意插画。用户说「画某个古典人物配诗」「诗画」「红楼梦人物插画」「按 poem-plate 画」时使用。
---

# poem-plate：AI 画人物 + 代码排诗

分工一句话：**生图模型管画功，代码管留白、配色、排诗。**

好看的关键是构图：人物缩小推到一侧，另一侧留出大片纸色空白放竖排诗，边缘羽化让画从纸里浮出来。实测这种合成版明显胜过生图模型原图满版，也胜过纯代码画线稿（代码画人体和手很难过关）。

## 0 复述
一句话说清：画谁、什么意境、配哪几句原文（出处）、几张、是否成系列。成系列时所有张共用同一纸色、同一字体、同一版式骨架（诗在左、人在右，或统一镜像）。

## 1 文字先核实（P0 源头）
- 诗句、判词、回目、出处逐字核对原文（维基文库、古诗文网等可靠全文页），写进 `text.md`，附来源 URL。繁体原文转简体时逐字再看一遍。
- 生图模型写中文会乱码：**画里一律不要字**，所有文字由代码排。

## 2 生图
- 任何能出 3:4 插画的模型都行（作者用 Grok Imagine；额度不够时也用过别的生图工具）。每个人物出 3–4 张候选再挑。
- 有满意的旧作时，把它当风格参考图一起喂给模型，系列气质更稳。
- 英文提示词骨架（替换人物/场景/道具）：

  `1920s American Art Deco fashion magazine illustration, ink line art on cream paper, <人物+动作+情绪>, <服饰发式首饰>, <2-4 件道具>; bold confident long lines, solid black masses vs large empty space, S-curve pose, elegant and fully clothed, not sexy; strictly limited palette: cream #f5f4ed background, near-black #141413 ink, single gold accent; no other colors, no text, no letters, no signature, no watermark. Leave a large clean empty area on the <left> for vertical calligraphy.`

- 人物神态贴性格：每个人物写一句「性格 → 姿态/眼神/道具」的翻译放进提示词。
- 古典人物写明朝代服饰（如 Qing dynasty aoqun / bijia / cloud collar），否则模型常画成民国旗袍。
- 气质靠大块实心墨色、密集金色纹样、能框住人物的场景物件（帘、镜、亭柱、花树）。人物身份朴素时，用神态和场景抬气质，而不是堆首饰。
- 手是最大风险：提示里让手少露、只露指尖或藏袖；选图时逐张放大看手指数、镜像和道具结构。
- 局部有问题（手、某个道具）：只把那一块裁出来重画再贴回，不要整张重抽。

## 3 合成（compose_lib.py）
```bash
pip install numpy pillow
export POEM_FONT=/path/to/NotoSerifSC-Light.otf   # 任意中文衬线体
export POEM_SIGNATURE=你的名字 POEM_HANDLE=@你的账号
python example_compose.py plate.jpg out.png
```
它做的事：
1. 去掉原图细边框（没有就保留整图）；
2. 把偏黄底色压成精确 `#f5f4ed`；
3. 边缘羽化（FEATHER 28），画边 70px 内的浅灰提亮成纸色，避免像贴图；道具被原图切边时，那一边可直接出血到画布边（`bleed`）；
4. 把画缩放推到右侧，左边留 600px 给文字；
5. 亮度映射纸 ↔ 墨，金色系映射到 `#B8893A`–`#D4AF6A`；
6. 逐字竖排（《》自动旋转），文字压到画或出左边界会直接报错；左上金色系列小字，左下竖排署名 + 旋转账号。

画布 1500×2000（3:4，小红书）；发 X 可另补边出 4:5。

## 4 评审
- 用一个强模型（如 Claude Opus）当严格评审，六项打分：线条 / 动势 / 留白 / 古典 / 结构 / 神韵（或换成题材相关项）。
- P0：手畸形、读不懂的部件、错字漏字、暴露或性感化、服饰朝代错、乱码。
- 评审提示词要把原文逐字给它对；**改了版式就同步改评审提示词**，否则会误判 P0。
- 至少 2 轮，P0 不清零不交付。系列作品让评审拿最满意的一张当对照，判断气质够不够。
- 交付前自己逐张打开整图看。

## 5 交付
每张：成品 PNG、生图原图、分数、最大缺点；系列再拼一张总览。不替用户发帖。

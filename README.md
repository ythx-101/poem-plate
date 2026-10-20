# poem-plate

**AI 画人物，代码排诗：把古诗和古典人物做成一张留白讲究、可以直接发的诗意插画。**

一个给 Claude Code 等 AI agent 用的技能（skill）。生图模型负责人物的画功；代码负责把画缩到一侧、压成统一的纸色 / 墨色 / 单一金色、边缘羽化，再在大片留白里竖排原文、出处和落款。

![预览：新妇晨妆](examples/xinfu-preview.jpg)

<sub>温庭筠《菩萨蛮》+ 朱庆馀《近试上张籍水部》。上图为最终成品，生图原图满版见 [examples/xinfu-raw.jpg](examples/xinfu-raw.jpg)。</sub>

## 为什么要合成

- 生图模型原图是满版的，人物太满，没有地方放诗，中文字也会写成乱码。
- 纯代码画线稿，人体和手很难画对。
- 合成版两头取长：画交给模型，留白、配色、文字交给代码，文字永远准确，系列风格永远统一。

## 它做什么

- **文字先核实**：诗句、出处逐字对照可靠全文，画里不放任何字。
- **出图提示词骨架**：1920s Art Deco 墨线插画、单一金色、留出左侧空白；按人物性格写神态；写明朝代服饰。
- **代码合成**（`compose_lib.py`）：去边框、纸色压平、边缘羽化与提亮、缩放推到右侧、纸墨金色映射、竖排中文（《》自动旋转），文字压到画上会直接报错。
- **严格评审**：六项打分，手畸形、错字、服饰朝代错、性感化都算 P0，不清零不交付。


## v2：动漫角色 × 古典画法

![预览：《无职转生》三妻](examples/preview.jpg)

现在可以把动漫角色画成古典诗画，由三个旋钮自由组合：

| 旋钮 | 选项 |
|---|---|
| **字** | 红楼式判词：工整、押韵、对仗的七言绝句，按平水韵校平仄和粘对，每句藏一个剧情典故 |
| **色** | 克制色板：一种纸色、一种墨色，加一种强调色 |
| **笔** | Art Deco 墨线，或 11 种中国古典人物画法：洛神赋、吴带当风、唐仕女、敦煌飞天、李公麟白描、陈洪绶、十二金钗……每种都附提示词骨架和高清图链接，见 [styles/classical-styles.md](styles/classical-styles.md) |

| 角色 | 判词 |
|---|---|
| 希露菲 | 青丝一夜化霜华，墨镜藏眸入帝家。莫道重逢人不识，春风原是旧时花。 |
| 洛琪希 | 心声难解别家乡，一骑携童出院墙。弟子焚香尊若圣，十年笑约作新娘。 |
| 艾莉丝 | 赤焰飞扬意气高，留书断发入风涛。霜锋磨尽圣门雪，未诉相思先拔刀。 |

系列合成脚本在 `compose/`：`compose_lib.py` 是系列版（固定版式骨架，指定哪几条边出血、不羽化，其余边提亮），`compose_bw.py` 让半句之间只空半格，`example_mushoku.py` 是上面这三张的参数。

## English

**poem-plate** is an agent skill that turns classical Chinese poems and characters into minimal, print-like illustrated plates. An image model draws the figure; `compose_lib.py` scales it to one side, maps everything to a strict cream / near-black / single-gold palette, feathers the edges, and typesets the poem, its source, and a signature vertically in the empty space. A strong reviewer model scores each plate and blocks delivery on P0 issues (malformed hands, wrong characters, wrong-era costume). The skill itself is written in Chinese.

## 安装

```bash
mkdir -p ~/.claude/skills/poem-plate
cd ~/.claude/skills/poem-plate
for f in SKILL.md compose_lib.py example_compose.py; do
  curl -LO https://raw.githubusercontent.com/ythx-101/poem-plate/main/$f
done
pip install numpy pillow
```

需要一个中文衬线字体（推荐 [Noto Serif SC](https://fonts.google.com/noto/specimen/Noto+Serif+SC) Light），用 `POEM_FONT` 指定路径；`POEM_SIGNATURE`、`POEM_HANDLE` 改成你自己的署名。

## License

MIT

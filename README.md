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

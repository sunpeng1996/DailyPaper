---
title: Scaling Creative Writing Beyond Story-Centric Data with Attribute-Guided Genre
  Expansion
title_zh: 基于属性引导体裁扩展的跨类创意写作数据扩增方法
authors:
- Hwan Chang
- Yongil Kim
- Heuiyeen Yeen
- Yireun Kim
- Jinsik Lee
- Hwanhee Lee
affiliations:
- Chung-Ang University
- LG AI Research
arxiv_id: '2608.13947'
url: https://arxiv.org/abs/2608.13947
pdf_url: https://arxiv.org/pdf/2608.13947
published: '2026-08-14'
collected: '2026-08-17'
category: LLM
direction: 生成式内容创作 · 合成数据扩增
tags:
- Creative Writing
- Synthetic Data Generation
- Genre Control
- LLM Fine-tuning
- Data Scaling
one_liner: 提出属性引导的体裁扩展框架，构建5万条多体裁数据集，显著提升LLM跨类创意写作能力
practical_value: '- 电商文案生成场景可复用「属性引导+通用创意种子」的合成数据范式，用人工标注的文案体裁属性（短标题、直播话术、详情页文案等）约束通用prompt种子生成高质量标注对，大幅降低标注成本

  - 多场景Agent的内容生成模块可参考体裁拆分控制思路，将主题内容生成与格式/风格/结构约束解耦，提升不同业务场景下内容输出的合规性与匹配度

  - 生成式推荐的配套文案生成任务做模型微调时，可优先扩增不同体裁的标注数据而非单纯堆叠同类型数据，投入产出比更高'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
当前LLM的高质量创意写作训练数据以故事类为主，导致模型无法适配不同体裁的结构、风格、格式要求，跨类创作能力弱，覆盖场景有限。

### 方法关键点
1. 提出属性引导的体裁扩展框架，将主题广度和体裁格式控制解耦：以人工创作的故事prompt为通用创意种子，搭配人工标注的体裁属性（结构、风格、格式规则）引导大模型生成符合体裁要求的query-response对，再经质量过滤得到可用训练数据
2. 基于该框架构建了50K条覆盖13类创意体裁（故事、rap、歌词、剧本、游戏设计、角色设计等）的多体裁数据集

### 关键结果
在分布外写作基准、未见过的体裁测试集上，微调后的模型性能超过base模型、写作专用基线模型、在现有公开写作语料上训练的模型；消融实验显示受控体裁扩增相比单纯堆叠故事类数据，是提升创意写作鲁棒性的核心驱动因素

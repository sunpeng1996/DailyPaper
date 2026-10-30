---
title: 'How I Aligned Your Model: Scaling Up Multilingual Safety Training with Templates'
title_zh: 基于模板的规模化多语言LLM安全对齐训练框架
authors:
- Max Neuwinger
- Hanna Yukhymenko
- Imanol Schlag
affiliations:
- ETH Zurich
arxiv_id: '2610.40516'
url: https://arxiv.org/abs/2610.40516
pdf_url: https://arxiv.org/pdf/2610.40516
published: '2026-10-29'
collected: '2026-10-30'
category: Training
direction: LLM安全对齐 · 多语言训练
tags:
- Multilingual Alignment
- Safety Alignment
- Synthetic Data
- Low-resource Language
- LLM Training
one_liner: 提出模板化多语言安全对齐pipeline，生成覆盖60种语言的MSAFETEMP数据集，填补低资源语言安全训练缺口
practical_value: '- 跨语种电商/广告LLM合规对齐可复用该模板填充pipeline，将中文合规prompt扩展到小语种，规避纯翻译导致的本地化合规失效，大幅降低多语言合规数据标注成本

  - 多语言Agent/生成式推荐的安全评测可直接复用MSAFETEMP的低资源语言子集，快速验证小语种场景下的内容合规性，补充现有评测集的本地化缺口

  - 生成式推荐的多语言文案增强可借鉴该思路，通用模板填充本地节日、本土品牌等实体，提升小语种市场的推荐文案相关性与合规性'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前LLM安全对齐严重英语中心化，低资源语言防护能力极弱，纯翻译的安全数据缺少本地化文化语境，常出现英语下被拒绝的有害请求，翻译并适配本地文化后模型却违规响应的问题；同时人工标注多语言安全数据成本高、效率低，直接请求大模型生成有害内容还会触发其安全拦截，规模化生产多语言安全数据难度极高。
### 方法关键点
- 从英语有害种子prompt中提取带类型的槽位（如`<public_figure>`、`<illicit_substance>`）生成无危害模板，仅翻译模板文本保留槽位，规避生成模型的安全拦截
- 为每一种语言生成本地文化卡片，包含本土组织、事件、敏感概念等实体，分别填充有害/良性实体生成对应有害prompt和匹配的良性对照样本，同时控制过拒绝问题
- 采用双阶段异源LLM judge验证所有生成样本的有害性、语言流畅度、文化适配性，过滤不合格样本
### 关键结果
- 生成的MSAFETEMP数据集包含44种语言的1.84M训练样本、60种语言的217k评测样本，人工验证自然度4.43/5、文化适配度4.46/5，91%的有害样本标签获得专家认可
- 仅用英语评测会严重低估多语言安全风险：Olmo等模型英语下攻击成功率（ASR）为0%，翻译为其他语言后ASR升至13.7%，45%的安全漏洞仅能通过本地化实体样本发现
- 基于MSAFETEMP做SFT+DPO训练，可将多语言场景ASR降低70%以上，未出现在训练集中的语言安全提升幅度与训练集语言接近，跨语言迁移效果显著

> 最值得记住的一句话：多语言安全能力不能依赖英语对齐的跨语言迁移，必须同时覆盖语言、文化两个维度的适配，英语场景的安全指标完全无法代表小语种场景的真实安全水平。

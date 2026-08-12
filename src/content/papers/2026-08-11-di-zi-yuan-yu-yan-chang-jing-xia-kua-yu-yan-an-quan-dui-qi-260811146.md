---
title: The Illusion of Cross-Lingual Safety in Low-Resource Languages
title_zh: 低资源语言场景下跨语言安全对齐的幻觉
authors:
- Abigail Oppong
- P Sam Sahil
- Tadesse Destaw Belay
- Maryam Ibrahim Mukhtar
- Esmael Ahmed Abdu
- Tassallah Abdullahi
- Jessica Oparebea
- Saminu Mohammad Aliyu
- Idris Abdulmumin
- Abubakar Juma Chilala
affiliations:
- Makerere University Center for Artificial Intelligence
- University of Hamburg
- Instituto Politécnico Nacional
- Bayero University, Kano
- Wollo University
arxiv_id: '2608.11146'
url: https://arxiv.org/abs/2608.11146
pdf_url: https://arxiv.org/pdf/2608.11146
published: '2026-08-11'
collected: '2026-08-12'
category: LLM
direction: 大语言模型 · 跨语言安全对齐
tags:
- LLM Safety
- Cross-lingual Alignment
- Low-resource Language
- Safety Probing
- Alignment Dataset
one_liner: 针对4种非洲低资源语言，提出安全数据集与隐层几何探测框架，证实跨语言安全迁移效果极弱
practical_value: '- 做多语种跨境电商Agent/客服LLM的团队，不能默认英文安全对齐能力可迁移到小语种，必须针对目标低资源语言做单独的安全对齐微调，避免违规内容输出

  - 多语种LLM安全评估时不能只测直译prompt，需补充本地化文化相关的恶意prompt，避免漏判安全风险

  - 可复用论文提出的隐层拒绝表征探测方法，无需等待生成内容即可快速评估LLM在小语种下的安全能力，提升评测效率'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
当前LLM安全对齐多基于英文实现，行业默认安全能力可跨语言泛化，但该假设在低资源语言下缺乏验证，存在重大安全漏洞。

### 方法关键点
1. 构建LoDNA安全数据集，覆盖Twi、豪萨语、阿姆哈拉语、斯瓦希里语4种非洲低资源语言，包含直译和文化本地化的配对恶意prompt
2. 提出隐层几何探测框架，通过分析LLM隐层拒绝表征判断安全响应触发情况，突破生成式评测的局限性

### 关键结果数字
多数LLM-低资源语言配对下，恶意prompt仅保留不到10%的英文场景拒绝信号；直译与本地化prompt语义余弦相似度达0.95~0.996，但隐层表征随层漂移，说明模型能理解语义但未触发安全机制，现有跨语言安全对齐仅为表层效果。

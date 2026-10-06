---
title: Frozen Factor or Spectral Band? Disentangling Two Choices in Low-Rank LoRA
title_zh: 低秩LoRA优化拆解：冻结因子与谱带选择的效果对比
authors:
- Adnan Slimane Ali
- Ayoub Belfatmi
- David Ngwe Pouth
affiliations:
- CentraleSupélec, Université Paris-Saclay
- École polytechnique, Institut Polytechnique de Paris
arxiv_id: '2610.06621'
url: https://arxiv.org/abs/2610.06621
pdf_url: https://arxiv.org/pdf/2610.06621
published: '2026-10-05'
collected: '2026-10-06'
category: Training
direction: 大模型高效微调 · LoRA策略优化
tags:
- LoRA
- PEFT
- Spectral Initialization
- Fine-Tuning
- Low Rank Adaptation
one_liner: 分离LoRA的冻结因子与谱带两种设计选择，量化低秩场景下冻结A的显著性能优势
practical_value: '- 低秩LoRA（rank≤8）垂域微调场景（比如电商文案生成、Agent工具调用能力微调）优先选择冻结A训练B的方案，同参数下效果比冻结B高6~19pp，即使A用随机正交基初始化效果也优于谱带初始化的冻结B方案

  - 做不同LoRA变种的业务选型对比时，必须为每个配置单独搜索最优学习率，固定学习率的对比结果可能完全失真，过往部分LoRA变种的宣称优势可能来自调参不充分

  - rank≥16的高秩LoRA场景下，冻结A的优势大幅收窄，和谱带选择的效果影响相当，此时无需刻意选择冻结方案，优先按参数量预算选型即可'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有谱LoRA变种（MiCA、PiCa等）的效果对比同时混淆了「冻结因子选择」和「谱带选择」两个独立设计变量，过往LoRA因子不对称研究未量化两类选择的效果差距，也未充分控制秩、参数量、调参等干扰变量，导致业务侧做LoRA选型时缺乏可落地的参考依据。
### 方法关键点
- 采用2×2对照实验设计：分别冻结A/冻结B，分别在预训练权重的top/bottom奇异方向初始化冻结因子，每个配置单独学习率搜索，排除调参偏差
- 新增两类对照组：同参数量的普通LoRA基线，以及给冻结B配置更多参数的对照，排除参数量差异的干扰
- 实验覆盖4款主流开源LLM（Llama-3.2-1B、Qwen2.5-1.5B/7B、Mistral-7B）、3类任务（结构化格式化生成、OpenBookQA、ARC常识问答）
### 关键结果
- rank=2低秩场景下，冻结A比同谱带的冻结B效果高6.6~19pp，而top/bottom谱带切换的效果差异最大仅5.2pp；冻结B比同参数量普通LoRA低8~18pp，即使给冻结B多18~22%的参数，仍比冻结A低6.3~12.2pp
- 冻结A的优势随秩升高持续下降，rank=16时因子差距和谱带差距相当（2.58pp vs 3.02pp）
- PEFT官方MiCA实现在统一迁移训练配方下，比同参数量普通LoRA低3.08pp
### 核心结论
低秩LoRA微调时，冻结哪个因子的优先级远高于选哪个谱带初始化，除非rank≥16否则优先选择冻结A训练B的方案

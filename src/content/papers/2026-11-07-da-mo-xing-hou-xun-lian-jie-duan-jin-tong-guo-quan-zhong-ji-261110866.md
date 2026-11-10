---
title: The Surprising Effectiveness of Deleting Weights in LLM Post-Training
title_zh: 大模型后训练阶段仅通过权重清零即可媲美全参数微调
authors:
- Jack Lu
- Zhenbang Yang
- Mike Lasby
- Tejas Pote
- Yani Ioannou
- Mengye Ren
affiliations:
- New York University
- University of Calgary
arxiv_id: '2611.10866'
url: https://arxiv.org/abs/2611.10866
pdf_url: https://arxiv.org/pdf/2611.10866
published: '2026-11-07'
collected: '2026-11-10'
category: Training
direction: 大模型高效微调 · 轻量化适配器
tags:
- Parameter-Efficient Fine-Tuning
- LLM Training
- Sparse Learning
- Continual Learning
- Deletion Tuning
one_liner: 仅学习Transformer门控层二值掩码删除0.05%以内权重，效果匹配全参数微调且遗忘率极低
practical_value: '- 可替代LoRA用于电商/推荐场景的LLM微调，适配器比r=1 LoRA更小，多任务切换仅需加载几MB掩码文件，大幅降低多场景LLM服务的存储和部署成本，适合商品文案生成、客服应答、推荐理由生成等多任务场景

  - 对于需要持续迭代的推荐/Agent场景（如按季度上新调整商品理解能力、迭代营销话术），Deletion Tuning的旧任务准确率仅下降不到1个点，远低于FFT、LoRA最高5.4点的下降幅度，无需反复在旧任务上重训

  - 微调仅需修改Transformer门控投影层参数，训练算力开销远低于全参数微调，中小团队也可快速迭代LLM相关的推荐、广告能力

  - 可直接复用Wanda初始化+掩码锐化的训练trick，无需复杂调参即可适配SFT、RLHF、知识蒸馏等多种微调范式，快速落地业务需求'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前LLM后训练方案存在明显痛点：全参数微调（FFT）存储成本高、 catastrophic forgetting 严重；LoRA等适配器方案虽轻量化，但仍存在遗忘问题、存算开销仍有优化空间；现有稀疏方法多为推理加速设计，从未将权重删除作为微调的核心机制，亟需更轻量、遗忘更低的微调方案。

### 方法关键点
- 核心方案为Deletion Tuning，仅针对Transformer块的门控投影层学习二值掩码，原始预训练权重完全冻结，推理时仅将掩码为负的权重清零，其余权重保留预训练值
- 训练阶段采用sigmoid+掩码锐化策略，逐步提高sigmoid陡峭度，最终收敛到硬二值掩码；基于Wanda剪枝分数初始化掩码，搭配稀疏正则化约束
- 无缝兼容GRPO（可验证奖励强化学习）、SFT、SDFT（在线蒸馏）三种主流微调范式，无需修改原训练目标

### 关键实验
- 实验覆盖0.5B~30B参数的Llama、Qwen系列模型，对比基线包括FFT、LoRA（r=1/4）、MTH稀疏微调等
- 7B/8B及以上规模模型效果完全匹配FFT：Llama8B在GSM8K上准确率达83.55%（FFT为83.24%），Qwen30B MoE在SimpleRL-Zoo上准确率达58.54%（FFT为58.43%）
- 适配器大小比FFT小3~4个数量级，8B模型仅8.4MB，比r=1 LoRA更小；RL训练场景下旧任务准确率仅下降不到1个点，远低于FFT、LoRA最高5.4点的下降幅度

### 最值得记住的一句话
大模型后训练不需要修改权重取值，仅删除极少量门控层权重就能获得和全参数微调相当的效果，同时极大降低存储开销和遗忘率。

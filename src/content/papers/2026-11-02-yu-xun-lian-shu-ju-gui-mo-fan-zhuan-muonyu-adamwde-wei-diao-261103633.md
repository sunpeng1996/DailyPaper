---
title: Pretraining Data Scale Reverses the Muon-AdamW Fine-Tuning Gap
title_zh: 预训练数据规模反转Muon与AdamW的微调效果差距
authors:
- Catherine Li
- Jingchu Gai
- Andrej Risteski
- Jacob Mitchell Springer
- Aditi Raghunathan
affiliations:
- Carnegie Mellon University
arxiv_id: '2611.03633'
url: https://arxiv.org/abs/2611.03633
pdf_url: https://arxiv.org/pdf/2611.03633
published: '2026-11-02'
collected: '2026-11-03'
category: Training
direction: LLM训练 · 优化器选型与效果评估
tags:
- Muon
- AdamW
- Pretraining
- Fine-tuning
- LLM
- Optimization
one_liner: 揭示预训练数据与模型尺寸对Muon、AdamW微调效果的反转规律，提出MSR指标解释内在机制
practical_value: '- 垂域小模型（如电商文案生成、Agent决策小模型）预训练数据有限时，优先选Muon，可获得更好的微调学习-遗忘平衡

  - 大参数基座（如全域推荐大模型、通用电商Agent基座）搭配超大规模预训练数据时，优先选AdamW，微调后遗忘更少、下游表现更优

  - 可复用MSR指标预判基座模型的微调适配性，无需全量微调即可快速筛选预训练checkpoint，降低调优成本

  - 对于100M以上参数的垂域基座，AdamW在TPR≈20（训练token为参数20倍）时就可能超过Muon，优先做AdamW基线测试'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
Muon近期被证明在LLM预训练阶段收敛速度、预训练Loss均优于AdamW，但业界不清楚其预训练优势能否延续到微调阶段；而预训练优化器选型直接影响下游任务的学习-遗忘平衡，是大模型落地的核心痛点，尤其影响垂域基座、推荐/Agent大模型的下游适配效率。

### 方法关键点
- 预训练30M~600M参数的OLMo风格模型，覆盖150M~154B DCLM tokens，TPR（token-parameter ratio，单参数对应训练token数）范围5~2560
- 定义微调差距（GFT）量化AdamW与Muon的学习-遗忘帕累托前沿优劣，正号表示AdamW更优
- 提出MSR（margin-to-spread ratio）指标：正确logit相对错误logit的平均间隔与错误logit离散度的比值，量化模型对输出扰动的鲁棒性
- 通过线性联想记忆模型从理论上证明MSR随数据规模的变化规律，验证其与微调效果的相关性

### 关键实验结果
在GSM8K、StackMathQA、Alpaca、MusicPile四个数据集微调，共近600次预训练、29000次微调跑批：
- 小TPR下Muon更优，超过交叉TPR后AdamW反超，60M模型在StackMathQA任务上交叉TPR约为100
- 模型越大交叉TPR越小：30M模型交叉TPR为320，600M模型仅为10，即越大的模型AdamW越早反超Muon
- Muon的预训练Loss优势随模型增大而收窄，相同TPR下大模型中Muon的遗忘程度比AdamW高30%以上

**最值得记住的一句话**：不要仅用预训练Loss作为优化器选型的唯一标准，大模型+大规模预训练场景下AdamW的微调适配性显著优于Muon。

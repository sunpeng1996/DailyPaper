---
title: Verifier-Induced Support Reshaping in On-Policy Optimization
title_zh: 在策略优化中由验证器引发的支持域重塑
authors:
- Shaohang Wei
- Zikun Su
- Feifan Song
- Wen Luo
- Wei Li
- Guangyue Peng
- Houfeng Wang
affiliations:
- Peking University
- BUPT
arxiv_id: '2608.00220'
url: https://arxiv.org/abs/2608.00220
pdf_url: https://arxiv.org/pdf/2608.00220
published: '2026-07-30'
collected: '2026-08-17'
category: Training
direction: LLM对齐 · RLVR跨任务能力保留优化
tags:
- RLVR
- On-Policy Optimization
- Continual Learning
- LLM Alignment
- Support Reshaping
one_liner: 揭示RLVR训练引发的支持域重塑效应，验证其机制并测试现有缓解方案的局限性
practical_value: '- 若采用RL优化业务Agent/生成式推荐文案，除监控当前任务pass@1外，需新增best@k指标，避免后续迭代时可优化轨迹枯竭，无法适配新业务目标

  - RLVR对输出分布的改变高度集中在开头数个token，多目标优化时可显式约束不同任务的输出开头范式，降低不同阶段训练的互相干扰

  - 多阶段RL微调做OPD时，选择中等收敛程度的教师模型，比全收敛教师更易平衡当前任务收益与跨任务能力保留，避免能力坍缩'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前LLM后训练常采用多阶段RLVR（带可验证奖励的在策略强化学习）优化数学推理、指令遵循等任务，现有研究仅关注当前任务收益，忽略后续任务的可训练性：即使模型未遗忘相关能力，成功轨迹也可能因采样概率过低，在有限rollout预算下无法被捕捉，导致后续训练无正样本信号。

### 方法关键点
- 采用双向训练设计，从同一基座出发分别做Math-RLVR和IF-RLVR，再交叉训练另一任务，观测跨任务影响
- 定义effective rewardable support：固定rollout预算下可采样到的成功轨迹集合，用pass@1、best@k、pass-count等指标量化支持域变化
- 开展token级分布分析与干预实验，定位分布变化的发生位置与因果关系

### 关键结果
在Qwen3-8B-Base、Qwen2.5-Math-7B两个模型上测试：Math-RLVR使IFEval的pass@1提升6.5pp，但best@32下降9.8pp；IF-RLVR使AIME的best@k全采样预算下下降，回复开头从分步推理（DRI）向直接答案（DAI）偏移，DAI占比与best@32的皮尔逊相关系数为-0.85；现有KL约束、路由先验、OPD等缓解方案均只能部分保留跨任务支持，或需牺牲当前任务收益。

最值得记住的结论：在策略RL优化的终点指标提升，不代表未来可训练性或多任务联合能力得到保留。

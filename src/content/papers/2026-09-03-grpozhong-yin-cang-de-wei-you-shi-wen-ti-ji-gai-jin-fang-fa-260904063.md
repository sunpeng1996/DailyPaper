---
title: Spurious Advantage Hidden in GRPO
title_zh: GRPO中隐藏的伪优势问题及改进方法SIGNBALANCE
authors:
- Jiamian Wang
- Samyadeep Basu
- Koustava Goswami
- Tong Yu
- Zhiqiang Tao
affiliations:
- Rochester Institute of Technology
- Adobe Research
arxiv_id: '2609.04063'
url: https://arxiv.org/abs/2609.04063
pdf_url: https://arxiv.org/pdf/2609.04063
published: '2026-09-03'
collected: '2026-09-04'
category: Training
direction: LLM RL训练 · GRPO优化
tags:
- GRPO
- Advantage Estimation
- RLHF
- LLM Training
- Search Agent
one_liner: 发现GRPO组内优势估计的伪优势缺陷，提出无组依赖SIGNBALANCE提升有界任务与搜索Agent性能
practical_value: '- 电商/广告搜索多轮Agent的RL对齐场景可直接drop-in替换原生GRPO的优势估计为SIGNBALANCE，无需额外参数、无推理开销，能避免靠冗余搜索碰巧答对的伪信号误导，多跳QA场景增益可达7%+

  - 有界候选输出类业务（比如多选型query意图识别、有限SKU的个性化选品、优惠券面额决策）的RL微调优先采用SIGNBALANCE，对比原生GRPO在这类任务上平均准确率提升5%以上

  - 业务落地前可先统计任务的随机猜对基线，当基线>0.5%时SIGNBALANCE的增益会更显著，若任务为完全开放答案（比如长文案生成）则可直接用原生GRPO'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
GRPO是当前LLM RL微调（推理、Agent类任务）的主流算法，但其组内优势估计仅依赖组内对错样本比例，无法区分正确答案来自推理还是随机猜测，伪优势信号会误导策略学习猜答案而非真推理，在三类场景问题尤为突出：有界答案任务（如多选）、开放答案集中的有界子集、多轮搜索Agent（靠冗余搜索蒙对答案）。

### 方法关键点
- 提出SIGNBALANCE优势估计，完全解耦单条rollout的优势幅度与组内样本构成，从根源规避伪优势进入梯度
- 仅保留验证器给出的奖励符号，正样本采用全局固定优势幅度c，负样本通过stop-gradient的类间缩放（-c*sg[n+/n-]）实现batch级零均值平衡
- 无额外参数、无推理开销，是原生GRPO的完全可替换组件，PPO代理损失逻辑无需改动

### 关键实验结果
- 数学推理任务：Qwen2.5-0.5B上，相比原生GRPO，有界答案任务平均提升约6%（SAT-Math +6.26、AQuA +5.90），8个数据集平均准确率36.61%，超GRPO 2.37个点；3B模型上平均准确率43.78%，超GRPO 0.98个点，开放答案任务性能无损失
- 搜索Agent QA任务：Qwen2.5-7B上，6个QA数据集平均准确率37.80%，比SOTA Search-R1高1.8个点，多跳QA数据集2WikiMultiHopQA提升达7.62个点

### 核心结论
当RL任务存在非零的无推理猜对概率时，原生GRPO的组内优势放大机制必然引入伪信号，SIGNBALANCE是该场景下零成本的优先优化选择

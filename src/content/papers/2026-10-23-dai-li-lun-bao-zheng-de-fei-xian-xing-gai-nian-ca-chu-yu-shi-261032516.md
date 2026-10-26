---
title: Principled Nonlinear Concept Erasure and Steering
title_zh: 带理论保证的非线性概念擦除与表示调控方法
authors:
- Idan Simai
- Shauli Ravfogel
- Uri Shaham
affiliations:
- Bar-Ilan University
- New York University
arxiv_id: '2610.32516'
url: https://arxiv.org/abs/2610.32516
pdf_url: https://arxiv.org/pdf/2610.32516
published: '2026-10-23'
collected: '2026-10-26'
category: LLM
direction: LLM表示去偏 · 概念擦除与属性调控
tags:
- Concept Erasure
- Representation Steering
- Autoencoder
- Fairness
- PLM
one_liner: 提出带理论保证的条件自编码器框架，实现更优概念擦除trade-off与无额外成本的表示调控能力
practical_value: '- 电商/广告推荐场景可复用该框架消除用户/物品表示中的敏感属性（如性别、地域偏见），在几乎不损失推荐效用的前提下满足合规要求，抗非线性探针攻击能力远强于现有线性去偏方法

  - 生成式推荐/Agent的输出调控可复用其无额外训练的steering能力，仅需在推理时替换目标概念标签，即可实现输出属性的灵活切换（如营销文案风格调控、毒性内容过滤），无需微调大模型

  - 训练目标设计可直接复用「重构损失+HSIC独立性惩罚」的两阶目标，比现有基于对抗的去偏方法优化更简单、收敛更快，无需下游任务标签即可实现SOTA级别的效用-去偏trade-off'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有预训练语言模型的表示常编码性别、种族等敏感属性，易导致下游任务出现公平性问题。当前概念擦除方案存在明显短板：线性方法仅能防御线性探针，无法应对非线性攻击；非线性方法缺乏理论保证，易损失任务效用，且所有现有方法均不支持无额外成本的表示属性调控，难以同时满足工业场景对效用、去偏强度、可控性的三重需求。

### 方法关键点
- 采用条件自编码器架构：编码器将输入表示映射为与敏感概念独立的擦除后表示，解码器结合擦除后表示与敏感概念标签重构原始输入，天然具备属性调控能力
- 两阶段训练目标：仅用MSE重构损失保证非敏感信息最大限度保留，HSIC独立性惩罚保证擦除后表示与敏感属性统计独立，无需下游任务标签参与训练
- 提供完整理论保证：证明完美重构+群体级独立即可实现完美非线性防护，同时给出非完美重构场景下的效用保留量化边界

### 关键实验
在BIAS IN BIOS、DIAL-SENTIMENT、DIAL-MENTION 3个标准去偏数据集，覆盖BERT、GPT-2、DeepSeek-7B、LLaMA-3.2-1B 4种主流PLM，对比Obliviator、INLP等7种基线方法。在BIAS IN BIOS数据集上，性别预测准确率接近随机水平（56%）时，职业预测准确率达74%，比有监督SOTA方法Obliviator高出13个百分点；毒性调控任务中，在相同内容相关性下，相比MiMiC基线，PPL降低10.4%，毒性水平相当。

**最值得记住的一句话**：重构损失+独立性约束的简单组合，即可同时实现带理论保证的强非线性概念擦除和无额外训练成本的表示属性调控，trade-off表现远超现有复杂方案。

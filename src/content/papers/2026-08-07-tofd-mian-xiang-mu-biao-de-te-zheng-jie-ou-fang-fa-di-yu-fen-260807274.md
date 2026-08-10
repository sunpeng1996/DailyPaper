---
title: 'TOFD: Target-Oriented Feature Decoupling against Poisoning Attacks in Split
  Federated Learning'
title_zh: TOFD：面向目标的特征解耦方法，抵御拆分联邦学习投毒攻击
authors:
- Yuhan Xie
- Jingrong Huang
- Chen Lyu
affiliations:
- Shanghai University of Finance and Economics
- MoE Key Laboratory of Interdisciplinary Research of Computation and Economics
arxiv_id: '2608.07274'
url: https://arxiv.org/abs/2608.07274
pdf_url: https://arxiv.org/pdf/2608.07274
published: '2026-08-07'
collected: '2026-08-10'
category: Training
direction: 拆分联邦学习 · 投毒攻击防御
tags:
- Split Federated Learning
- Poisoning Attack Defense
- Feature Decoupling
- Robust Training
- Distributed Learning
one_liner: 提出三阶段TOFD框架，可在拆分联邦学习场景下同时实现多类投毒攻击的主动检测与鲁棒优化
practical_value: '- 跨端联邦联合训练用户/商品特征时，可复用Margin Perturbation阈值校准方法过滤恶意投毒的客户端特征数据，降低投毒对推荐模型效果的影响

  - 分布式训练场景下的特征污染防御可参考TOFD的三阶段架构，先识别攻击目标再过滤污染样本最后解耦攻击影响，兼顾鲁棒性和计算开销

  - 多机构联合训练广告/推荐模型时，可直接复用TOFD的收敛理论保证方案，快速落地低开销的投毒防御能力'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
Split Federated Learning (SFL) 可降低客户端计算开销实现隐私保护协同训练，但拆分架构新增攻击面，易受各类投毒攻击，现有防御未利用拆分范式特性，无法提前检测和遏制恶意行为。
### 方法关键点
TOFD包含三阶段：1）目标推理：通过类别专属Margin Perturbation (MP) 细化类别安全区，识别潜在攻击目标；2）样本净化：通过跨类MP的min-max归一化校准阈值，自适应过滤被投毒的smashed数据；3）解耦优化：用对抗引导模型捕获攻击诱导模式，在优化时解耦其影响，抑制残留对抗效应，且提供收敛性理论保证。
### 关键结果
5个数据集的实验显示，TOFD在各类攻击场景下均优于SOTA防御方案，鲁棒性更优且计算开销极低，适合实际部署。

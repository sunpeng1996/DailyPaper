---
title: Difficulty Calibration Across Time for Membership Inference in Diffusion Models
title_zh: 面向扩散模型成员推理的跨时间难度校准方法
authors:
- Michael Joseph
- Yedid Hoshen
affiliations:
- The Hebrew University of Jerusalem
arxiv_id: '2610.40616'
url: https://arxiv.org/abs/2610.40616
pdf_url: https://arxiv.org/pdf/2610.40616
published: '2026-10-29'
collected: '2026-11-01'
category: Other
direction: 扩散模型隐私审计 · 成员推理攻击
tags:
- Diffusion Model
- Membership Inference
- Calibration
- Privacy Audit
- Copyright Protection
one_liner: 通过训练时间、扩散时间双维度校准，大幅提升扩散模型成员推理攻击的准确率与泛化性
practical_value: '- 若业务使用扩散模型生成商品/广告素材，可复用RMC/TSC方法审计训练集是否混入未授权版权图、用户隐私图，规避合规风险

  - 做生成式模型隐私防护时，可针对「记忆信息在扩散时间上局部化、固有难度跨噪声水平持续」的特性，设计混淆策略降低MIA攻击成功率

  - 对黑盒扩散模型做版权溯源时，TSC仅需单模型无需历史checkpoint的特性可大幅降低审计成本'
score: 4
source: arxiv-cs.LG
depth: abstract
---

**动机**：当前扩散模型依赖海量无标注训练数据，易混入版权/隐私内容，传统成员推理攻击（MIA）仅用重构损失判断样本是否属于训练集，因样本固有重构难度差异准确率极低，无法区分「易重构的非训练样本」和「难重构的训练样本」。
**方法关键点**：采用双时间维度校准思路，分离样本固有难度和模型记忆效应；Reference-Model Calibration（RMC）对比微调后模型与更早checkpoint的损失差，隔离新记忆的样本，适配有历史checkpoint的场景；Temporal Self-Calibration（TSC）基于「样本固有难度跨噪声水平持续、记忆效应仅在特定扩散时间步出现」的观测，对比目标时间步与相邻时间步的损失抵消难度影响，仅需单模型即可实现。
**关键结果**：效果大幅超越现有SOTA，可泛化到x-、v-、ε-预测等不同参数化的扩散模型，RMC在无文本标注场景也可实现近完美审计

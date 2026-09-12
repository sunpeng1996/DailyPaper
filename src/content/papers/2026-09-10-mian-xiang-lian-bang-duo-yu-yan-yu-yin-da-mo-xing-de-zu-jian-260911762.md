---
title: Component-Aware Differential Privacy for Federated Multilingual Speech-LLMs
title_zh: 面向联邦多语言语音大模型的组件感知差分隐私方法
authors:
- Jordi Luque
- Fernando López
- Aleix Sant
affiliations:
- Telefónica Innovación Digital
- Universidad Autónoma de Madrid
- Universitat Politècnica de Catalunya
arxiv_id: '2609.11762'
url: https://arxiv.org/abs/2609.11762
pdf_url: https://arxiv.org/pdf/2609.11762
published: '2026-09-10'
collected: '2026-09-12'
category: Training
direction: 大模型联邦训练 · 差分隐私优化
tags:
- Differential Privacy
- Federated Learning
- Speech-LLM
- Gradient Clipping
- Privacy Protection
one_liner: 提出α-split双池梯度裁剪方案，解决联邦语音LLM跨组件差分隐私预算崩溃问题
practical_value: '- 做跨模态/多组件大模型（如含召回、排序模块的端到端推荐大模型）联邦隐私训练时，不要用单池分层裁剪，需按组件拆分独立梯度池，避免预算崩溃

  - 有隐私合规要求的大模型训练可复用α-split双池分配策略，在满足DP要求前提下最小化精度损失

  - 多组件大模型梯度裁剪可根据各组件更新范数差异动态分配预算，平衡不同模块的隐私保护强度与性能开销'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有分层差分隐私（DP）梯度裁剪按参数规模分配预算，在语音LLM场景完全失效：声学编码器与语言解码器的更新范数差1个数量级，单池分层方法会出现跨组件预算崩溃，导致WER大幅上升甚至训练完全失败，单池自适应方案仅能缓解轻度范数不平衡问题。
### 方法关键点
提出α-split双池分配机制：将编码器和LLM参数划入独立梯度池分别做裁剪，不改变原(ε,δ)-DP安全保证与联合ℓ₂敏感度，α参数根据模型架构动态校准。
### 关键结果
校准α后，模型WER性能与全局平裁剪相当；编码器抗说话人语音梯度反转攻击的保护强度提升4.47倍，仅带来2.6%的LLM噪声额外开销。

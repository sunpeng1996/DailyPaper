---
title: 'Gradient Mirage: Trainable yet Label-Unidentifiable Gradients in Large Language
  Model Split Learning'
title_zh: 梯度幻影：大模型拆分学习下可训练且标签不可识别的梯度防御
authors:
- Shiyu Miao
- Yunlong Mao
- Zirui Huang
- Liang Yao
- Tianshuo Zheng
- Yanhui Gu
- Fan Liu
- Sheng Zhong
affiliations:
- 南京大学
- 河海大学
- 南京师范大学
arxiv_id: '2608.18767'
url: https://arxiv.org/abs/2608.18767
pdf_url: https://arxiv.org/pdf/2608.18767
published: '2026-08-19'
collected: '2026-08-20'
category: Training
direction: 大模型拆分训练 · 隐私防御
tags:
- Split Learning
- Gradient Privacy
- Differential Privacy
- LLM Fine-tuning
- Adversarial Defense
one_liner: 提出三重梯度混淆防御方案，在保留微调性能的同时抵御大模型拆分学习中的梯度匹配攻击
practical_value: '- 端云协同LLM微调/个性化训练场景，可直接复用三重梯度混淆策略，在保护用户侧行为、prompt等标签隐私的同时不损失训练效果

  - 基于vMF的方向差分隐私机制可迁移到联邦推荐、用户侧LoRA微调场景，在梯度交互环节实现可控的隐私-精度权衡

  - 双轨反向传播+底层梯度恢复架构可用于拆分部署的生成式推荐模型训练，避免暴露用户侧敏感交互数据'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
LLM拆分学习广泛用于端云协同训练场景，但现有梯度匹配攻击（GMA）可通过拆分层暴露的梯度反推客户端私有标签，现有防御方案普遍存在隐私性不足或训练效用损失过大的问题。
### 方法关键点
核心思路是打破梯度与客户端原始训练目标的一致性，构造攻击者无解的逆问题：1）选择性自回归监督：基于掩码替代损失生成暴露给服务端的梯度，破坏目标一致性；2）尺度混淆：对梯度乘随机系数隐藏原始量级；3）方向私有化：基于von Mises-Fisher机制对梯度方向加噪，满足方向度量差分隐私；配套双轨反向传播、底层梯度恢复策略，保证上下游模型训练的梯度有效性。
### 关键结果
实验验证，在微调性能与baseline持平的前提下，Gradient Mirage的隐私防护能力显著优于现有防御方案，实现更优的隐私-效用权衡

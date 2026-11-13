---
title: On the Difficulty of Sequence-Level Supervised Learning for Autoregressive
  Language Models
title_zh: 自回归语言模型序列级监督学习的难点分析
authors:
- Mathieu Blondel
- Michaël E. Sander
- Germain Vivier-Ardisson
- Tianlin Liu
- Vincent Roulet
affiliations:
- Google DeepMind
arxiv_id: '2611.16736'
url: https://arxiv.org/abs/2611.16736
pdf_url: https://arxiv.org/pdf/2611.16736
published: '2026-11-12'
collected: '2026-11-13'
category: Training
direction: 自回归模型训练 · 序列级损失分析
tags:
- Autoregressive LM
- Teacher Forcing
- Sequence-level Loss
- Exposure Bias
- Supervised Learning
one_liner: 证明两类序列级监督损失存在根本性缺陷，AR模型监督阶段teacher forcing已足够
practical_value: '- 做生成式推荐、LLM文案生成等AR任务的监督训练时，无需尝试自研序列级损失，直接使用teacher forcing + token级交叉熵即可，避免无意义的踩坑

  - 若需解决exposure bias问题，不要改动损失函数，优先选择在线策略蒸馏（仍用token级交叉熵）或RL后训练的路径，工程可行性更高

  - moment matching+stop gradient的更新方向理论有效但方差随序列长度激增，长序列生成场景（如多轮Agent对话、长文案生成）不建议落地'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
自回归（AR）模型监督训练普遍采用teacher forcing的token级交叉熵损失，但存在训练-推理不匹配的exposure bias问题，业界长期尝试设计结合推理时解码逻辑的序列级损失解决该问题，但此前未明确这类损失的可行性边界。
### 方法关键点
1. 分析基于贪婪解码的序列级损失，推导证明其存在不连续、非凸、下界无界的根本性缺陷，训练时损失会发散到-∞，完全不可用
2. 分析基于自回归采样的序列级损失，同样证明其非凸、下界无界；通过提出自回归Gumbel trick，证明两类损失本质同源，采样损失是加入Gumbel扰动的贪婪损失的期望
3. 尝试通过stop gradient消除解码序列对模型参数的依赖，得到moment matching更新方向，证明其是AR负对数似然的有效下降方向，但该方向方差随序列长度线性增长，实用价值有限
### 关键结果
本文为纯理论推导工作，无实证实验数据，最终结论为：针对静态数据集的AR模型监督学习，teacher forcing已是最优选择，无需设计替代序列级损失。
### 核心结论
teacher forcing may well be "all you need" for the supervised learning phase of AR models from static datasets

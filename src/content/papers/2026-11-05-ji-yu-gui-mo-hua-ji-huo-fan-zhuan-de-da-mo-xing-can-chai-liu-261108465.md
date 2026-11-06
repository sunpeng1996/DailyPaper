---
title: Towards interpreting any residual stream direction by scaling activation inversion
title_zh: 基于规模化激活反转的大模型残差流任意方向解释方法
authors:
- Celeste De Schamphelaere
- Juan J. Vazquez
- Ari Spiesberger
- Tomáš Gavenčiak
- Gavin Leech
- Euan Ong
- Jiahai Feng
affiliations:
- MATS
- Arb Research
- Charles University
- Anthropic
arxiv_id: '2611.08465'
url: https://arxiv.org/abs/2611.08465
pdf_url: https://arxiv.org/pdf/2611.08465
published: '2026-11-05'
collected: '2026-11-06'
category: LLM
direction: 大模型可解释性 · 残差流激活反转
tags:
- LLM Interpretability
- Residual Stream
- Activation Inversion
- SAE
- LoRA
one_liner: 提出MAEM元模型，可将目标模型残差流方向映射为高激活文本样例，具备高解释性与可验证性
practical_value: '- 做LLM4Rec可解释性时，可复用MAEM思路将推荐模型隐层激活方向转换为可解释文本，定位用户偏好/Item Embedding对应的语义概念

  - 检测LoRA微调的推荐/广告大模型后门风险时，可复用MAEM反查LoRA隐层向量对应的异常语义，保障线上模型安全性

  - 做Agent推理过程可解释性时，可通过MAEM将Agent工作区残差流激活转为自然语言，复盘决策逻辑，定位推荐/广告决策错误根因'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有大模型残差流方向解释依赖语料库扫描，受限于语料覆盖范围，无法适配任意残差方向的解释需求，也难以覆盖低资源语言、小众领域语义。
### 方法关键点
提出Maximally-Activating Example Metamodels（MAEMs），采用无标注RL训练目标，最大化输入残差流方向与MAEM生成文本在冻结目标模型对应层激活的余弦相似度，实现残差方向到高激活文本样例的端到端映射。
### 关键结果
- 基于Qwen3.6-27B的MAEM反演效果优于10M token语料搜索与自然语言自编码器（NLA），在多数跨语言/跨领域测试集表现更优
- 可激活89%的未见过的SAE特征，LoRA后门载荷识别率高于语料搜索
- 支持将模型工作区内部推理状态转换为自然语言，生成结果可通过目标模型前向传播直接验证

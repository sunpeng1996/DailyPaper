---
title: 'Beyond Paired Inputs: Learning to Leverage RGB-T Cross-Modal Relations in
  Multimodal Large Language Models'
title_zh: 超越配对输入：多模态大模型的RGB-T跨模态关系学习方法
authors:
- Tianyi Zhao
- Qihao Xu
- Jiawen Xi
- Duanni Meng
- Bo Zhao
- Maoxun Yuan
- Xingxing Wei
- Bo Li
affiliations:
- Beihang University
- Fudan University
arxiv_id: '2611.19493'
url: https://arxiv.org/abs/2611.19493
pdf_url: https://arxiv.org/pdf/2611.19493
published: '2026-11-14'
collected: '2026-11-17'
category: Multimodal
direction: 多模态大模型 · RGB-T跨模态关系建模
tags:
- MLLM
- Cross-Modal Learning
- RGB-T
- Reward Engineering
- Multimodal Reasoning
one_liner: 提出RelMLLM框架，显式建模RGB-T跨模态关系提升多模态任务性能与鲁棒性
practical_value: '- 电商多模态推荐的特征融合环节可借鉴模态可靠性、主导模态的显式建模逻辑，替代直接拼接多模态特征的方案，提升弱光照、低画质等异常商品素材下的推荐鲁棒性；

  - 跨模态监督信号可通过对比单模态、多模态任务结果自动构造的思路，可复用在多模态推荐模型训练中，降低跨模态对齐的人工标注成本；

  - 分层奖励强制证据、关系、决策一致性的设计，可迁移至多模态导购Agent的决策对齐任务，减少Agent多模态输入理解错误导致的答非所问问题。'
score: 7
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有处理RGB-T输入的MLLM仅支持配对输入推理，无法将跨模态互补关系转化为任务决策，模态互补性的性能、鲁棒性增益未被充分释放。
### 方法关键点
1. 提出RelMLLM框架，将模态可靠性、跨模态关系、主导模态抽象为可验证的决策状态；
2. 对比仅RGB、仅TIR、配对RGB-T三类输入的任务输出，自动生成决策状态的任务关联监督信号，无需额外标注；
3. 设计分层关系引导奖励，同时监督模态证据提取、关系状态预测、最终任务输出三个环节，强制三者逻辑一致性。
### 关键结果
相比Qwen3-VL基线，RGB-T grounding准确率提升，传感器退化场景下鲁棒性显著增强，通用RGB-T推理基准性能无损失。

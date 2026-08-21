---
title: 'PEA-DPO: Perception-Enhanced Alignment Direct Preference Optimization for
  MLLMs Alignment'
title_zh: PEA-DPO：面向多模态大模型对齐的感知增强直接偏好优化
authors:
- Jiawei Feng
- Jiancan Wu
- Xingyu Zhu
- Junkang Wu
- Xiang Wang
- Xiangnan He
affiliations:
- University of Science and Technology of China
- National University of Singapore
arxiv_id: '2608.19598'
url: https://arxiv.org/abs/2608.19598
pdf_url: https://arxiv.org/pdf/2608.19598
published: '2026-08-20'
collected: '2026-08-21'
category: Training
direction: 多模态大模型 · DPO对齐训练优化
tags:
- MLLM
- DPO
- Alignment
- Hallucination Mitigation
- Multimodal Training
one_liner: 针对多模态DPO的视觉不敏感问题，提出感知增强对齐框架，降低幻觉提升多模态对齐效果
practical_value: '- 做电商多模态商品理解、短视频内容标签生成的MLLM微调时，可替换普通DPO为PEA-DPO，减少多模态幻觉，提升视觉内容识别准确率

  - 跨图像/同图像的视觉不敏感问题分析框架可直接复用，用于排查业务中MLLM视觉理解错误的根因

  - 对齐训练时显式引入视觉偏好信号的思路，可迁移到多模态生成式推荐的模型对齐环节，降低推荐结果与用户视觉偏好的 mismatch'
score: 7
source: arxiv-cs.MM
depth: abstract
---

### 动机
DPO在LLM人类偏好对齐中效果优异，但迁移到多模态场景时存在显著的视觉不敏感问题，分为跨图像不敏感（无法区分不同图像的响应差异）和同图内不敏感（无法捕捉单张图像内关键视觉上下文的缺失），易引发幻觉，制约多模态大模型落地。

### 方法关键点
提出PEA-DPO对齐框架，在DPO训练过程中显式引入视觉偏好信号，理论层面证明可同时缓解两类视觉不敏感问题，且能保留基础模型的原生语言建模能力。

### 关键结果
在3个主流多模态幻觉评测基准上测试，不同参数量级的MLLM采用PEA-DPO训练后，视觉上下文敏感度显著提升，幻觉率大幅降低，多模态对齐效果全面优于原生DPO方法。

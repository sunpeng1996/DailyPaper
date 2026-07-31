---
title: 'Veritas++: Value-aware On-Policy Distillation for Perception-Enhanced AIGI
  Detection'
title_zh: Veritas++：面向感知增强AIGI检测的价值感知在策略蒸馏
authors:
- Hao Tan
- Jun Lan
- Zichang Tan
- Ajian Liu
- Zijian Yu
- Chuanbiao Song
- Huijia Zhu
- Weiqiang Wang
- Jun Wan
- Zhen Lei
arxiv_id: '2607.27113'
url: https://arxiv.org/abs/2607.27113
pdf_url: https://arxiv.org/pdf/2607.27113
published: '2026-07-29'
collected: '2026-07-31'
category: Multimodal
direction: 多模态AIGI检测 · 感知能力增强
tags:
- MLLM
- AIGI Detection
- On-Policy Distillation
- Perception Learning
- Multimodal
one_liner: 提出感知增强AIGI检测框架Veritas++，通过定向学习与自适应蒸馏提升异常捕捉泛化性
practical_value: '- 电商营销素材/商品图审核场景可复用PoRL机制，用可验证奖励替代开放描述监督，提升AI生成虚假图的细粒度异常捕捉准确率

  - 做垂类小模型蒸馏时可借鉴VaOPD自适应蒸馏策略，优先筛选高价值蒸馏信号，在不损失原有检测能力的前提下快速迭代新识别维度

  - 可解释内容审核场景可复用「基础感知能力打底+上层推理」的架构，检测结果可关联具体视觉异常点，降低人工审核校验成本'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
AIGC生成图在公开场景普及，现有基于MLLM的AIGI检测器存在明显感知瓶颈，对细粒度、像素级、语义层面的异常捕捉能力不足，过往优化多侧重推理逻辑组织，忽略底层感知能力建设。
### 方法关键点
1. 基于「可靠感知是真实性推理基础」的思路搭建Veritas++框架，将AIGI检测锚定在细粒度视觉细节捕捉、语义异常识别、像素级差异感知三类基础能力上
2. 设计Perception-oriented Learning（PoRL），用可验证奖励替代开放式描述监督，定向强化三类感知能力
3. 提出Value-aware On-Policy Distillation（VaOPD）自适应蒸馏机制，优先处理高价值蒸馏信号，通过特权自教师内化感知增强的推理逻辑
### 关键结果
在标准、真实场景、新兴三类基准上均取得优异泛化表现，感知学习可无副作用提升检测效果，VaOPD可在不损失原有性能的前提下实现能力高效迭代

---
title: 'Breaking Failure Cascades: Step-Aware Reinforcement Learning for Medical Multimodal
  Reasoning'
title_zh: 破解错误级联：面向医疗多模态推理的步骤感知强化学习
authors:
- Junha Jung
- Minbyul Jeong
- Suhyeon Lim
- Sungwook Jung
- Jaehoon Yun
- Taeyun Roh
- Mujeen Sung
- Jaewoo Kang
affiliations:
- Korea University
- Upstage AI
- Kyung Hee University
- KAIST
- Hanyang University College of Medicine
arxiv_id: '2606.31825'
url: https://arxiv.org/abs/2606.31825
pdf_url: https://arxiv.org/pdf/2606.31825
published: '2026-06-30'
collected: '2026-07-01'
category: Reasoning
direction: 多模态推理 · 分步RL优化
tags:
- Reinforcement Learning
- Multimodal Reasoning
- Credit Assignment
- MLLM
- Step-wise Reward
one_liner: 提出带分步过程奖励的MRPO算法，破解医疗多模态推理错误级联，提升推理准确率
practical_value: '- 电商导购Agent、多步决策推荐场景可复用分步奖励机制，对早期错误步骤分配更高惩罚，减少错误级联导致的最终结果偏差

  - LLM/Agent的RL优化中可借鉴稀疏信用分配解法，不依赖单一最终结果奖励，拆分中间步骤奖惩信号提升训练效率

  - 业务垂直场景中小参数模型可通过针对性过程优化，效果超过大参数模型，降低推理部署成本'
score: 7
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有多模态大模型后训练pipeline以结果为核心，仅依赖最终答案正确性或序列级偏好做监督，存在严重的稀疏信用分配问题，早期推理步骤的错误会引发级联效应，是医疗VQA任务预测错误的核心诱因。
### 方法关键点
提出MRPO（Medical Reasoning-aware Policy Optimization）强化学习算法，引入分步过程奖励机制：当最终答案错误时，对越早出现的无效推理步骤的token分配指数级更高的惩罚，在不干扰正确推理路径的前提下破解错误级联问题。
### 关键结果
跨3个多模态大模型backbone测试，MRPO效果始终优于标准GRPO及现有RL基线；基于Qwen3-VL-8B-Instruct的实现效果超过34B参数的HuatuoGPT-Vision 2.79个点；将早期推理失败率从64.0%降至13.0%，同时提升推理质量与最终答案准确率。

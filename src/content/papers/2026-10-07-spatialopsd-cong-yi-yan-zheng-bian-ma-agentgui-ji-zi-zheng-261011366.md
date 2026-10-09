---
title: 'SpatialOPSD: Self-Distilling Spatial Intelligence from Verified Coding Agent
  Traces'
title_zh: SpatialOPSD：从已验证编码Agent轨迹自蒸馏空间智能的框架
authors:
- Rongxue Li
- Meng Yang
- Yiru Mao
- Yongliang Tao
- Lulu Hu
- Bin Yang
- Zhao Xu
- Weihua Luo
- Bowen Xu
affiliations:
- Alibaba Group
arxiv_id: '2610.11366'
url: https://arxiv.org/abs/2610.11366
pdf_url: https://arxiv.org/pdf/2610.11366
published: '2026-10-07'
collected: '2026-10-09'
category: Agent
direction: Agent能力蒸馏 · 空间推理能力内化
tags:
- Self-Distillation
- Spatial Reasoning
- MLLM
- Agent Trace
- On-Policy Training
one_liner: 通过on-policy自蒸馏将工具增强的空间推理能力内化到MLLM，推理时无需调用外部工具
practical_value: '- 落地工具增强Agent时可复用该蒸馏范式：将业务场景下Agent调用工具生成的已验证执行轨迹作为特权信息做OPSD蒸馏，无需人工标注即可将工具能力内化到小模型，解决推理时调用工具延迟高、无法支撑高吞吐推荐/广告请求的问题

  - 蒸馏阶段可直接复用Repetition-Aware Distillation trick：通过n-gram匹配检测学生对特权信息的直接拷贝与自我重复片段，对这些片段屏蔽蒸馏监督同时施加unlikelihood惩罚，可大幅降低特权信息泄露，避免推理时模型幻觉不存在的工具输出

  - 特权信息构造优先选择摘要形式：而非全量原始轨迹，可平衡师生模型的熵差，既保证知识转移效果，又降低蒸馏难度，适合多模态电商推荐场景下将复杂3D工具、空间计算工具的能力迁移到端侧/轻量部署模型'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
带外部工具的空间编码Agent虽能大幅提升MLLM的空间推理准确率，但推理时需循环调用代码执行、几何计算等外部工具，延迟高、依赖复杂基础设施，无法适配高吞吐的业务场景；而SFT、GRPO等常规训练方法要么缺少中间推理步骤监督导致准确率低、泛化性差，要么训练效率低、冷启动成本高。
### 方法关键点
- 先部署空间编码Agent跑通所有训练样本，仅保留最终结果与真值匹配的已验证轨迹作为训练语料，全程无需人工标注
- 采用on-policy自蒸馏（OPSD）框架：将轨迹摘要作为特权信息输入给冻结的教师模型，学生模型仅能访问原始输入，将教师的空间推理能力蒸馏到学生
- 提出重复感知蒸馏策略：用4-gram匹配检测学生输出中直接拷贝特权信息、自我重复的片段，对这些片段屏蔽蒸馏监督，同时施加unlikelihood惩罚，避免特权信息泄露
### 关键结果
在MindCube、ViewSpatial空间推理基准上，基于Qwen3.5-9B的SpatialOPSD平均准确率达51.9%，比SFT高4.3个百分点，比GRPO高3.7个百分点，达到工具版Agent 91%的性能，推理时完全无工具依赖；OOD场景下平均准确率达64.7%，优于SFT、GRPO基线，泛化性优异；该方法在2B、4B、27B参数尺度下均有2.2~3.8个百分点的稳定提升，适配不同编码Agent生成的轨迹。
### 核心结论
将工具增强Agent的已验证执行轨迹作为特权信息做自蒸馏，是低成本将Agent能力内化到standalone模型、兼顾推理性能与部署效率的可行路径。

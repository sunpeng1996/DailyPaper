---
title: 'TinyAstral: Transferring Self-Evolving Harnesses to Tiny Generalist Manipulation
  Agents'
title_zh: TinyAstral：将自进化Harness迁移到小型通用操控Agent
authors:
- Kehong Gong
- Xiaoxu Zheng
- Guanli Hou
- Seunghun Lee
- Mengqi Guo
- Runjia Tan
- Zhengyu Wen
- Qi Wang
- Xiaoyu He
- Mingyuan Zhang
affiliations:
- Huawei Technologies Co., Ltd
- Huawei Noah Research Institute
- Independent Researcher
arxiv_id: '2610.41216'
url: https://arxiv.org/abs/2610.41216
pdf_url: https://arxiv.org/pdf/2610.41216
published: '2026-10-29'
collected: '2026-11-03'
category: Agent
direction: Agent · Harness自进化与小模型蒸馏
tags:
- Agent
- Harness Evolution
- Distillation
- RSI
- Tiny LLM
- Embodied Agent
one_liner: 先迭代大模型Agent的Harness再蒸馏为小模型，大幅降低推理成本同时性能接近大模型
practical_value: '- 可复用「先优化大模型Agent周边Harness（工具链、反馈逻辑、错误恢复规则）再蒸馏小模型」的两步pipeline，比直接调优小模型性价比更高，适合推理成本敏感的业务场景如端侧Agent、实时推荐响应模块

  - 蒸馏时保留大模型的推理链作为监督信号，能显著提升小模型任务成功率，该trick可直接迁移到电商客服Agent、导购Agent的小模型训练

  - 蒸馏训练时加入故障注入的分支样本，可提升小模型容错能力，适合搜索推荐bad case修复、复杂query多轮交互场景的模型训练

  - Harness迭代时用严格配对A/B测试控制回退，可复用在业务Agent的prompt、工具链灰度迭代流程，避免迭代导致的效果波动'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
大模型Agent的性能不仅依赖模型本身，周边Harness（工具、反馈、记忆、错误恢复逻辑）的贡献同样关键，但大模型推理成本过高无法落地，现有Harness优化和小模型蒸馏两条路线相互独立，无法将Harness的优化收益迁移到小模型，亟需兼顾效果和成本的落地方案。

### 方法关键点
- 阶段1（Harness进化）：冻结大模型权重，通过递归自进化（RSI）迭代Harness：用前沿LLM分析大模型执行轨迹的失败原因，提出Harness修改方案，仅通过配对A/B测试验证有明确提升的修改才会被采纳，全程不改动大模型权重
- 阶段2（蒸馏迁移）：冻结最终优化后的Harness，采集大模型的完整执行轨迹（含推理链、工具调用、故障恢复过程），加入故障注入的分支样本、真实场景离线监督数据，SFT训练0.8B-4B的小模型，部署时小模型直接替换大模型接入相同Harness

### 关键实验
在RoboTwin等3个训练基准、3个零样本测试基准上验证：Harness迭代让180B大模型的RoboTwin任务成功率从33.4%提升到63.6%；蒸馏得到的4B小模型成功率达62.8%，仅比大模型低0.8pp，推理加速器耗时仅为大模型的1/5，零样本场景下性能接近552B大模型；消融实验显示移除推理链监督会让LIBERO-PRO任务成功率下降19.3pp。

### 核心结论
Agent的性能不仅来自模型权重，周边Harness的优化收益可以通过蒸馏完整迁移到小模型，是兼顾效果和推理成本的可行路径。

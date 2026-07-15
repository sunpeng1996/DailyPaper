---
title: Tracing Agentic Failure from the Flow of Success
title_zh: 基于成功轨迹的智能体系统失败步骤归因方法研究
authors:
- Samuel Yeh
- Yiwen Zhu
- Shaleen Deep
- Sharon Li
arxiv_id: '2607.12747'
url: https://arxiv.org/abs/2607.12747
pdf_url: https://arxiv.org/pdf/2607.12747
published: '2026-07-14'
collected: '2026-07-15'
category: Agent
direction: Agent 故障诊断与失败归因
tags:
- Agent
- Failure Attribution
- One-class Learning
- Neural CDE
- Unsupervised Learning
one_liner: 提出仅用成功轨迹训练的无监督智能体失败归因模型OAT，效率精度均优于prompt基线
practical_value: '- 电商导购Agent、搜索推荐链路的Agent故障排查可复用仅用成功轨迹训练的思路，无需昂贵的失败步骤标注，大幅降低训练数据成本

  - 可将神经受控微分方程建模正常轨迹动态的思路迁移到推荐系统异常检测（如刷单、异常流量识别）场景，仅用正常样本训练即可落地

  - 线上Agent服务的实时故障归因可直接参考OAT的低延迟设计，相比prompt类方法降本提效效果显著，适合工业级规模化部署'
score: 8
source: arxiv-cs.CL
depth: abstract
---

### 动机
基于LLM的Agent系统失败步骤归因是系统调试、性能优化的核心需求，现有方案存在两大痛点：prompt类归因pipeline计算成本极高，有监督归因方法依赖成本高昂的步骤级失败标注，难以规模化落地。
### 方法关键点
提出无监督归因框架OAT，将失败归因转化为单类学习任务：仅使用成功轨迹训练，通过神经受控微分方程在隐空间建模成功轨迹的动态演化模式；推理时计算失败轨迹每一步与学习到的正常动态的偏差，输出异常分识别错误步骤，全程无需失败标注数据参与训练。
### 关键结果
仅用100条成功轨迹训练即可达到SOTA效果：1. 推理速度比prompt类基线快200~5000倍；2. 域内数据集F1相对提升20%，分布外数据集F1相对提升7%

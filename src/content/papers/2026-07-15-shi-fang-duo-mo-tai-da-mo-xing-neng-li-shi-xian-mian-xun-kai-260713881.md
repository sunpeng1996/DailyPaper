---
title: Unleashing Multimodal Large Language Models for Training-free HOI Detection
  in the Wild
title_zh: 释放多模态大模型能力实现免训练开放域人物交互检测
authors:
- Ting Lei
- Jialin Liu
- Zhu Xu
- Yuxin Peng
- Yang Liu
affiliations:
- Wangxuan Institute of Computer Technology, Peking University
arxiv_id: '2607.13881'
url: https://arxiv.org/abs/2607.13881
pdf_url: https://arxiv.org/pdf/2607.13881
published: '2026-07-15'
collected: '2026-07-17'
category: Other
direction: 多模态大模型 · 免训练开放域HOI检测
tags:
- MLLM
- Training-Free
- HOI Detection
- Open-world
- Agent Framework
one_liner: 提出免训练AgentHOI框架，调度多视觉基础模块实现开放域HOI检测，性能优于现有监督方法
practical_value: '- 电商场景下免训练识别用户与商品交互行为（如试用、拿起、摆放）的方案可直接复用，无需标注HOI交互数据，降低冷启动成本

  - 上下文感知多轮推理+多维度特征融合定位的机制可迁移到多模态搜索的商品定位、交互意图理解模块，提升模糊场景识别准确率

  - 模块化调度多个视觉基础模型的Agent架构可借鉴到多模态内容理解链路，无需端到端重训即可快速适配新场景'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
传统人物交互检测（HOID）依赖预定义交互类别与数据集标注，泛化性差，无法适配开放域组合场景；现有基于MLLM的prompt方法仅提取判别性表征，未充分利用模型固有多模态推理能力，模糊场景下交互理解效果差。
### 方法关键点
- 提出免训练AgentHOI框架，模块化调度互补的视觉基础模块，协同完成开放式语义推理与空间定位
- 设计上下文感知多轮推理机制，逐步优化交互假设，实现全面的组合式HOI发现
- 设计多维度交互定位机制，融合语义、空间、外观特征生成实例专属描述，提升定位精度
### 关键结果
无需任何HOID训练数据，真实场景下性能优于SOTA监督、弱监督HOI检测方法

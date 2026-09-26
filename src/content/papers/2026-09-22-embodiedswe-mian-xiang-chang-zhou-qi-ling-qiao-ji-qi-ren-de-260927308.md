---
title: 'EmbodiedSWE: Coding Agents for Long Horizon Dexterous Robotics'
title_zh: 《EmbodiedSWE：面向长周期灵巧机器人的编码智能体》
authors:
- Haoxiang You
- Zeyu Shen
- Yilang Liu
- Zhicheng Zheng
- Lihan Zha
- Kashu Yamazaki
- Mingtong Zhang
- Suning Huang
- Jiankai Sun
- Qianzhong Chen
affiliations:
- ByteDance Seed
- Yale University
- Princeton University
- Carnegie Mellon University
- Stanford University
arxiv_id: '2609.27308'
url: https://arxiv.org/abs/2609.27308
pdf_url: https://arxiv.org/pdf/2609.27308
published: '2026-09-22'
collected: '2026-09-26'
category: Agent
direction: 具身智能 · 编码Agent数据生成
tags:
- CodingAgent
- EmbodiedAI
- DataGeneration
- VLA
- LongHorizonTask
one_liner: 提出EmbodiedSWE框架，用编码Agent生成可扩展监督数据训练机器人VLA模型
practical_value: '- 单Agent生成的解决方案可通过多样化扩增生成大量训练轨迹，可迁移到推荐系统冷启动时用Agent生成用户/物品交互样本扩充训练集

  - 针对长序列任务的Agent辅助工具设计思路，可复用在电商全链路运营Agent的工具链搭建中，降低长任务迭代交互成本

  - 单实例解决方案泛化到不同任务变体的扩增思路，可迁移到生成式推荐的prompt多样化，提升LLM4Rec的跨场景泛化能力'
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
长周期灵巧机器人任务缺乏大量可泛化的训练标注，现有单任务编码Agent解决方案泛化性差、迭代成本高，无法支撑通用机器人策略训练。

### 方法关键点
1. 构建EMBODIEDSWE-BENCH模拟基准，覆盖接触式操控、可变形物体处理等最长达30分钟的长周期任务；
2. 设计配套辅助工具提升编码Agent长任务解决效率；
3. 提出EMBODIEDSWE-GEN框架，将编码Agent的单任务解决方案扩增为多样化轨迹数据集，用于训练VLA模型。

### 关键结果
仅用Agent生成的模拟演示微调的VLA可完成真实机器人长周期任务，Agent辅助的样本多样化使VLA对未见过的任务变体泛化性显著提升，且性能随生成演示数量增加单调上涨。

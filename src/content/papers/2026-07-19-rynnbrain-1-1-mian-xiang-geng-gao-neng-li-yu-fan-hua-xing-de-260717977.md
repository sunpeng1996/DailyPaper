---
title: 'RynnBrain 1.1: Towards More Capable and Generalizable Embodied Foundation
  Model'
title_zh: RynnBrain 1.1：面向更高能力与泛化性的具身基础模型
authors:
- Kehan Li
- Bohan Hou
- Minghao Zhu
- Tianyi Zhang
- Zesen Cheng
- Zhikai Wang
- Sicong Leng
- Xin Li
- Xiao Lin
- Biying Yao
affiliations:
- DAMO Academy, Alibaba Group
- Hupan Lab
arxiv_id: '2607.17977'
url: https://arxiv.org/abs/2607.17977
pdf_url: https://arxiv.org/pdf/2607.17977
published: '2026-07-19'
collected: '2026-07-22'
category: Agent
direction: 具身Agent · 多尺度跨实体泛化优化
tags:
- Embodied AI
- Foundation Model
- VLA
- 3D Grounding
- Multi-embodiment
one_liner: 达摩院推出多尺度具身基础模型家族，新增3D grounding等能力，在多基准及真实机器人实验表现SOTA
practical_value: '- 跨实体统一表征+实体专属掩码的设计思路，可迁移到多场景（搜索/推荐/广告）统一大模型训练，适配不同业务域的差异化需求

  - 多任务多实体联合训练相比单任务训练涨点的结论，可复用在电商多场景（召回/排序/文案生成）联合建模的方案设计中

  - 小模型原生支持3D grounding的优化思路，可参考优化端侧/低算力场景下的多模态推荐/导购Agent推理性能'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有具身基础模型跨实体泛化性弱、小模型3D感知能力不足，输出与真实操控对齐度差，难以适配多形态硬件落地需求。
### 方法关键点
1. 发布2B/9B/122B-A10B三尺度模型家族，基于统一时空物理grounding框架训练；
2. 全系列新增接触点预测能力，2B/9B模型原生支持3D grounding，输出更适配机器人操控；
3. 推出RynnBrain-VLA，采用统一跨实体动作空间+实体专属掩码，支持多形态机器人部署。
### 关键结果
- 122B-A10B模型在VSI-Bench、MMSI、RefSpatial-Bench上超越所有参评闭源/开源模型；
- 真实机器人实验中，RynnBrain初始化策略优于Qwen系及主流通用VLA；
- 多任务多实体联合训练相比单任务训练，流程得分与成功率均有显著提升。

---
title: On-Policy Distillation for Vision-Language Model Adaptation, an Effective Paradigm
  on Low-Quality Multimodal Data
title_zh: 面向低质多模态数据的视觉语言模型同策略蒸馏适配范式
authors:
- Hongyuan Zhang
- Xianda Guo
- Yanlun Peng
- Qianlong Yang
- Yubin Guo
- Pinhan Fu
- Mulin Chen
- Xiaozhen Qiao
- Ping Luo
affiliations:
- The University of Hong Kong
- Great Wall Motor
- Wuhan University
- China University of Petroleum (East China)
- University of Science and Technology of China
arxiv_id: '2609.10321'
url: https://arxiv.org/abs/2609.10321
pdf_url: https://arxiv.org/pdf/2609.10321
published: '2026-09-09'
collected: '2026-09-10'
category: Training
direction: 多模态大模型 · 知识蒸馏优化
tags:
- Knowledge Distillation
- Vision-Language Model
- On-Policy Learning
- Multimodal Adaptation
- Low-Quality Data
one_liner: 提出OnPoKD同策略蒸馏框架，动态自适应构建VLM蒸馏目标，适配低质多模态数据场景
practical_value: '- 做多模态商品图文表征蒸馏时，可复用OnPoKD动态目标构造逻辑，替代固定教师预测范式，适配低质用户上传图文等脏数据场景

  - 蒸馏训练时可加入轻量策略控制器，用验证集反馈更新控制逻辑，平衡三类信号权重，无需改动推理架构不增加上线成本

  - 跨域迁移/新类泛化的多模态蒸馏场景，可复用样本级自适应目标构造思路，提升分布偏移下的蒸馏效果'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有VLM知识蒸馏采用固定教师预测作为统一训练目标，在类别偏移、域偏移的低质多模态数据场景下性能不稳定
### 方法关键点
1. 提出OnPoKD on-policy蒸馏框架，将蒸馏目标构造建模为动态策略决策，是首个将同策略蒸馏应用到VLM适配的方案
2. 训练轻量控制器，结合教师、学生模型输出与零样本先验的置信度、分歧信号，逐样本自适应构造蒸馏目标
3. 控制器基于验证集反馈更新，动态平衡教师监督、零样本先验引导、硬标签锚定三类信号权重，适配不同样本可靠性与训练阶段，且仅训练阶段使用，不增加推理成本
### 关键结果
在基类到新类泛化、跨数据集迁移两类基准上，相对现有强VLM蒸馏基线均取得一致性能提升

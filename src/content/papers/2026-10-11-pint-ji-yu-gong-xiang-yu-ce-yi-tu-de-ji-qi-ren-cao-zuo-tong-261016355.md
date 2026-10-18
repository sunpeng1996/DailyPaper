---
title: 'PINT: A Unified Model with Shared Predictive Intent for Robot Manipulation'
title_zh: PINT：基于共享预测意图的机器人操作统一模型
authors:
- Xinyu Guo
- Chao Jing
- Li Yi
- Xingyu Chen
- Zhengxing Wu
affiliations:
- Institute of Automation, Chinese Academy of Sciences
- University of Chinese Academy of Sciences
- Zhongguancun Academy
- Fudan University
- Tsinghua University
arxiv_id: '2610.16355'
url: https://arxiv.org/abs/2610.16355
pdf_url: https://arxiv.org/pdf/2610.16355
published: '2026-10-11'
collected: '2026-10-18'
category: Other
direction: 多模态统一建模 · 机器人操作
tags:
- VLM
- Video Generation Model
- Intent Token
- OOD Generalization
- Unified Model
one_liner: 通过共享块级预测意图协调多专家模块，无需具身预训练即可提升机器人操作OOD泛化能力
practical_value: '- 多专家模块融合可借鉴「共享可学习Token作为跨模块接口」的设计，不需要修改预训练模型内部注意力逻辑、保留各模块专业能力，可迁移到LLM+推荐场景下召回、排序、生成模块的协同架构

  - 两阶段训练策略可复用：第一阶段冻住下游生成类模块，先让中间意图表示对齐核心任务目标，第二阶段冻住中间表示微调下游模块，可降低多任务/跨域微调时预训练能力被冲刷的风险

  - 中间意图表示无需人工定义编码规则，通过多模块原生预测目标联合学习即可自动对齐，可省去多模态推荐/Agent场景下人工做跨模块语义对齐的规则开发成本'
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
通用机器人操作需结合VLM的语义推理能力与VGM的世界建模能力，但现有统一模型直接通过多层共享注意力融合两类模块，会削弱各模块的专属专业能力。
### 方法关键点
1. 设计块级共享Predictive Intent作为跨专家接口，在VLM序列插入可学习Intent Token，同时作为VGM和动作专家（AE）的输入条件，仅替换VGM的prompt conditioning，保留各模块独立通路；
2. 两阶段训练：阶段1冻住VGM，让Predictive Intent先对齐任务未来动态；阶段2冻住已学习的Intent，微调VGM和AE；
3. Predictive Intent无需人工定义编码规则，通过VLM、VGM、AE的原生预测目标联合学习自动对齐。
### 关键结果
无需具身预训练，RoboTwin 2.0-Hard OOD准确率达15.5%，是对比方法的3.8~7.6倍；LIBERO-Plus OOD准确率79.5%，较基线高4.5~28pct；真实世界双手操作任务ID成功率68%、OOD成功率24%，优于同设置基线。

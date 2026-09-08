---
title: Towards Neuro-Symbolic Procedural Reasoning for Long-Horizon Vision-Language-Action
  Manipulation
title_zh: 面向长序列视觉-语言-动作操控的神经符号过程推理
authors:
- Vivek Chavan
- Yahuan Shi
- Oliver Heimann
- Kevin Haninger
- Jörg Krüger
affiliations:
- Fraunhofer IPK, Berlin, Germany
- Technische Universität Berlin, Berlin, Germany
arxiv_id: '2609.05369'
url: https://arxiv.org/abs/2609.05369
pdf_url: https://arxiv.org/pdf/2609.05369
published: '2026-09-04'
collected: '2026-09-08'
category: Reasoning
direction: 长序列VLA任务·神经符号过程推理
tags:
- Neuro-Symbolic
- VLA
- Task-Graph
- Procedural-Reasoning
- Long-Horizon
- Multimodal-Memory
one_liner: 提出结合任务图、多模态记忆与注视引导的神经符号框架，提升长序列VLA操控鲁棒性
practical_value: '- 长序列多步骤Agent任务可复用「显式任务图+状态记忆」架构，将依赖逻辑、跳转条件与大模型推理解耦，降低长流程出错率

  - 人工演示的显著性/注视信号可作为弱监督信号加入多模态模型微调，提升目标选择、场景接地的准确率，降低标注成本

  - 可迁移「子目标分发+状态转移校验」机制，用于电商运营Agent、多轮客服任务的流程管控，避免逻辑跳步'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
VLA模型仅能稳定执行短程操控任务，在需持久任务状态、依赖感知推理、条件决策、可靠接地的长序列场景下表现脆弱，错误率高。
### 方法关键点
1. 搭建神经符号融合框架，将可学习VLA控制与显式任务图、多模态过程记忆结合：任务图编码动作依赖、有效转移路径与分支条件，记忆维护当前激活步骤、已完成动作、文本上下文与任务相关视觉证据，二者共同引导目标选择、目的地接地、子目标分发与预期状态转移校验
2. 引入人类演示的注视/显著性伪标注信号，在VLA微调与推理阶段提供时空引导，无需跨视角注视迁移
### 关键结果
在工作空间清理、手术器械处理两个长序列操控任务验证，结构化符号推理与演示视觉引导可协同提升目标选择准确率、子任务完成率、步骤顺序一致性与全任务成功率，显著降低流程类与执行类错误。

---
title: 'SeededGrasp: Language-Guided Grasping in Complex Scenes with Multiple Embodiments'
title_zh: SeededGrasp：复杂场景下多形态设备的语言引导抓取框架
authors:
- Yang Xu
- Gurpreet Singh Mukker
- Raymond Wang
- Jasper Gerigk
- Maria Attarian
- Igor Gilitschenski
affiliations:
- University of Toronto
- Vector Institute
- University of British Columbia
- Google Deepmind
arxiv_id: '2607.20207'
url: https://arxiv.org/abs/2607.20207
pdf_url: https://arxiv.org/pdf/2607.20207
published: '2026-07-21'
collected: '2026-07-25'
category: Other
direction: 多模态机器人 · 语言引导多设备抓取
tags:
- VLM
- Multi-embodiment
- Robotic Grasping
- Vision-Language
- Dataset
one_liner: 提出语义与几何执行解耦的高效语言引导抓取框架，开源2.5M规模多形态抓取数据集
practical_value: '- 可借鉴「高层语义推理+底层轻量执行」的解耦架构，例如LLM完成用户意图理解后输出控制信号给推荐排序模块，避免端到端训练的高成本

  - 多主体适配思路可迁移至多Agent推荐场景，统一语义层输出适配不同业务端（电商/广告/搜索）的执行逻辑

  - 数据高效训练思路可复用：用大模型输出种子信号作为下游小模型的条件输入，大幅降低下游任务标注需求'
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
复杂场景下机器人抓取需同时兼顾3D空间推理与任务语义对齐，现有VLM引导的抓取方案要么空间感知能力不足，要么端到端训练成本极高，难以扩展至多形态设备场景。
### 方法关键点
1. 采用高层语义推理与底层几何执行解耦设计：VLM仅输出抓取种子点作为条件，喂给后续轻量级抓取生成模型执行，无需端到端联合训练，数据效率高且天然支持多形态设备
2. 开源首个多形态桌面抓取数据集，覆盖杂乱场景下超2.5M条抓取样本
### 关键结果数字
仿真环境抓取成功率达72%，真实世界场景抓取成功率达78%，性能优于所有现有基线方案

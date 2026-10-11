---
title: 'ARC: A Reasoning Recipe for Robot Foundation Models'
title_zh: ARC：面向机器人基础模型的推理优化方案
authors:
- Gokul Puthumanaillam
- Tao Sun
- Elie Aljalbout
- Moritz Reuss
- Zhaoshuo Li
- Fabio Ramos
- Ankit Goyal
- Jenai Xuning Yang
affiliations:
- University of Illinois Urbana-Champaign
- Stanford University
- NVIDIA
- University of Sydney
- Proception
arxiv_id: '2610.12386'
url: https://arxiv.org/abs/2610.12386
pdf_url: https://arxiv.org/pdf/2610.12386
published: '2026-10-08'
collected: '2026-10-11'
category: Reasoning
direction: 机器人基础模型 · 推理性能优化
tags:
- Reasoning Trace
- Robot Foundation Model
- Zero-shot Learning
- Automatic Labeling
- Fine-tuning
one_liner: 无需新增数据或大规模训练，通过三步推理方案大幅提升机器人基础模型零样本任务表现
practical_value: '- 面向电商/广告/推荐场景的Agent决策任务，可复用「基于历史行为自动生成因果推理轨迹」的思路，无需新增标注成本即可提升Agent零样本泛化能力

  - 做下游模型适配时，可参考「针对不同架构定制微调+推理流程」的策略，避免全量重训的高昂成本

  - 优化语义理解/推荐决策类任务时，可借鉴推理轨迹需锚定最终决策/动作的设计，减少推理过程与落地目标的偏离'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有机器人基础模型（RFM）性能提升依赖更大模型参数、更多人工标注演示数据、大规模全量训练，算力与标注成本极高，亟需低成本的替代优化路径。
### 方法关键点
提出ARC推理优化框架，核心包含三个模块：1）设计锚定机器人下一个执行动作的因果推理轨迹，明确动作的合理性逻辑与预期执行效果；2）搭建可扩展的自动标注pipeline，直接从已有历史演示数据生成推理轨迹，无需新增任何数据采集成本；3）针对不同架构的预训练RFM（如VLA、WAM）定制专属微调与推理策略，使其能基于推理轨迹输出更准确的控制决策。
### 关键结果
无需新增演示数据或基础模型级大规模训练，RoboLab-Reasoning-50基准上性能最高提升50pp，真实机器人场景下π0.5模型任务成功率提升82.2pp，同时在RoboLab-120、MolmoSpaces基准上达到SOTA

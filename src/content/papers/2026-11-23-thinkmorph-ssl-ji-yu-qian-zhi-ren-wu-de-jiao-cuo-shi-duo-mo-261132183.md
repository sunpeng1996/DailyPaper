---
title: 'ThinkMorph-SSL: Scaling Interleaved Multimodal Reasoning with Pretext Tasks'
title_zh: ThinkMorph-SSL：基于前置任务的交错式多模态推理规模化训练
authors:
- Jiawei Gu
- Linjie Li
- Yiming Liu
- Yunzhuo Hao
- Huichen Wang
- Guanzheng Chen
- Zhichao Peng
- Luxin Xu
- Xinyu Zhang
- Li Luo
affiliations:
- University of Washington
- Tsinghua University
- Zhejiang University
- National University of Singapore
- Stanford University
arxiv_id: '2611.32183'
url: https://arxiv.org/abs/2611.32183
pdf_url: https://arxiv.org/pdf/2611.32183
published: '2026-11-23'
collected: '2026-11-25'
category: Multimodal
direction: 多模态推理 · 自监督训练范式
tags:
- Multimodal Reasoning
- Self-Supervised Learning
- Pretext Task
- Instruction Tuning
- Multimodal LLM
one_liner: 提出两阶段自监督训练框架，无需额外人工标注即可提升交错式多模态推理能力
practical_value: '- 电商多模态Agent（商品图文理解、营销素材生成）场景可复用两阶段训练范式，基于海量无标注商品图文数据做前置任务预训练，大幅降低标注成本

  - 可将图像去噪、风格迁移等视觉前置任务改造为交错推理轨迹，增强多模态大模型图文联合推理能力，适配商品质检、AI设计等业务需求

  - 指令微调标注预算有限时，先开展前置推理预训练可显著提升微调效率，效果优于纯指令微调方案'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
交错式多模态推理可生成中间图像引导后续推理，是多模态大模型的核心能力之一，但传统训练方法依赖难以采集的任务特定标注示范，成本极高。
### 方法关键点
提出两阶段自监督训练方案ThinkMorph-SSL：
1. 前置推理阶段：将图像上色、去噪等视觉前置任务转换为无指令交错轨迹，要求模型依次完成受损图像描述、修复图像生成、结果解读三步；
2. 指令微调阶段：基于自动构造的示范开展问题驱动的指令微调。
### 关键结果
相同指令微调预算下，模型效果优于纯指令微调训练的模型；全训练流程在12个基准数据集上平均精度较基础模型提升11.33个百分点。

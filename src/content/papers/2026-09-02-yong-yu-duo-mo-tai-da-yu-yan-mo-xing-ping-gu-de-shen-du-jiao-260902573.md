---
title: Deeply Interleaved Text-Image Contexts for Multimodal LLMs Assessment
title_zh: 用于多模态大语言模型评估的深度交错图文上下文基准TIC-Bench
authors:
- Zihao Wang
- Xi Xiang
- Yuwen Sun
- Yingyu Li
- Yabo Zhang
- Yihan Zeng
- Fan Li
- Wangmeng Zuo
affiliations:
- Harbin Institute of Technology
- Huawei Noah's Ark Lab
arxiv_id: '2609.02573'
url: https://arxiv.org/abs/2609.02573
pdf_url: https://arxiv.org/pdf/2609.02573
published: '2026-09-02'
collected: '2026-09-04'
category: Eval
direction: 多模态大模型评估 · 交错图文场景
tags:
- MLLM
- Benchmark
- Multimodal Understanding
- Text-Image Interleaving
- Evaluation
one_liner: 提出覆盖逻辑时空关联的TIC-Bench基准，评测多模态大模型对深度交错图文上下文的理解能力
practical_value: '- 电商多模态商品理解、直播文案+画面联动理解场景的模型验证，可直接复用TIC-Bench的逻辑/时空关联评测维度设计自定义用例，降低测试集构建成本

  - 开发多模态导购Agent时，可参考该基准的任务划分方式，针对性优化图文交错输入下的线索整合能力，减少跨模态信息遗漏导致的回答错误

  - 训练多模态商品内容生成模型时，可引入TIC-Bench的校验逻辑，对生成结果的图文语义一致性做自动化质检，提升内容审核效率'
score: 7
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有多模态大模型的评估与训练多聚焦多图任务，文本仅作为任务指令，未与视觉内容产生深度语义交互，无法匹配图文共创、多模态内容理解等真实场景对跨模态信息融合的需求。
### 方法关键点
推出TIC-Bench基准，覆盖逻辑关联、时序关联、空间关联三大核心领域，细分8类子任务，共包含2280道评测题，可量化模型在深度交错图文上下文内整合跨模态线索、还原事实的能力。
### 关键结果
对10个SOTA MLLM的评测显示，现有模型性能与人类专家存在显著差距，普遍存在分散式交错图文输入下的证据整合困难问题。

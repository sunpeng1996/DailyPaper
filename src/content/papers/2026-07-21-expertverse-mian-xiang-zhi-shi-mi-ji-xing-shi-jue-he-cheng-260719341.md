---
title: 'ExpertVerse: A General-Purpose Benchmark for Expert-Level Reasoning in Knowledge-Intensive
  Visual Synthesis'
title_zh: ExpertVerse：面向知识密集型视觉合成的专家级推理通用基准
authors:
- Yuan Wang
- Yongchao Du
- Mengting Chen
- Jinsong Lan
- Xuetao Feng
- Xiaoyong Zhu
affiliations:
- Alibaba Group
- Tsinghua University
arxiv_id: '2607.19341'
url: https://arxiv.org/abs/2607.19341
pdf_url: https://arxiv.org/pdf/2607.19341
published: '2026-07-21'
collected: '2026-07-23'
category: Multimodal
direction: 多模态生成 · 评测与推理优化
tags:
- Multimodal Generation
- Benchmark
- VLM
- RL Fine-tuning
- Pareto Optimization
- Knowledge Reasoning
one_liner: 构建知识密集型视觉生成评测基准，提出多奖励适配的帕累托策略优化方法训练VLM推理引擎
practical_value: '- 多奖励优化遇到梯度冲突、跨模态奖励不匹配时，可复用BPPO的BRR奖励矫正和CPAF优势融合策略，适配生成式广告、虚拟试穿等电商多模态生成场景的RL调优

  - 构建垂直领域多模态生成能力评测集时，可参考9类认知能力+8类专家领域的正交分类框架，覆盖单图编辑、多图合成、文生图三类核心任务

  - 专业领域知识密集型多模态生成任务（如工业/医疗类商品种草图生成）可引入「先输出思考链再生成精细化指令」的范式，提升内容专业度'
score: 6
source: arxiv-cs.CV
depth: abstract
---

**动机**：现有多模态生成模型仅支持常识推理、浅层因果理解与直接知识召回，无法胜任知识密集型视觉生成任务，且缺乏针对性的能力评测基准。
**方法关键点**：1. 推出ExpertVerse评测基准，采用9类认知能力×8个专家领域的正交分类体系，覆盖58个子领域，包含1611条专家标注实例、100K条带推理轨迹的自动生成样本，覆盖文生图、单图编辑、多图合成三类任务；2. 训练KnowThinker VLM推理引擎，联合输出思考链与精细化生成指令；3. 针对多奖励优化中的跨模态奖励错位、梯度冲突问题，提出BPPO算法，融合BRR奖励矫正与CPAF帕累托优势融合模块。
**关键结果**：对开源及商用多模态模型的评测均暴露其存在显著的知识密集型推理缺陷，验证了该基准的实用价值，BPPO算法相较通用RL优化方法在知识驱动生成任务上表现大幅领先。

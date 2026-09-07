---
title: 'MuSP-Bench: Advanced Multimodal Benchmarking of Music Understanding across
  Score and Performance'
title_zh: MuSP-Bench：跨乐谱与演奏的多模态音乐理解评测基准
authors:
- Milan Liessens Dujardin
- Song-Ze Yu
- Kevin Miao
affiliations:
- Bryel Labs
- UC Berkeley
arxiv_id: '2608.28212'
url: https://arxiv.org/abs/2608.28212
pdf_url: https://arxiv.org/pdf/2608.28212
published: '2026-08-28'
collected: '2026-09-07'
category: Eval
direction: 多模态音乐理解评测基准构建
tags:
- Multimodal LLM
- Benchmark
- Music Understanding
- Cross-Modality
- Evaluation
one_liner: 推出含490道人工标注题的跨乐谱与演奏的多模态音乐理解评测基准MuSP-Bench
practical_value: '- 跨模态评测基准构建可参考「单模态内推理+跨模态关联+长序列推理」的分层任务设计范式，全面覆盖不同能力维度

  - 多模态模型能力评估可复用人工构造真实场景任务的思路，减少自动化生成任务带来的评估偏差

  - 若业务涉及音乐类内容推荐、音乐教育/UGC产品，可直接采用该基准测试多模态模型的音乐理解能力'
score: 4
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有音乐理解评测多单独评估乐谱、演奏音频单模态能力，任务集中在短序列、选择题型，无法覆盖真实音乐场景下跨模态关联、长时序推理、解释性分析等核心需求。
### 方法关键点
1. 构建490道人工编写的评测题，覆盖古典钢琴、管弦乐两大场景；
2. 任务划分为乐谱理解、演奏音频理解、跨模态关联推理、长时序推理4类，支持多输入条件测试；
3. 基准完全开源，访问地址为https://musp.vaclis.net/。
### 关键结果
当前前沿多模态大模型在乐谱理解任务上表现较差，在演奏音频推理任务上能力更弱，跨模态音乐理解存在较大技术缺口。

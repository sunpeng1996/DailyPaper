---
title: 'SemComp-Bench: Benchmarking Semantic Task Completion in Video Generation'
title_zh: SemComp-Bench：视频生成语义任务完成能力评测基准
authors:
- Keyu Tu
- Zhuowei Chen
- Mengqi Huang
- Yuxin Wang
- Jiahao Zhu
- Zhendong Mao
- Yongdong Zhang
affiliations:
- University of Science and Technology of China
- FrameX.AI
- Sun Yat-sen University
arxiv_id: '2608.17426'
url: https://arxiv.org/abs/2608.17426
pdf_url: https://arxiv.org/pdf/2608.17426
published: '2026-08-17'
collected: '2026-08-20'
category: Eval
direction: 多模态生成 · 视频生成能力评测
tags:
- Video Generation
- Benchmark
- VLM
- Semantic Grounding
- Evaluation Dataset
one_liner: 提出结果导向视频生成的语义任务完成评测数据集、协议与双维度量化指标
practical_value: '- 电商营销内容/商品生成视频的效果评测，可复用「结果达成度+任务相关语义对齐」的双维度评估逻辑，无需过度约束无关属性一致性

  - 多模态生成效果的自动化评测，可借鉴基于VLM回答结构化二元问题的方案，大幅降低人工评测成本

  - 垂直领域生成式任务评测数据集构建，可复用四阶段可扩展数据治理流水线，快速标准化原始素材'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有视频生成模型的视觉保真度、时序连贯性表现已较成熟，但指令遵循下的目标达成能力、与参考输入的任务相关高层语义对齐能力缺乏统一的系统性评测框架。
### 方法关键点
1. 定义结果导向的语义任务完成视频生成范式，核心要求为达成指令目标+保留任务相关的参考图高层语义，无需完整呈现中间步骤、无需对齐无关属性的外观一致性
2. 构建覆盖6个领域的SemComp-Data评测数据集，单实例包含参考图、粗细粒度指令、结果导向视频片段，配套可扩展的四阶段数据治理流水线
3. 推出SemComp-Bench评测协议，基于VLM回答结构化二元问题，输出结果达成OA Score、生成可靠性GR Score两个核心量化指标
### 关键结果
对主流视频生成模型的评测验证，现有模型同时兼顾指令目标达成、参考语义对齐的能力仍存在显著短板

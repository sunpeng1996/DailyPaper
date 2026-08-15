---
title: 'Edit2TikZ: A Comprehensive and Challenging Benchmark for Scientific Figure
  Editing with TikZ'
title_zh: Edit2TikZ：面向TikZ科研图表编辑的综合性高难度基准
authors:
- Zongyun Zhang
- Jiacheng Ruan
- Xian Gao
- Ruizhu Zhou
- Lingcheng Meng
- Lining Hu
- Ting Liu
- Yuzhuo Fu
affiliations:
- Shanghai Jiao Tong University
arxiv_id: '2608.13441'
url: https://arxiv.org/abs/2608.13441
pdf_url: https://arxiv.org/pdf/2608.13441
published: '2026-08-13'
collected: '2026-08-15'
category: Eval
direction: 多模态大模型 · 代码生成基准评估
tags:
- MLLM
- Benchmark
- Code Generation
- Curriculum Learning
- TikZ
one_liner: 推出含1548个样本的TikZ图表编辑基准，配套评估框架及小模型训练优化方案
practical_value: '- 电商商品海报/装修HTML代码生成场景，可复用先重建原始代码再执行编辑的课程学习范式，显著提升小模型生成代码的可执行率

  - 垂类生成任务的benchmark构建可参考真实+合成样本结合、分步标注的方案，兼顾覆盖真实需求和控制评估难度

  - 生成类任务评估可借鉴「需求完成度+无关内容保留度」的双维度框架，提升评估结果和人类体验的对齐度'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有MLLM在视觉理解、图形代码生成上已展现潜力，但指令驱动的可编译科研图表编辑任务缺乏系统评估基准，现有TikZ基准仅聚焦图表重建与生成，未覆盖编辑场景需求。
### 方法关键点
发布Edit2TikZ基准，包含1548个真实+合成的高质量样本，支持文本、视觉两类定位编辑请求，覆盖多步编辑场景并配套步级标注；构建对齐人类判断的双维度评估框架，同时推出混合训练集TikZEditMix，采用先重建再编辑的课程学习策略优化小模型表现。
### 关键结果
14款主流MLLM评测显示，闭源模型平均编译成功率仅75%，9B以下小模型在指令遵循、完整生成上表现更差；上述训练策略将Qwen3.5-4B的编译成功率从45.35%提升至83.40%，综合评估指标平均提升18.7分。

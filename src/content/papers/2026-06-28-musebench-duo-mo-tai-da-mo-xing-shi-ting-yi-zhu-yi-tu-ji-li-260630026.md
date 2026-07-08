---
title: 'MuseBench: Benchmarking Intent-Level Audiovisual Arts Understanding in MLLMs'
title_zh: MuseBench：多模态大模型视听艺术意图级理解评测基准
authors:
- Yuxuan Fan
- Gyusik Seo
- Jing Hao
- Jaemin Cho
- Mohit Bansal
- Jaehong Yoon
affiliations:
- NTU Singapore
- The University of Hong Kong
- Johns Hopkins University
- AI2
- UNC-Chapel Hill
arxiv_id: '2606.30026'
url: https://arxiv.org/abs/2606.30026
pdf_url: https://arxiv.org/pdf/2606.30026
published: '2026-06-28'
collected: '2026-07-08'
category: Eval
direction: 多模态大模型 · 艺术意图理解评测
tags:
- MLLM
- Multimodal
- Benchmark
- Art Understanding
- Reasoning
one_liner: 推出覆盖4类视听艺术的MuseBench基准，评测MLLM的创意意图推理能力
practical_value: '- 四阶段迭代式评测集构建pipeline（捷径过滤+对抗干扰项+专家校验）可直接复用在生成式推荐、多模态导购Agent的效果评测集建设中，提升评测数据质量

  - 单选+可变选项多选的混合题型设计，可借鉴到广告创意理解、商品卖点匹配等多模态任务的效果评估，更贴合真实业务的开放式判定场景

  - 评测发现的模型对非突出选项漏判、依赖表层感知而非深层语义的缺陷，可指导多模态商品理解模型的bad case挖掘与优化方向'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有MLLM评测多聚焦感知识别任务，缺失对视听艺术创作意图推理能力的评估维度，无法衡量模型的深层艺术语义理解水平。
### 方法关键点
从1万+带专业解说的视频论说文提炼4016道题目，覆盖电影、静态视觉、舞台表演、游戏4类视听艺术场景；采用单选+可变选项多选的混合题型适配艺术分析的开放式特性；通过四阶段迭代pipeline生成与校验题目，包含捷径过滤、对抗干扰项构造、专家验证环节。
### 关键结果数字
28个SOTA MLLM零-shot评测最高准确率仅48.29%，远低于人类专家的87.18%；模型在游戏艺术类目表现最差，多选任务易漏判非突出选项，瓶颈来自风格词汇储备与文化先验缺失而非时序定位能力。

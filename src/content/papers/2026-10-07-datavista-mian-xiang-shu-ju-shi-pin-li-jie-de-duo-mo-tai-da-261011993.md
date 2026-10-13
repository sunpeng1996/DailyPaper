---
title: 'DataVista: Diagnosing Multimodal LLMs on Data Video Understanding'
title_zh: DataVista：面向数据视频理解的多模态大模型诊断基准
authors:
- Yupeng Xie
- Zhenyang Wang
- Jiayi Zhu
- Yinghao Tang
- Zhouan Shen
- Yiyu Chen
- Yuyu Luo
affiliations:
- The Hong Kong University of Science and Technology (Guangzhou)
- Zhejiang University
arxiv_id: '2610.11993'
url: https://arxiv.org/abs/2610.11993
pdf_url: https://arxiv.org/pdf/2610.11993
published: '2026-10-07'
collected: '2026-10-13'
category: Eval
direction: 多模态大模型评测 · 数据视频理解
tags:
- MLLM
- Video Understanding
- Benchmark
- Multimodal Evaluation
- Data Visualization
one_liner: 构建首个数据视频理解基准DataVista，覆盖三级能力维度并完成19款主流MLLM性能测评
practical_value: '- 电商直播/短视频中带数据类营销内容的理解任务，可复用DataVista的三级能力拆解框架，分层落地降低实现复杂度

  - 优化多模态内容理解模块时，增帧、加字幕的优化策略对时序感知类任务收益明确，高阶叙事类任务需额外做专项微调

  - 搭建商分析类视频自动解析工具时，可先规避因果推理、叙事结构类高难度自动化任务，降低bad case发生率'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有MLLM评测基准仅覆盖普通视频或静态图表，缺乏针对融合数据可视化与叙事的真实数据视频的系统性评测方案，该类内容在新闻、商业分析等场景应用广泛。
### 方法关键点
构建首个数据视频理解基准DataVista，包含961条真实世界数据视频、6775道评测题，覆盖5个领域、10类细粒度题型，按能力递进分为数据感知、时序推理、叙事理解三级框架。
### 关键结果数字
19款主流MLLM中最优的Gemini-3.1-Pro整体准确率仅70.0%，远低于人类水平，因果推理、叙事结构类题型表现最差；增帧、加字幕仅对感知、时序推理任务收益明显，对叙事理解提升有限，同时定位到图表读值、证据判断等三类典型失效模式。

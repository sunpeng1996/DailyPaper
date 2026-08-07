---
title: 'GST-Bench: Can VLMs Develop Global Spatial Awareness from Video?'
title_zh: GST-Bench：视觉大模型能否从视频中习得全局空间感知能力
authors:
- Qifeng Zhang
- Kaixiang Huang
- Heng Dong
- Huang Fang
- Junting Chen
- Junjie Zhu
- Yonghang Chen
- Zhiyu Zhang
- Wei Li
affiliations:
- ByteDance Seed
- Zhejiang University
- National University of Singapore
arxiv_id: '2608.05747'
url: https://arxiv.org/abs/2608.05747
pdf_url: https://arxiv.org/pdf/2608.05747
published: '2026-08-05'
collected: '2026-08-07'
category: Eval
direction: 具身Agent · VLM空间感知评测
tags:
- VLM
- Embodied Agent
- Spatial Reasoning
- Video Understanding
- Benchmark
one_liner: 推出面向视频VLM全局时空感知的评测基准GST-Bench，暴露现有模型长时序全局空间建模的核心短板
practical_value: '- 做电商仓储/线下门店导购具身Agent的团队，可直接复用GST-Bench作为模型空间推理能力的评测基准，减少自研评测集的成本

  - 现有VLM长时序全局场景表征能力存在明显短板，开发室内导航/货品盘点类Agent时，需额外引入显式的空间地图构建模块，不可完全依赖VLM端到端推理

  - 做长视频/直播语义理解的业务，可借鉴基准中长时序观测拼接的评估思路，优化跨帧全局语义对齐的效果'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
具身Agent核心依赖空间智能，但现有空间感知评测仅聚焦单/少视角的局部感知能力，缺失长时序连续视频流下的全局空间感知评估维度，无法支撑具身Agent相关VLM的能力验证。

### 方法关键点
构建GST-Bench基准，包含6790分钟合成视频对应的人工验证VQA问题，要求模型完成两类核心任务：从输入未出现的新视角做空间推理、将第一人称观测映射到全局俯视图；配套推出局部空间感知子基准GST-Bench-Local用于能力归因，以及训练数据集GST-Train支撑后续算法优化。

### 关键结果
22款SOTA VLM评测显示，最强零样本模型得分仅42.68，远低于人类的79.08；能力归因实验证明，模型局部空间感知能力达标，但无法将长时序观测整合为全局一致的场景表征，是核心短板。

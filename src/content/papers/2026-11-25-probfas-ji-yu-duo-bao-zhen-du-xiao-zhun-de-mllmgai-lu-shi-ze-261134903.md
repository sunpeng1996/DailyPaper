---
title: 'ProbFaS: Probabilistic Video Frame Selection for MLLMs via Multi-Fidelity
  Calibration'
title_zh: ProbFaS：基于多保真度校准的MLLM概率视频帧选择方法
authors:
- Tianru Zhang
- Mayank Nautiyal
- Hugo Eidmann
- Prashant Singh
- Ekta Vats
affiliations:
- Uppsala University
- SciLifeLab
arxiv_id: '2611.34903'
url: https://arxiv.org/abs/2611.34903
pdf_url: https://arxiv.org/pdf/2611.34903
published: '2026-11-25'
collected: '2026-11-26'
category: Multimodal
direction: 多模态大模型 · 长视频帧选择优化
tags:
- MLLM
- Frame Selection
- Multi-fidelity Calibration
- Gaussian Process
- Video Understanding
one_liner: 提出无训练无标注的多保真校准概率帧选择方案，大幅降低长视频MLLM推理成本
practical_value: '- 电商短视频理解/种草内容分析场景可复用「低成本粗信号+高成本精信号」的多保真校准思路，用低开销CLIP类ITA得分做全量初筛，少量MLLM判断做校准，兼顾精度和成本

  - 长序列关键单元选择（如直播切片选品、用户行为序列采样）可复用时间行列式点过程的选点逻辑，同时覆盖峰值相关性和时间序列完整性

  - 无训练无标注的pipeline设计思路可直接落地增量业务场景，无需额外标注数据和模型训练成本，快速上线'
score: 7
source: arxiv-cs.CV
depth: abstract
---

### 动机
长视频输入MLLM推理成本极高，传统均匀采样易丢失关键帧；现有无训练方法依赖的ITA得分与MLLM实际需求相关性弱，40%以上query下甚至负相关，而MLLM本身的判断信号精度高但采样成本高。
### 方法关键点
ProbFaS是无训练无标注的概率帧选择pipeline，将密集ITA得分作为低成本有偏信号，稀疏MLLM yes/no判断作为高成本精确信号，通过co-kriging多保真高斯过程融合两类信号校准所有帧的相关性，再基于时间行列式点过程选择帧，同时覆盖相关性峰值和时间覆盖度。
### 关键结果
在Video-MME、MLVU、LongVideoBench的15个测试设置（8-128帧）中，13个精度领先14个SOTA无训练选择器和均匀采样，最高超最强基线3.1个百分点；32帧效果等价于基线128帧、均匀采样最多768帧的效果，推理成本降至原方案的1/4~1/24。

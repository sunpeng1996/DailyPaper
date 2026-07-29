---
title: 'FilmBench: A Film-Grade Benchmark for Cinematic Video Generation'
title_zh: FilmBench：面向电影级视频生成的专业评测基准
authors:
- Shengyi Wang
- Niantong Li
- Guangzheng Hu
- Hong Qi
- Fei Ding
- Weixu Qiao
- Jinlin Wang
- Xiaotong Lv
- Peng Han
- Zimeng Li
affiliations:
- Alibaba Group
- Moku Lab, Hujing Digital Media & Entertainment Group
- Beijing Film Academy
arxiv_id: '2607.24241'
url: https://arxiv.org/abs/2607.24241
pdf_url: https://arxiv.org/pdf/2607.24241
published: '2026-07-26'
collected: '2026-07-29'
category: Eval
direction: 生成式视频 · 专业评测基准
tags:
- Video Generation
- Benchmark
- Evaluation Agent
- Automatic Metric
- Cinematic AI
one_liner: 联合北电与影视工作室推出基于专业电影语言的视频生成基准及自动评测Agent
practical_value: '- 做电商短视频/广告片生成类业务的评测，可参考「从行业专业标准拆解多级细粒度metrics」的思路，避免仅依赖通用粗粒度质量指标

  - 做生成效果自动评测Agent的团队，可复用「从真实专业样本反向构造prompt集+分层领域专属评估算子」的架构，提升自动打分与人工排序的相关性

  - 做多镜头长视频生成业务（如品牌剧情广告生成），可参考该基准发现的单镜头到多镜头性能滑坡问题，针对性优化长时序连贯生成能力'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有视频生成基准多采用网络/LLM模板prompt、通用多模态模型打分，评测维度仅覆盖基础视觉质量、粗粒度文本对齐等，未对标影视行业专业电影语言标准，无法评估电影级生成工艺水平。
### 方法关键点
1. 联合北电、影视工作室，从获奖电影片段反向构建1169条专业prompt，其中1056条为多镜头，覆盖20种影视类型，每条均对应真实实拍参考；
2. 设计三级电影语言评测体系，含3轴12类共35个T2V子指标+3个R2V专属子指标；
3. 自研专家级自动评测Agent，开源核心电影语言算子库FilmOps。
### 关键结果
自动评测与人工排序的模型级斯皮尔曼系数达0.95（T2V）、0.96（R2V）；主流模型得分远低于传统网络基准，普遍存在动态美学短板，且弱模型多镜头性能滑坡更显著。

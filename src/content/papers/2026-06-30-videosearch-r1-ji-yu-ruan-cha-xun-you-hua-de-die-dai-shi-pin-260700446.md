---
title: 'VideoSearch-R1: Iterative Video Retrieval and Reasoning via Soft Query Refinement'
title_zh: VideoSearch-R1：基于软查询优化的迭代视频检索与推理框架
authors:
- Seohyun Lee
- Seoung Choi
- Dohwan Ko
- Jongha Kim
- Hyunwoo J. Kim
affiliations:
- KAIST
- Korea University
arxiv_id: '2607.00446'
url: https://arxiv.org/abs/2607.00446
pdf_url: https://arxiv.org/pdf/2607.00446
published: '2026-06-30'
collected: '2026-07-02'
category: Agent
direction: Agent 多模态视频检索推理优化
tags:
- Video Retrieval
- Soft Query Refinement
- GRPO
- Multi-turn Reasoning
- Agent
one_liner: 提出融合视频搜索引擎的Agent框架与软查询优化技术，实现大规模视频库检索与时序推理SOTA
practical_value: '- 软查询优化（SQR）思路可迁移到电商搜索/推荐的query改写场景，直接在Embedding空间优化query表示，避免离散文本改写引入的语义噪声，同时降低token开销

  - 多轮「召回-验证-优化」的Agent闭环设计可复用在商品/短视频内容的粗召回后修正流程，用2-3轮小迭代快速修正初始召回错误，提升整体召回准确率

  - GRPO多任务奖励联合优化范式可借鉴到「检索+下游任务（如商品属性匹配、内容片段定位）」的端到端训练，用任务级奖励替代分阶段监督，减少误差传播

  - SQR训练用InfoNCE对比损失做弱监督，不需要标注改写后的query，可大幅降低query优化模块的标注成本，适合工业界少标注场景'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有视频检索方案将召回与下游推理解耦，初始召回失败会直接导致后续精细推理任务失效；当前主流视频Agent框架默认相关视频已给定，无法支撑大规模视频库的检索需求；传统硬文本改写的query优化方式易引入语义噪声，token开销高，效果与效率均不理想。

### 方法关键点
- 多轮迭代Agent框架：每轮调用外部视频搜索引擎召回Top1视频，验证query与视频匹配度，不匹配则触发查询优化，匹配则执行时序定位输出结果
- 软查询优化（SQR）：不在离散文本空间改写query，直接在连续隐空间生成8个软query token，拼接原query embedding后用于召回，用InfoNCE对比损失优化软query与目标视频的相似度
- 两阶段训练：第一阶段SFT冷启动，用强VLM生成的CoT标注训练匹配验证、时序定位能力，同时优化SQR；第二阶段用GRPO做RL训练，设计格式、验证、检索、时序定位4类奖励联合优化全流程

### 关键结果
在ActivityNet-FIG、Charades-FIG、DiDeMo-FIG三个VCMR基准数据集上测试，对比同参数Qwen3-VL-2B基线：视频检索VR R@1最高提升6.0，端到端VCMR 0.3/R@1最高提升9.7；SQR仅用8个软token，效果优于平均26.8个token的硬文本改写，VR R@1多提升3.5个点；多轮推理最多3轮即可饱和，平衡效率与效果。

> 隐空间软查询优化比离散文本改写更适配检索场景，能以更低的token开销实现更精准的query表示调整，同时避免文本改写引入的语义噪声

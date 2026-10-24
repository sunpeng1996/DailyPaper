---
title: 'Making MLLM Latents Matter: Factor-Aware Predictive Learning for Cinematic
  Video Generation'
title_zh: 让MLLM隐层发挥价值：面向电影级视频生成的因子感知预测学习
authors:
- Songlin Yang
- Zhe Wang
- Xiaotong Zhao
- Xi Wang
- Ran Zhang
- Shuai Li
- Taiyi Wu
- Songlian Li
- Eric Liu
- Alan Zhao
affiliations:
- MMLab@HKUST, The Hong Kong University of Science and Technology
- Tencent Video
- École Polytechnique
arxiv_id: '2610.30926'
url: https://arxiv.org/abs/2610.30926
pdf_url: https://arxiv.org/pdf/2610.30926
published: '2026-10-22'
collected: '2026-10-24'
category: Multimodal
direction: 多模态大模型 · 可控视频生成
tags:
- MLLM
- Video Generation
- Diffusion Transformer
- Factor-aware Control
- Temporal Inference
one_liner: 提出因子感知预测学习FAPL，强化MLLM隐层在电影级视频生成的可控性与时序推理能力
practical_value: '- 冻结预训练大模型+仅训下游模块/连接器的增量训练范式，可直接迁移到电商商品短视频生成场景，大幅降低训研成本

  - 因子感知控制思路（指定目标因子修改、其余因子保留），可复用在商品素材定向编辑需求，如换背景/模特而保留商品本身特征

  - 有限输入下的时序推理训练策略，可参考用于少样本（短文本/少数参考图）生成完整带货短视频的业务场景'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
电影级视频生成需要同时满足有限输入下的时序推理、以及人物/场景/动作/镜头等多因子可控编辑两大需求，现有MLLM表征无法直接适配Video DiT的生成链路，存在表征利用不充分、可控性弱、时序预测效果差的问题。
### 方法关键点
1. 提出FAPL框架，先通过latent-only生成器锚定训练，冻结MLLM与连接器，强化DiT对MLLM latents的利用效率；
2. 引入factor-span替换训练，基于配对视频数据学习目标因子修改、非目标因子保留的可控编辑逻辑；
3. 冻结训练完成的DiT，反向优化MLLM与连接器，适配稀疏输入的时序预测需求。
### 关键结果
在稀疏输入转视频、因子感知编辑、多镜头生成三类电影级视频生成任务上全面优于基线，验证了MLLM特征利用、时序控制、因子协同三方面的显著提升

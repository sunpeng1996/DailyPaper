---
title: x-Prediction Is All You Need:Training-Free Accelerated Generation via Endpoint
  Decodability
title_zh: 基于x预测与端点可解码性的生成式模型免训练推理加速
authors:
- Xin Peng
- Ang Gao
affiliations:
- School of Physical Science and Technology, Beijing University of Posts and Telecommunications
arxiv_id: '2607.06114'
url: https://arxiv.org/abs/2607.06114
pdf_url: https://arxiv.org/pdf/2607.06114
published: '2026-07-07'
collected: '2026-07-08'
category: Training
direction: 生成式模型 · 免训练推理加速
tags:
- Diffusion Model
- Flow Matching
- Inference Acceleration
- Training-Free
- Sampling Optimization
one_liner: 提出免训练的截断跳跃采样方法TJS，可将扩散/流匹配模型NFEs降低20-70%且生成质量几乎不变
practical_value: '- 电商场景生成式文案/商品图生成任务可直接复用TJS，无需重训现有SD类checkpoint就能降低推理latency 20%以上，适配高QPS需求

  - 生成式推荐团队可直接集成TJS到推理pipeline，无需调整模型架构或训练流程，改造成本极低

  - Agent多模态内容生成模块可引入该方法优化推理速度，降低端到端响应延迟，提升交互体验'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
扩散、流匹配等生成模型推理时需要数十到数百次神经函数评估（NFEs），现有加速方案大多需要重训、蒸馏或调整生成轨迹，针对已发布checkpoint的改造成本极高，难以落地到高QPS业务场景。
### 方法关键点
挖掘x-prediction的端点可解码性特征：标准仿射概率路径的中间状态+路径速度可直接得到干净样本的最小MSE估计$oldsymbol{E}[x_0|x_t]$，据此提出截断跳跃采样（TJS）：在ODE采样过程中提前在$t^*$时刻退出，直接解码得到最终生成结果，全程无需重训、蒸馏、修改模型架构或生成轨迹。
### 关键结果
在SDXL、SD3.5M、Z-Image-Turbo等主流生成模型及3个类条件基准测试集上，TJS可降低20%~70%的NFEs，同时生成质量与全量采样几乎一致

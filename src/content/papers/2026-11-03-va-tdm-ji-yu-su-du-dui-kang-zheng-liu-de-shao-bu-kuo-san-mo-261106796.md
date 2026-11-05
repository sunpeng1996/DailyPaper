---
title: 'VA-TDM: A Unified View for Improving Few-Step Diffusion Models by Velocity
  Adversarial Distillation'
title_zh: VA-TDM：基于速度对抗蒸馏的少步扩散模型优化统一框架
authors:
- Yihong Luo
- Tianyu Pang
- Tianyang Hu
affiliations:
- Hong Kong University of Science and Technology
- The Chinese University of Hong Kong, Shenzhen
arxiv_id: '2611.06796'
url: https://arxiv.org/abs/2611.06796
pdf_url: https://arxiv.org/pdf/2611.06796
published: '2026-11-03'
collected: '2026-11-05'
category: Training
direction: 多模态生成 · 扩散模型蒸馏
tags:
- Diffusion Model
- Knowledge Distillation
- Adversarial Learning
- Text-to-Image
- Text-to-Video
one_liner: 提出速度对抗蒸馏框架VAD，统一多类扩散蒸馏方法，实现SOTA 4步文生图文生视频性能
practical_value: '- 生成式推荐场景下可复用VAD蒸馏思路，将大参数文生海报、文生商品描述模型蒸馏为少步推理版本，在不损失生成质量的前提下降低推理延迟，满足线上实时性要求

  - 可复用双形式速度混合+共享骨干的Trick，蒸馏时同时对齐矩和全分布信息，既降低训练成本，又提升生成内容的多样性和指令遵循度

  - 少步生成模型蒸馏时，可加入transition-aware字段输入（将当前生成步骤ID作为额外输入喂给辅助网络），解决不同步骤分布不一致问题，提升细粒度生成质量（如电商海报文字渲染准确性）'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
少步扩散蒸馏可大幅降低生成模型推理成本，但现有方法存在中间步骤学生分布估计不准、训练信号与实际分布不匹配的问题，同时各类蒸馏方法缺乏统一理论框架，难以针对性优化。

### 方法关键点
- 提出速度对抗蒸馏VAD框架，通过可学习critic对齐学生和教师的速度场，统一分数蒸馏、Fisher匹配、矩匹配等多类现有扩散蒸馏方法，可推导新的训练目标
- 基于VAD设计VA-TDM，结合A-form（低方差矩对齐）和B-form（全分布对齐）两种速度监督，采用共享骨干网络降低训练开销，混合pathwise和flow-product更新平衡训练稳定性和性能
- 引入transition-aware场估计，将学生当前过渡步骤作为额外输入喂给辅助网络，解决不同步骤分布差异导致的监督不准问题，搭配ODE回归热启动提升训练效率

### 关键实验结果
在SD3.5-Medium、FLUX.2 4B、33B MiniMax-H3三个backbone上做4步生成实验，对比TDM、官方4步模型等基线：SD3.5上GenEval从0.61提升到0.67；FLUX.2上OCR相似度从0.64提升到0.69、LPIPS多样性从0.47提升到0.56；33B MiniMax-H3的4步版本在人类偏好测试中赢Fast-H3的比例达61.33%，对100步教师的偏好率达45.53%，远高于Fast-H3的24.67%。

最值得记住的一句话：速度场对齐的对抗蒸馏框架可统一现有各类少步扩散蒸馏方法，仅需4步推理就能逼近上百步教师模型的生成质量。

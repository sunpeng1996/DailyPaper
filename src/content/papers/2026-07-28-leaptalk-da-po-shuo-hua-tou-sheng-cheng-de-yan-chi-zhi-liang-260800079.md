---
title: 'LeapTalk: Breaking the Latency-Quality Trade-off in Talking Head Generation'
title_zh: LeapTalk：打破说话头生成的延迟-质量权衡
authors:
- Rongxiang Zhang
- Songhua Liu
affiliations:
- Shanghai Jiao Tong University
- Harbin Institute of Technology
arxiv_id: '2608.00079'
url: https://arxiv.org/abs/2608.00079
pdf_url: https://arxiv.org/pdf/2608.00079
published: '2026-07-28'
collected: '2026-08-05'
category: Multimodal
direction: 多模态实时数字人说话头生成优化
tags:
- Talking_Head_Generation
- Knowledge_Distillation
- Diffusion_Model
- Real-Time_Generation
- Brownian_Bridge
one_liner: 提出单步桥接蒸馏框架，实现200FPS高保真长时序实时说话头生成
practical_value: '- 单步蒸馏+SNR对齐时间转换方案可复用在电商直播数字人场景，大幅降低推理延迟，满足实时互动要求

  - 基于持久参考的Brownian bridge数据传输思路，可解决长时直播数字人身份漂移问题，提升用户观感

  - 音频驱动的无分类器引导机制可直接迁移到数字人带货场景，优化口型同步精度，降低内容违和感'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
长时序实时说话头生成存在延迟-质量权衡：多步扩散推理延迟高，不支持流式生成；自回归实时方案存在误差累积、身份漂移问题，无法落地高要求的实时场景。
### 方法关键点
1. 提出单步桥接蒸馏框架，基于Brownian bridge设计数据到数据的传输范式，以持久参考图像为锚点缓解身份漂移，提升长时时序稳定性；
2. 采用SNR对齐的时间转换Φ(τ)实现异构蒸馏，消除预训练扩散教师模型与学生桥接模型的功能差异，完成知识平滑迁移；
3. 设计音频驱动的无分类器引导机制，在单步极简推理下保留细粒度口型同步效果。
### 关键结果
仅需1次前向推理即可生成任意长度的高保真时序一致视频，推理帧率最高达200FPS，效率和稳定性显著优于现有方案。

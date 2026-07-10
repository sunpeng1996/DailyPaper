---
title: 'OPSD-V: On-Policy Self-Distillation for Post-Training Few-Step Autoregressive
  Video Generators'
title_zh: OPSD-V：面向少步自回归视频生成器的同策略自蒸馏后训练方法
authors:
- Hongyu Liu
- Chun Wang
- Feng Gao
- Xuanhua He
- Yue Ma
- Ziyu Wan
- Yong Zhang
- Xiaoming Wei
- Qifeng Chen
affiliations:
- Meituan
- HKUST
- City University of Hong Kong
arxiv_id: '2607.08766'
url: https://arxiv.org/abs/2607.08766
pdf_url: https://arxiv.org/pdf/2607.08766
published: '2026-07-08'
collected: '2026-07-10'
category: Multimodal
direction: 多模态生成 · 自回归模型蒸馏优化
tags:
- Self-Distillation
- Autoregressive Generation
- Video Diffusion
- KV Cache
- Post-Training
one_liner: 提出同策略自蒸馏范式OPSD-V，缓解少步AR视频生成长序列误差累积且不改动推理逻辑
practical_value: '- AR序列生成场景下可复用同策略自蒸馏思路：用真实长序列替换KV cache中陈旧生成内容做监督，无需改动推理逻辑即可缓解长序列误差累积

  - 电商短视频生成业务可直接集成OPSD-V到现有少步AR视频扩散模型后训练流程，提升长视频的运动连贯性与整体画质

  - 多轮交互Agent生成长上下文内容时，可借鉴该方案用真实上下文替换历史错误生成内容做蒸馏监督，降低多轮输出退化概率'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有少步自回归（AR）视频生成模型推理延迟低，但长序列生成时存在显著误差累积、运动动态弱化问题，现有优化方案往往需要修改推理逻辑，落地成本高。
### 方法关键点
1. 提出OPSD-V同策略自蒸馏后训练范式，训练时引入真实长视频作为时序上下文，提供稠密轨迹级监督
2. 学生分支完全对齐推理逻辑，基于自身生成的历史KV cache逐块生成内容
3. 教师分支在相同去噪状态下，用真实视频上下文替换旧的历史缓存提供修正监督，同时保留近期模型生成缓存保证AR一致性，全程不改变推理侧采样器、去噪步数、KV cache机制
### 关键结果
在Self-Forcing、LongLive等基准少步AR视频模型上验证，视觉质量、运动动态、VBenchLong得分均实现一致提升；用户研究显示，66.0%的整体偏好选择OPSD-V生成结果，排除平局后偏好占比达82.5%

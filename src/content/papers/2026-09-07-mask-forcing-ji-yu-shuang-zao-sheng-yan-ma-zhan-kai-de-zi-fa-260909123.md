---
title: 'Mask Forcing: Improving Autoregressive Video Diffusion Distillation via Dual-Noise
  Masking Rollout'
title_zh: Mask Forcing：基于双噪声掩码展开的自回归视频扩散蒸馏优化方法
authors:
- Zhuoran Zhao
- Shengju Qian
- Tongtong Liang
- Xianghao Kong
- Songchun Zhang
- Junchao Huang
- Guian Fang
- Xin Wang
- Pan Hui
- Anyi Rao
affiliations:
- HKUST(GZ)
- HKUST
- LIGHTSPEED
- UCSD
- CUHK(SZ)
arxiv_id: '2609.09123'
url: https://arxiv.org/abs/2609.09123
pdf_url: https://arxiv.org/pdf/2609.09123
published: '2026-09-07'
collected: '2026-09-10'
category: Training
direction: 视频生成 · 扩散模型蒸馏优化
tags:
- Diffusion Model
- Knowledge Distillation
- Autoregressive Generation
- Mode Collapse
- Video Generation
one_liner: 通过时空随机掩码注入干净信号缓解DMD蒸馏模式崩溃，提升AR视频扩散模型生成质量
practical_value: '- 电商/广告短视频生成场景下，做AR扩散模型蒸馏时可直接复用双噪声掩码策略，缓解模式崩溃问题，提升生成素材的多样性与真实感，无需额外标注数据

  - 做序列类生成任务（如用户行为序列建模、Agent长上下文生成、推荐结果序列生成）的知识蒸馏时，可通过在对应维度（时序/特征维度）随机掩码注入干净信号，减少自回归过程的误差累积

  - 知识蒸馏任务中若采用reverse KL目标出现模式坍缩问题，可借鉴掩码扰动思路引导学生模型探索教师分布的更多区间，避免输出同质化'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
自回归（AR）视频扩散模型适配实时生成场景，现有基于Distribution Matching Distillation（DMD）的方案将预训练双向扩散模型蒸馏为AR学生模型时，reverse KL目标的模式寻求特性易引发学生分布坍缩，仅覆盖教师分布的少数模式，生成内容存在过饱和、过平滑问题，视觉质量与真实感不足。
### 方法关键点
提出Mask Forcing双噪声掩码展开策略：在AR扩散蒸馏的自展开过程中，沿时空维度对输入做随机掩码，向带噪的自展开输入中注入更干净的信号。一方面扰动自展开过程引导学生探索教师分布的更多区域，缓解模式崩溃；另一方面干净token可作为带噪token的去噪指导，优化中间预测结果，减少误差累积。
### 关键结果
无需引入真实视频数据或额外后训练阶段，即可在多种现有AR视频扩散蒸馏方法上实现视觉质量的稳定提升

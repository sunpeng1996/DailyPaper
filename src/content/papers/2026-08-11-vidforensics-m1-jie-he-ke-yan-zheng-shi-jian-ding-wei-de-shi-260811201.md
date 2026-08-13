---
title: 'VidForensics-M1: Meta-Detection Reinforcement Learning with Verifiable Temporal
  Grounding for AI-Generated Video Forensics'
title_zh: VidForensics-M1：结合可验证时间定位的AI生成视频取证元检测强化学习方法
authors:
- Bowei Liu
- Zheng Lu
- Yuhan Bian
- Xinchen Zhang
- Xingming Shui
- Yuesheng Huang
- Xuhuan Li
- Zihao Liu
- Yifan Yang
- Jun Zhou
affiliations:
- Tsinghua University
- Peking University
- Renmin University of China
- Microsoft
arxiv_id: '2608.11201'
url: https://arxiv.org/abs/2608.11201
pdf_url: https://arxiv.org/pdf/2608.11201
published: '2026-08-11'
collected: '2026-08-12'
category: Other
direction: AIGC检测 · 伪造视频取证
tags:
- AI-Generated Video Forensics
- Meta-Detection
- Reinforcement Learning
- Temporal Grounding
- Reward Shaping
one_liner: 首次将元检测引入AI生成视频取证，结合可验证时间定位与证据引导奖励重分配实现鲁棒泛化检测
practical_value: '- 电商UGC/AI生成商品短视频审核场景可复用「预测结果+支撑证据」联合优化的强化学习范式，降低 hallucination
  导致的审核误判

  - 证据引导的奖励重分配策略可迁移至多模态分类/检测任务，在保留主任务监督信号的同时提升模型可解释性

  - 基于边界帧条件的成对真伪样本自动构建pipeline，可低成本扩充AIGC内容审核场景的训练数据集'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有MLLM驱动的AI生成视频检测器多依赖监督微调或粗粒度标签级强化学习，对未知视频生成器、跨域场景的泛化能力差；传统文本类证据易受hallucination干扰，可信度低。
### 方法关键点
1. 首次将元检测范式引入视频取证领域，联合优化检测标签与支撑证据，选择客观可验证的时序定位作为证据信号
2. 提出自动化数据集构建pipeline：基于边界帧条件的视频生成模型替换原始视频时序片段，自动生成成对真伪视频样本
3. 设计证据引导的奖励重分配机制：对标签预测正确的样本按证据质量重新分配奖励，同步提升检测精度与细粒度伪造定位能力
### 关键结果
大量实验验证，该方案跨未知生成器、跨域的检测性能显著优于现有SOTA检测器，同时可输出可验证的伪造时序区间，大幅提升结果可解释性

---
title: 'OPD-V: Visual On-Policy Self-Distillation with Modality Balance'
title_zh: OPD-V：引入模态平衡的视觉在策略自蒸馏方法
authors:
- Aniri
- Jinhe Bi
- Peng Liao
- Zengjie Jin
- Volker Tresp
- Fei Shen
- Yunpu Ma
- Tat-Seng Chua
affiliations:
- National University of Singapore
- Ludwig Maximilian University of Munich
- Munich Center for Machine Learning
- Sun Yat-sen University
arxiv_id: '2608.05131'
url: https://arxiv.org/abs/2608.05131
pdf_url: https://arxiv.org/pdf/2608.05131
published: '2026-08-04'
collected: '2026-08-06'
category: Training
direction: 多模态大模型 · 自蒸馏训练优化
tags:
- MLLM
- On-Policy Self-Distillation
- Modality Balance
- Visual Reasoning
- Training Optimization
one_liner: 通过正负教师构造模态平衡特权信息，优化MLLM视觉在策略自蒸馏，兼顾效果与训练效率
practical_value: '- 电商多模态Agent（商品理解、图文问答、直播内容生成）微调时，可复用正负教师的模态平衡检测思路，解决模型过度依赖文本先验、忽略视觉细节的问题，提升商品属性识别、穿搭推荐准确率

  - 自蒸馏训练时可借鉴Modality-Balance Trust Region的token选择机制，仅对视觉依赖强的token做蒸馏，可减少70%左右无效token计算，同时提升效果、降低训练成本

  - 小参数多模态模型优化可参考该方案的特权信息设计，仅通过图像变换（放大/遮挡）构造监督信号，无需额外标注，小模型即可媲美大几十倍参数的MLLM效果，适合低时延多模态推荐场景落地'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有MLLM在策略自蒸馏（OPSD）方法普遍忽略模态失衡问题：模型生成时过度依赖文本先验，即使任务需要视觉信息也不会充分调用视觉输入，导致精心构造的特权信息利用率低，自蒸馏效果受限。
### 方法关键点
- 构造正负双教师：正教师输入放大任务关键区域的Zoom-In Image，负教师输入随机遮挡关键区域的Mask Image，学生输入原始图像，三者共享EMA更新的同一份参数，无额外参数量
- 定义Modality-Balance Logits Margin：计算正负教师对学生生成token的打分差，仅将打分差为正的token划入模态平衡信任区域，证明这些token的预测更依赖视觉信息而非文本先验
- 轻量化蒸馏目标：仅在信任区域内用正教师的分布做Jensen–Shannon蒸馏，同时采用top-K=100的近似计算降低显存开销
### 关键实验
在6个多模态推理基准（V* Bench、ZoomBench、HR-Bench 4K/8K、MME-RealWorld中英子集）、4个Qwen系列MLLM骨干上对比5种后训练方法：Qwen3.5-4B骨干上平均准确率从64.3%提升到80.01%，绝对涨点15.7pp，领先现有最优自蒸馏方法2.9pp，4B参数效果超过1T参数的Kimi-K2.6；训练step latency 4B模型降低31.8%、9B模型降低24.7%，响应长度缩短74.5%。
### 核心结论
模态平衡本身可以作为自蒸馏的特权信息，无需额外标注就能同时提升MLLM视觉推理效果与训练效率

---
title: f-Divergence Self-Play for Tabular Anomaly Detection via Large Language Models
title_zh: 基于f散度自博弈的大语言模型表格数据异常检测方法
authors:
- Hoang Tran Vuong
- Linh Ngo Van
- Dang Nguyen
- Thin Nguyen
- Phuoc Nguyen
- Mehrtash Harandi
- Trung Le
affiliations:
- Hanoi University of Science and Technology
- Deakin University
- Monash University
arxiv_id: '2611.18370'
url: https://arxiv.org/abs/2611.18370
pdf_url: https://arxiv.org/pdf/2611.18370
published: '2026-11-13'
collected: '2026-11-16'
category: LLM
direction: 大模型微调 · 表格异常检测
tags:
- Large Language Model
- Self-Play
- f-Divergence
- Tabular Data
- Anomaly Detection
one_liner: 提出f散度驱动的自博弈微调框架DiSPaT，提升大模型表格异常检测性能
practical_value: '- 电商交易/用户行为等表格型异常检测场景，可复用将表格序列化为文本喂给LLM的处理思路，省去异构特征融合的繁琐工程

  - 标注稀缺的异常检测场景，可借鉴自博弈交替优化思路：用当前模型生成伪异常样本，再训练判别器得到反馈信号更新模型，降低标注依赖

  - 分布对齐类训练目标设计时，可参考f散度最小化的近似推导方法，收紧生成样本与真实正常样本的分布差，提升识别精度'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
表格数据包含数值、类别、文本等异构特征，难以学习正常分布的有效表征；现有LLM类表格异常检测方法依赖单轮有监督微调，信号不足，对正常样本的刻画精度有限。

### 方法关键点
基于f散度最小化理论，提出自博弈微调框架DiSPaT，训练目标锚定缩小真实正常数据与模型生成样本的分布差。采用交替优化机制：每轮由当前策略生成合成样本作为伪异常，判别器学习区分真实正常样本与伪异常，用判别信号更新策略，逐步对齐模型分布与真实正常数据分布。

### 关键结果
在多类基准数据集上，DiSPaT性能全面超越此前的LLM类、深度学习类、经典无监督异常检测方法。

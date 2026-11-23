---
title: Learning Video Foresight Reasoning from Unlabeled Videos via On-Policy Self-Distillation
title_zh: 基于同策略自蒸馏的无标注视频前瞻推理学习方法
authors:
- Jingchen Sun
- Jiaxing Zhang
- Qingqiao Hu
- Dingqiang Ye
- Yuqi Jia
- Yijun Liang
- Di Fu
- Yunjie Tian
- Dongdi Zhao
- Changyou Chen
affiliations:
- University at Buffalo
- Stony Brook University
- Johns Hopkins University
- Duke University
- University of Maryland, College Park
arxiv_id: '2611.26954'
url: https://arxiv.org/abs/2611.26954
pdf_url: https://arxiv.org/pdf/2611.26954
published: '2026-11-19'
collected: '2026-11-23'
category: Reasoning
direction: 多模态·视频前瞻推理
tags:
- Self-Distillation
- Video-Language
- Foresight-Reasoning
- Self-Supervised-Learning
- On-Policy-Learning
one_liner: 提出无需额外标注与LLM监督的自蒸馏框架Future-OPSD，显著提升视频前瞻推理效果
practical_value: '- 无标注数据自蒸馏思路可迁移到短视频推荐场景，利用用户观看的前序/后续视频对构造自监督信号，大幅降低标注成本

  - 前瞻评分加权机制可借鉴到短视频序列推荐中，对用户后续行为的高价值片段加权，抑制无关上下文干扰，提升序列建模效果

  - 同策略师生蒸馏框架可复用在多模态推荐模型增量训练中，无需外部大模型监督即可实现效果提升，有效控制训练成本'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有视频前瞻推理方法存在两大局限：一是依赖标注数据或外部大模型提供监督，可扩展性差；二是对未来片段全量等权处理，大量无关上下文会干扰模型学习有效信息。
### 方法关键点
1. 提出On-Policy自蒸馏框架Future-OPSD，直接利用视频的过去-未来对构造天然自监督信号，无需额外标注或外部LLM监督。
2. 定义前瞻得分推导对比特权优势，优化可求解的下界代理目标，插值真实与随机参考未来的优势、师生蒸馏优势，放大决策相关信息，抑制无关上下文。
### 关键结果
开放预测任务相对基线最高提升14.2个点，封闭规划任务最高提升15.9个点，且不会损害通用视频理解能力。

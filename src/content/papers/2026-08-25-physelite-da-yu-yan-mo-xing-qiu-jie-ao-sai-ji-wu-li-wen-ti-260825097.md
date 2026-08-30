---
title: 'PhysElite: How Far Are LLMs from Solving Olympiad-Level Physics Problems?'
title_zh: PhysElite：大语言模型求解奥赛级物理问题还有多少差距
authors:
- Ruoran Xu
- Wending Gao
- Liyunfeng Chen
- Aixin Shi
- Haoyu Cheng
- Zixiang Fang
- Yiqiang Zou
- Qiufeng Wang
affiliations:
- Xi’an Jiaotong-Liverpool University
arxiv_id: '2608.25097'
url: https://arxiv.org/abs/2608.25097
pdf_url: https://arxiv.org/pdf/2608.25097
published: '2026-08-25'
collected: '2026-08-30'
category: Eval
direction: 大模型复杂推理能力基准评测
tags:
- MLLM
- Reasoning Benchmark
- Physics Reasoning
- Multimodal Eval
- Complex Reasoning
one_liner: 构建含11586道题的双语多模态奥赛物理基准，实测最强MLLM准确率仅33.7%
practical_value: '- 可参考其step-level推理链路诊断方法，用于LLM导购/客服Agent复杂用户问题解决能力的错误归因，定位推理断点优化效果

  - 其多模态图文混合题目的标注范式可复用，用于构建电商场景下商品参数+图文的用户咨询场景评测数据集

  - 高难度任务的基准构建逻辑可借鉴，用于评估推荐系统中复杂用户需求（如专业家电选购、家装方案推荐）的生成效果'
score: 4
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有物理推理基准存在两大核心缺陷：一是缺乏高难度任务数据集，二是对视觉形式、知识点、分步解答过程的覆盖度不足，无法准确衡量模型解决复杂物理问题的真实能力。
### 方法关键点
构建PhysElite大规模双语多模态奥赛级物理推理基准，包含11586道不同难度的物理题，每道题配套对应可视化图表、中英双语分步推导解答路径及最终标准答案，覆盖K12到奥赛全难度层级。
### 关键结果
对18款开源、闭源多模态大模型开展基准测试，最强模型的答案准确率仅为33.7%；额外设计步骤级过程评测指标，可精准诊断模型在推理全链路中的具体失败节点。

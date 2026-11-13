---
title: Measuring, Revealing and Mitigating Harmful Content Propagation in Recommender
  Systems
title_zh: 推荐系统有害内容传播的量化、揭示与缓解方法研究
authors:
- Xiaokun Zhang
- Youlin Wu
- Junyu Lu
- Jiamin Chen
- Zhaochun Ren
- Hongfei Lin
- Fenglong Ma
- Xue Liu
- Chen Ma
affiliations:
- City University of Hong Kong
- Dalian University of Technology
- Leiden University
- Pennsylvania State University
- MBZUAI
arxiv_id: '2611.15160'
url: https://arxiv.org/abs/2611.15160
pdf_url: https://arxiv.org/pdf/2611.15160
published: '2026-11-11'
collected: '2026-11-13'
category: RecSys
direction: 负责任推荐 · 有害内容治理
tags:
- Recommender System
- Responsible AI
- Harmful Content Mitigation
- Benchmark
- Sequential Recommendation
one_liner: 构建带有害标注的推荐基准，提出通用MitiHarm框架抑制有害内容传播且保留用户满意度
practical_value: '- 数据标注环节可复用LLM+人审核的范式，先让LLM生成有害标签+理由，再人工投票修正，可降低79%以上的人工标注工作量，适合内容电商、短视频平台的内容安全标注场景

  - 可直接复用HP@k、HO@k两个指标衡量推荐结果的健康度，分别覆盖健康内容占比和排序优先级，补充现有推荐体系的安全维度评估

  - MitiHarm是模型无关的轻量插件，无需修改原有推荐模型结构，仅需补充有害内容表征和健康锚点注意力模块，就能实现有害内容抑制，精度损失控制在2%以内，可快速落地到现有推荐链路'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有推荐系统以提升精度、匹配用户兴趣为核心目标，完全忽略内容有害性（暴力、仇恨言论、歧视、虚假信息等）的传播风险，且行业缺乏带有害标注的公开数据集、无标准化的有害性评估指标，无法系统性评估和治理推荐侧的有害内容扩散问题，实测显示主流BERT4Rec生成的推荐列表近半数包含有害内容，会严重损害用户心智和平台生态。
### 方法关键点
- 数据层：提出LLM+人协同的标注范式，给TN、QB、EB-NeRD三个公开推荐数据集补充二元有害标签+有害理由标注，标注准确率超过79%，大幅降低人工标注成本
- 评估层：设计两个有害性评估指标，HP@k衡量top-k推荐中健康内容的占比，HO@k加权衡量健康内容的排序优先级，分值越高代表推荐健康度越好
- 算法层：提出通用模型无关的MitiHarm框架，在item表征融入有害理由信号，通过健康/有害锚点对比学习训练有害感知的用户自注意力，最终打分融合用户兴趣分和健康度分，用超参λ平衡两者权重
### 关键实验
在三个标注数据集上对比13个主流推荐模型，原有模型推荐的健康内容占比普遍低于50%；接入MitiHarm后，HP@5最高提升54.01%，HO@5最高提升50.32%，推荐精度损失普遍低于2%，部分场景精度略有提升；框架推理耗时增加不超过0.05s， overhead极低
### 核心结论
推荐系统的用户交互数据本身存在「有害内容交互率更高」的偏差，纯精度导向训练必然放大有害内容传播，必须在推荐链路显式引入健康度约束才能平衡用户体验和平台社会责任

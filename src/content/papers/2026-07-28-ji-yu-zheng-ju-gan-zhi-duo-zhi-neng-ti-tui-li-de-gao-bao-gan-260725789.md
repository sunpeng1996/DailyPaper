---
title: Towards Faithful Sentimental Image Captioning via Evidence-Aware Multi-Agent
  Reasoning
title_zh: 基于证据感知多智能体推理的高保真情感图像字幕生成
authors:
- Tiecheng Cai
- Zexian Yang
- Chao Chen
- Shanshan Lin
- Xiangwen Liao
affiliations:
- Fuzhou University
- Harbin Institute of Technology Shenzhen
arxiv_id: '2607.25789'
url: https://arxiv.org/abs/2607.25789
pdf_url: https://arxiv.org/pdf/2607.25789
published: '2026-07-28'
collected: '2026-07-29'
category: MultiAgent
direction: 多智能体协作 · 情感多模态生成
tags:
- Multi-Agent
- Image Captioning
- Hallucination Mitigation
- Affective Analysis
- Multimodal Generation
one_liner: 提出证据感知多智能体框架SEA-Cap，解决情感图像字幕生成的幻觉与情感漂移问题
practical_value: '- 「生成-校验-仲裁」的多智能体迭代优化架构可直接迁移到电商商品图配文、营销文案生成场景，解决生成内容与商品事实不符的幻觉问题

  - 从全局属性控制转向可验证细粒度实体级证据锚定的思路，可复用在广告素材合规校验、生成式推荐内容溯源场景

  - 共享黑板式的Agent协作机制可降低多模块交互开发成本，适合中小团队快速搭建多Agent生成校验链路'
score: 7
source: arxiv-cs.CV
depth: abstract
---

### 动机
情感图像字幕生成（SIC）需平衡情感表达与视觉保真度，现有方法缺乏本地视觉锚定与情感校验机制，极易出现幻觉、情感漂移，无法满足营销、内容生成等场景落地要求

### 方法关键点
1. 设计Sentiment Evidence Miner模块，提取结构化细粒度对象级情感线索，替代传统全局属性控制，锚定生成的情感依据
2. 基于共享黑板架构编排Generator、Hallucination Checker、Arbitrator三个Agent迭代优化，每轮生成结果强制与视觉证据对齐校验

### 关键结果
在两个公开SIC基准数据集上达到SOTA性能，有效降低生成幻觉，同时兼顾情感准确率与事实一致性

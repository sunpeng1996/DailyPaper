---
title: Human-AI Perceptual Alignment by Playing Hues and Cues
title_zh: 基于Hues and Cues桌游的人类与AI感知对齐评估框架
authors:
- Nuria Alabau-Bosque
- Jorge Vila-Tomás
- Paula Daudén-Oliver
- Pablo Hernández-Cámara
- Valero Laparra
- Jesús Malo
affiliations:
- Image Processing Lab, Universitat de València
arxiv_id: '2608.07141'
url: https://arxiv.org/abs/2608.07141
pdf_url: https://arxiv.org/pdf/2608.07141
published: '2026-08-07'
collected: '2026-08-10'
category: Eval
direction: 多模态模型评估 · 人-AI感知对齐
tags:
- CVLM
- Perceptual Alignment
- Model Evaluation
- Gamified Benchmark
- Multimodal
one_liner: 提出游戏化人-AI感知对齐评估框架，揭示CVLM语义颜色落地的偏差规律与优化方向
practical_value: '- 电商商品图/营销文案配色适配场景，可复用该研究公开的颜色-语义关联人类基准数据，优化视觉素材的用户感知匹配度

  - 多模态推荐/搜索系统做CVLM选型时，优先选择经高度curated预训练数据训练的模型，可降低抽象营销话术对应配色的感知偏差

  - 搭建多模态模型人对齐评估体系时，可借鉴游戏化任务设计思路，低成本收集细粒度人类共识标注数据'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
传统CVLM人对齐评估基准忽略细粒度语义、文化层面的感知差异，无法有效衡量模型对抽象概念的感知对齐能力。

### 方法关键点
1. 将桌游Hues and Cues的480个离散色板映射到CIE xy色度空间，构建覆盖7个语义类别的100词评估词表
2. 采集325名人类观察者的颜色关联数据，通过LOO交叉验证构建人类一致性基线作为误差下界
3. 跨架构、跨预训练数据集评测162款CVLM的语义颜色落地能力

### 关键结果数字
CVLM对食物、植物等实物类概念的颜色感知可对齐人类认知偏差，但在抽象、主观、流行文化领域偏差显著；严重偏差存在两类故障模式：语义误分类、不确定时默认输出蓝色坐标；使用高度curated的预训练数据集，相比大规模无标注语料可显著降低27%以上的严重对齐偏差

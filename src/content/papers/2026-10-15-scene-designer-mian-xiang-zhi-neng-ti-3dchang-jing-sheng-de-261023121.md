---
title: 'Scene-Designer: Learning Design Intelligence for Agentic 3D Scene Generation'
title_zh: Scene-Designer：面向智能体3D场景生成的设计智能学习框架
authors:
- Xuanyu Liu
- Hongyan Feng
- Miao Pan
- Sunlai Chen
- Lizhou Liang
- Bing Sun
- Wenqi Zhang
- Xuhong Zhang
affiliations:
- Zhejiang University
- OmniAI Laboratory
- Universal Identification Technology (Hangzhou) Co.,Ltd.
arxiv_id: '2610.23121'
url: https://arxiv.org/abs/2610.23121
pdf_url: https://arxiv.org/pdf/2610.23121
published: '2026-10-15'
collected: '2026-10-19'
category: Agent
direction: Agent 3D生成 · 批判引导训练框架
tags:
- Agent
- 3D Generation
- Critic Guided Training
- GRPO
- Dataset Construction
one_liner: 提出带设计-批判双能力的智能体3D场景生成框架，搭配专属数据集与Critic引导的GRPO训练方法
practical_value: '- 可复用「生成模块+领域专属Critic」的双Agent架构，在生成式推荐、电商文案生成等场景中减少试错成本，提升输出合规性

  - Critic引导GRPO的训练范式可迁移到搜索推荐的排序、召回优化任务，用小样本领域评价数据替代通用大模型打分，降低训练成本

  - 「Observation-Thought-Action/Critic」的数据集构建思路可用于电商导购Agent、商品3D展示生成的微调数据制作，提升垂直领域Agent能力'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有3D场景生成方法要么依赖通用大模型缺乏领域设计经验，要么仅从静态场景学习，生成结果的物理合理性、功能可用性、布局一致性均达不到落地要求。
### 方法关键点
1. 构建两个垂直领域数据集：Scene-OTA-35K（含观察-思考-动作监督，用于学习场景设计与高效纠错）、Scene-OTC-15K（含观察-思考-批判监督，用于学习多维度场景质量评价）
2. 提出Scene-GRPO框架，用Critic引导GRPO训练优化设计决策，降低不必要的试错成本，测试阶段仍可通过Critic引导进一步提升生成效果
### 关键结果数字
Scene-Designer在物理有效性、功能正确性、布局一致性指标上均达SOTA；训练得到的Scene-Critic在场景评价任务上效果显著优于通用大模型，且设计与批判能力存在相互增强的正向趋势。

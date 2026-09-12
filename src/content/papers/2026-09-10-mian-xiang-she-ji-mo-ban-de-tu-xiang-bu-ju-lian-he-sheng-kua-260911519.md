---
title: Learning Interaction between Image and Layout Priors for Joint Image-Layout
  Generation in Design Templates
title_zh: 面向设计模板的图像-布局联合生成跨模态交互学习方法
authors:
- Shirong Yang
- Bo Yang
- Ying Cao
arxiv_id: '2609.11519'
url: https://arxiv.org/abs/2609.11519
pdf_url: https://arxiv.org/pdf/2609.11519
published: '2026-09-10'
collected: '2026-09-12'
category: Multimodal
direction: 多模态生成 · 图文布局联合生成
tags:
- Diffusion Model
- Multimodal Generation
- Layout Generation
- Design Automation
- Test-time Guidance
one_liner: 通过可学习通信模块连接预训练图像与布局扩散模型，实现双向交互的设计模板联合生成
practical_value: '- 电商广告banner、商品详情页生成场景可复用「冻结预训练单模态大模型仅训练跨模态通信模块」的范式，大幅降低训练成本的同时保证单模态生成质量

  - 多模态素材生成任务可迁移双向跨模态交互建模思路，替代传统串行生成方案，优化图文搭配和谐度，提升广告素材投放效果

  - 测试时引导策略可直接复用到个性化素材生成场景，无需重训即可响应用户自定义的布局、风格偏好，适配千人千面的广告投放需求'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有设计模板生成多采用串行范式，无法准确捕捉背景图与前景布局的依赖关系，导致生成内容搭配和谐度低，难以满足实际商用设计需求。
### 方法关键点
1. 提出InterIL联合生成模型，在单一生成流程内同步输出背景图与前景布局，通过可学习通信模块连接预训练图像、布局扩散模型骨干，显式建模双向跨模态交互
2. 训练阶段冻结两个单模态预训练骨干，仅更新通信模块，既保留预训练先验能力，又聚焦学习跨模态关联，无设计领域特定归纳偏置，适配真实设计特征
3. 引入测试时引导策略，无需重训即可支持用户自定义偏好调整生成结果
### 关键结果
对比现有串行方案，在图像质量、布局合理性、图文协调性三个维度均取得显著提升，生成结果更接近真实人工设计样本

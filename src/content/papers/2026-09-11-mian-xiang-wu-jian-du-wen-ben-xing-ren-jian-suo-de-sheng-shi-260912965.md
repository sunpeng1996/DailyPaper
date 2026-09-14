---
title: Generative Retrieval for Unsupervised Text-Based Person Search
title_zh: 面向无监督文本行人检索的生成式检索方法
authors:
- Mang Ye
- Yucheng Ji
- Yang Bai
- Min Cao
- Siyuan Chai
- Bo Du
- Min Zhang
arxiv_id: '2609.12965'
url: https://arxiv.org/abs/2609.12965
pdf_url: https://arxiv.org/pdf/2609.12965
published: '2026-09-11'
collected: '2026-09-14'
category: Other
direction: 无监督跨模态检索 · 生成式伪标签构造
tags:
- Generative Retrieval
- Unsupervised Learning
- Cross-Modal Retrieval
- Pseudo Label
- Dataset Construction
one_liner: 提出两阶段生成-检索框架GTR+与大规模细粒度TBPS数据集，实现无标注下文本行人检索性能提升
practical_value: '- 无标注跨模态检索场景可复用三层伪文本生成pipeline：先通过QA生成基础属性、再用对比机制增强细粒度、最后风格化扩充多样性，大幅降低标注成本

  - 伪标签降噪可借鉴高斯混合模型+双维度置信度（实时跨模态相似度+静态生成概率）的自适应加权方案，减少噪声样本对训练的干扰

  - 电商跨模态商品召回预训练可参考LargeFine-Person数据集的细粒度标注规范，提升模型对用户自然语言query的匹配精度'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有基于文本的行人检索（TBPS）方法依赖人工标注的图文配对数据，标注成本极高，无法适配大规模无标注场景的落地需求。
### 方法关键点
两阶段GTR+生成-检索框架核心设计：
1. 生成阶段采用三层时序生成流程：基础层通过自动QA机制生成视觉属性基础描述，中间层通过样本间对比机制增强细粒度细节，高层通过风格化扩充机制提升文本多样性，生成高质量伪标注文本；
2. 检索阶段引入自适应置信度加权学习方案，采用高斯混合模型区分干净/噪声伪图文对，结合实时图文相似度与前序阶段静态文本生成概率校准样本权重，降低伪标签噪声对训练的影响；
3. 开源LargeFine-Person大规模TBPS数据集，提供高质量细粒度、多样化文本标注，作为无监督场景下的预训练基准。
### 关键结果
在多个公开TBPS基准数据集上，GTR+性能显著优于现有无监督基线方法，LargeFine-Person数据集预训练可进一步提升跨模态检索模型的泛化性。

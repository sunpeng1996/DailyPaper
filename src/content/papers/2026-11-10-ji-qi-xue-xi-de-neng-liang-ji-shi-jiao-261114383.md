---
title: An Energy-Based Perspective on Machine Learning
title_zh: 机器学习的能量基视角
authors:
- Bo Dai
- Yilun Du
affiliations:
- Georgia Institute of Technology
- Harvard University
arxiv_id: '2611.14383'
url: https://arxiv.org/abs/2611.14383
pdf_url: https://arxiv.org/pdf/2611.14383
published: '2026-11-10'
collected: '2026-11-12'
category: Other
direction: 能量基模型 · 机器学习统一范式
tags:
- EBM
- Energy-Based Model
- Contrastive Learning
- Generative Model
- Representation Learning
one_liner: 以能量基模型EBM为统一视角串联全领域ML方法，给出统一分析框架与新算法生成路径
practical_value: '- 可复用EBM能量组合范式，在推理阶段直接融合召回、排序、用户偏好、业务规则等异构模型输出，无需重新训练

  - 推荐系统的排序、召回损失可统一到EBM对比学习框架下，仅替换单一组件（如采样策略）即可优化效果，无需重构训练流程

  - 电商导购Agent的世界建模、决策规划模块可采用EBM框架，天然支持多目标约束的组合推理，适配用户多意图场景'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
长期以来EBM仅被视为单一模型族，不同机器学习方向的算法分散缺乏统一分析框架，难以为跨域算法创新提供理论指引。
### 方法关键点
将所有机器学习方法拆解为**能量定义、推理流程、学习方法**三个核心组件，证明判别模型、GAN、扩散模型、对比学习、BERT、强化学习等各类主流算法本质都是不同组件配置的EBM，核心差异仅在配分函数与采样策略的处理方式，且所有学习方法共享统一对比结构。
### 成果
构建了覆盖全机器学习领域的EBM统一分析框架，支持仅替换单一组件快速生成新算法，同时提出能量组合的原则性方法，可在推理阶段直接融合多个已训练模型，无需额外微调。

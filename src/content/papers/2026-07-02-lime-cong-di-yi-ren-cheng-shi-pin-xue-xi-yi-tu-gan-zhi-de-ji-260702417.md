---
title: 'LIME: Learning Intent-aware Camera Motion from Egocentric Video'
title_zh: LIME：从第一人称视频学习意图感知的相机运动生成
authors:
- Boyang Sun
- Jiajie Li
- Yung-Hsu Yang
- Chenyangguang Zhang
- Tim Engelbracht
- Sunghwan Hong
- Cesar Cadena
- Marc Pollefeys
- Hermann Blum
affiliations:
- ETH Zurich
- Microsoft
- University of Bonn
arxiv_id: '2607.02417'
url: https://arxiv.org/abs/2607.02417
pdf_url: https://arxiv.org/pdf/2607.02417
published: '2026-07-02'
collected: '2026-07-05'
category: Other
direction: 具身智能 · 意图感知主动感知
tags:
- Embodied AI
- Active Perception
- Vision-Language
- Camera Motion
- Egocentric Video
one_liner: 从被动第一人称视频挖掘多意图监督，构建结合自回归输出与流匹配头的视觉语言相机运动生成模型LIME
practical_value: '- 多粒度意图对应多粒度动作的建模思路可迁移：电商场景下，用户「逛类目/找特定商品/看参数细节」不同粒度意图可对应差异化推荐策略（粗排扩召回/精排提权重/详情页信息结构化展示）

  - 被动观测数据挖掘弱监督三元组的方法可复用：可从用户行为日志中批量构造「用户意图-交互收益-系统动作」样本，大幅降低模型训练的标注成本

  - 「可解释收益输出+连续动作头」的联合建模架构可参考：生成式推荐场景可同时输出推荐理由和候选item集，兼顾推荐可解释性和用户多样化需求覆盖'
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
具身机器人执行操纵、问答等任务前，需根据用户自由意图调整相机位姿获取有效观测，但现有视觉语言工作多聚焦基座移动、操作动作生成，语言条件下的相机运动作为独立动作维度研究不足；且该任务需要适配从粗粒度空间移动到细粒度细节查看、遮挡区域揭示等不同语义层级的意图，建模难度高。
### 方法关键点
1. 采用从被动第一人称视频中挖掘多意图监督的范式，批量构造「自然语言意图-观测收益描述-相对SE(3)目标位姿」三元组训练数据，无需人工标注；
2. LIME模型融合自回归观测收益生成分支与连续流匹配位姿预测头，同时输出下一次观测能获取的有效信息和多候选目标位姿，覆盖多假设需求。
### 关键结果
在视点预测任务及下游操纵、具身问答等机器人任务上性能优于基线，可直接将普通人类第一人称录制视频转化为主动感知任务的可用监督信号。

---
title: 'The Moving Eye: Enhancing VLA Spatial Generalization via Hybrid Dynamic Data
  Collection'
title_zh: 《动眼：通过混合动态数据采集增强VLA空间泛化能力》
authors:
- Jincheng Tang
- Yilong Zhu
- Zhengyuan Xie
- Jiang-Jiang Liu
- Jiaxing Zhang
arxiv_id: '2607.02322'
url: https://arxiv.org/abs/2607.02322
pdf_url: https://arxiv.org/pdf/2607.02322
published: '2026-07-02'
collected: '2026-07-04'
category: Multimodal
direction: 多模态VLA · 数据采集优化
tags:
- VLA
- Spatial Generalization
- Shortcut Learning
- Data Collection
- Multimodal Model
one_liner: 提出静态多视角+连续动态相机的混合数据采集策略，缓解VLA捷径学习，提升跨架构空间泛化能力
practical_value: '- 数据层面解决泛化问题的思路可迁移至多模态推荐训练：优先通过数据构造消除虚假特征耦合，性价比高于单一调整模型结构

  - 动静混合的数据增强策略可复用在多模态搜索/推荐场景：混合固定视角与动态变化视角的商品/内容样本，提升模型跨场景泛化性

  - 捷径学习普适性结论可指导多模态Agent训练：所有架构的多模态模型均易依赖虚假关联，数据分布优化是泛化提升的核心抓手'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
VLA模型在机器人操控任务中语义理解能力优异，但空间泛化性脆弱，相机位姿或物体配置的微小变动就会导致性能骤降；仅增加静态视角数量无法解决问题，模型易陷入捷径学习，依赖相机-机器人-物体的虚假关联而非真实空间关系。

### 方法关键点
采用双臂实验设置，一臂执行操控任务，另一臂作为移动环境相机，系统评测Fixed、Multi-Fixed、Moving Views三类数据分布的效果，最终采用连续相机运动+多样化静态视角的混合策略，平衡虚假关联消除与训练稳定性。

### 关键结果数字
混合策略效果远优于仅增加静态视角，可让VLA泛化到未见过的相机位姿与物体配置；该收益具有跨架构普适性，ACT、Diffusion、Pi0、Gr00t等所有评测模型均获得显著性能提升。

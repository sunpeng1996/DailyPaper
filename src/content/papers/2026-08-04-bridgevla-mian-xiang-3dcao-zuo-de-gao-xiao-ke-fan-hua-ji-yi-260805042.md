---
title: 'BridgeVLA++: A Data-Efficient, Generalizable, and Memory-Augmented Vision-Language-Action
  Framework for 3D Manipulation'
title_zh: BridgeVLA++：面向3D操作的高效可泛化记忆增强视语言动作框架
authors:
- Peiyan Li
- Yuze Zhu
- Yixiang Chen
- Qisen Ma
- Yuan Xu
- Jiabing Yang
- He Guan
- Yan Huang
- Hongtao Wu
- Xiao Ma
arxiv_id: '2608.05042'
url: https://arxiv.org/abs/2608.05042
pdf_url: https://arxiv.org/pdf/2608.05042
published: '2026-08-04'
collected: '2026-08-06'
category: Other
direction: 多模态VLA · 时空记忆增强架构
tags:
- VLM
- Memory Augmentation
- VLA
- 3D Manipulation
- Multimodal
one_liner: 为BridgeVLA添加统一时空记忆架构，实现兼顾数据效率、泛化性的记忆感知3D VLA框架
practical_value: '- 统一时空记忆架构的设计思路可迁移至多轮交互电商Agent的上下文建模，提升长周期用户行为序列的依赖捕捉效率

  - 预训练模型微调时保留原生输入输出对齐的技巧，可复用在小样本场景下的多模态搜索/推荐模型微调，降低标注数据需求

  - 记忆增强模块不损害原有模型性能的迭代思路，可参考用于推荐系统的用户行为记忆模块升级，避免线上效果回退'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有3D VLA模型普遍存在数据需求量大、分布偏移下泛化性差、无过往观测显式记忆三大缺陷，无法适配数据稀缺、开放世界、依赖记忆的操作场景。
### 方法关键点
在原有BridgeVLA基础上新增统一时空记忆架构，建模持久化空间上下文与时间交互历史；微调阶段保留预训练VLM的输入输出对齐，先将点云投影为多视角图、预测中间热图再生成动作，兼顾记忆推理能力与原模型的数据效率、泛化性。
### 关键结果
在两项依赖记忆的操作基准上取得SOTA性能，同时不损失原模型的数据效率与泛化性；适配双操作臂场景，在真实机器人平台验证有效，支持跨任务、环境、平台扩展。

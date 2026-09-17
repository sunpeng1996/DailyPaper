---
title: 'ActionPiece: Rethinking Action Tokenization for Autoregressive Vision-Language-Action
  Models'
title_zh: ActionPiece：自回归视觉-语言-动作模型的动作分词重思考
authors:
- Shijie Lian
- Bin Yu
- Zhaolong Shen
- Xiaopeng Lin
- Yichao Du
- Zhirui Zhang
- Laurence T. Yang
- Kai Chen
affiliations:
- Huazhong University of Science and Technology
- Harbin Institute of Technology
- Beihang University
- The Hong Kong University of Science and Technology (Guangzhou)
- DeepCybo
arxiv_id: '2609.18487'
url: https://arxiv.org/abs/2609.18487
pdf_url: https://arxiv.org/pdf/2609.18487
published: '2026-09-15'
collected: '2026-09-17'
category: Agent
direction: 具身Agent · 动作tokenization优化
tags:
- VLA
- Action Tokenization
- Autoregressive Model
- Embodied Agent
- Quantization
one_liner: 提出物理秩一致性评估指标与ActionPiece动作分词框架，大幅提升VLA模型任务成功率与泛化性
practical_value: '- 离散token化场景（如Semantic ID生成、用户行为序列编码）可借鉴物理秩一致性指标，替代单纯MSE评估，保留序列/特征的相对关系

  - 向量量化（VQ）类任务可加入近远距离排序监督、码本分配分布正则，提升压缩后特征的关系保序性，减少上下文语义损失

  - 多模态Agent的指令到动作映射模块可复用ActionPiece的联合监督思路，提升跨场景动作泛化准确率'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
当前自回归VLA模型的动作分词器依赖MSE等逐点重构指标评估，仅能衡量单点误差，无法保留不同上下文下动作调整的相对关系，压缩后动作的细粒度上下文适配信号易失真、反转，严重影响策略泛化性。
### 方法关键点
1. 提出物理秩一致性（PRC）指标，衡量重构后动作局部物理距离排序的保留度，补充逐点精度之外的关系保真度评估维度
2. 提出ActionPiece分词框架，新增两类监督目标优化：物理秩保留监督约束编码器与量化后特征的近远距离排序，量化正则将相同排序约束作用于码本分配分布，两类目标结合重构损失共同优化，输出离散动作token供标准自回归策略学习
### 关键结果
相同Qwen3-VL-4B训练设置下，ActionPiece在LIBERO数据集准确率达94.8%，未见场景LIBERO-Plus达68.8%，SimplerEnv达71.9%，VLA-Arena L0-L2平均达51.5%，两个新增监督目标共同拉动PRC与策略成功率提升。

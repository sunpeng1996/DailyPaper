---
title: Enriching Sequential Recommendation with Graph Laplacian Positional Embeddings
title_zh: 利用图拉普拉斯位置嵌入增强序列推荐效果
authors:
- Ekaterina Trushkova
- Artur Gimranov
- Anton Lysenko
affiliations:
- HSE University
arxiv_id: '2609.31253'
url: https://arxiv.org/abs/2609.31253
pdf_url: https://arxiv.org/pdf/2609.31253
published: '2026-09-25'
collected: '2026-09-28'
category: RecSys
direction: 序列推荐 · 位置嵌入优化
tags:
- Sequential Recommendation
- Positional Embedding
- Graph Laplacian
- SASRec
- Spectral Embedding
one_liner: 用物品共现图拉普拉斯特征向量作为冻结位置嵌入替换SASRec可学习位置嵌入 提升序列推荐性能
practical_value: '- 序列推荐场景可复用轻量改造逻辑：无需修改Transformer骨干结构与训练目标，仅用离线预计算的物品共现图拉普拉斯特征向量替换原有可学习位置嵌入即可获得效果增益，改造成本极低

  - 适配冷启动场景：拉普拉斯位置嵌入是全局图结构导出的静态嵌入，新增用户无历史交互时也可复用预计算结果，不需要重新训练位置嵌入参数

  - 工程落地成本低：该方法不改变原有推理链路耗时，仅需增加离线图计算与特征预存步骤，可快速开展AB测试验证收益，无额外线上推理负担'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
现有基于Transformer的序列推荐模型（如SASRec）普遍依赖可学习序数位置嵌入编码用户交互顺序，未利用物品空间的全局结构信息，可学习嵌入在序列长度波动、新用户冷启动场景下泛化性较差。
### 方法关键点
1. 基于训练集用户交互数据构建全局物品共现图，计算其对称归一化拉普拉斯矩阵的特征向量，作为图结构导出的位置嵌入
2. 直接用上述预计算的冻结位置嵌入替换SASRec原生可学习位置嵌入，骨干模型结构、训练目标完全保持不变，无额外训练参数
### 关键结果
在4个公开序列推荐基准数据集上验证，该简单替换方案在绝大多数排序指标上优于原生SASRec，效果与性能更强的位置、时间编码基线持平

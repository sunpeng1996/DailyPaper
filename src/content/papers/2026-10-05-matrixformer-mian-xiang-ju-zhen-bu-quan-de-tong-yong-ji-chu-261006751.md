---
title: 'MatrixFormer: A Foundation Model for Matrix Completion'
title_zh: MatrixFormer：面向矩阵补全的通用基础模型
authors:
- Dwaipayan Saha
- Jacob Feitelberg
- Kyuseong Choi
- Raaz Dwivedi
- Anish Agarwal
affiliations:
- Columbia University
- Cornell Tech
arxiv_id: '2610.06751'
url: https://arxiv.org/abs/2610.06751
pdf_url: https://arxiv.org/pdf/2610.06751
published: '2026-10-05'
collected: '2026-10-06'
category: RecSys
direction: 通用矩阵补全 · 推荐评分预测
tags:
- MatrixCompletion
- Transformer
- SyntheticPretraining
- RecommenderSystem
- TabularImputation
one_liner: 提出合成数据预训练的轴向注意力Transformer，零样本跨场景高效矩阵补全，速度较基线提升超百倍
practical_value: '- 推荐系统冷启动/稀疏用户-物品矩阵补全场景，可直接复用预训练好的MatrixFormer-RecSys专家模型，零样本无需业务数据重训，降低评分预测误差

  - 高吞吐大尺寸矩阵补全任务可借鉴交替轴向注意力架构，相比逐条目预测的TabImpute有107×速度提升，大幅降低推理延迟

  - 多场景模型适配可复用其观测误差加权集成方案，基于业务观测数据自动拟合通用专家与场景专属专家的融合权重，无需微调预训练参数'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有表格基础模型做矩阵补全时采用逐条目预测范式，重复输入上下文、忽略矩阵二维结构，推理成本随矩阵尺寸激增；传统矩阵补全方法需针对每个新矩阵重新拟合参数，无法跨场景复用能力。
### 方法关键点
- 架构：采用交替轴向注意力机制，先在每行内跨列做特征注意力，再在每列内跨行做样本注意力，保留矩阵二维结构，引入行/列CLS token聚合全局信息
- 预训练：完全基于合成低秩、潜因子矩阵训练，覆盖MCAR/MAR/MNAR等多样缺失模式，新增尺寸扩展阶段适配最大2000×1000的矩阵输入
- 推理：单前向传播即可并行预测所有缺失条目，通过观测误差自适应融合通用Impute专家与推荐专属RecSys专家的预测结果
### 关键实验
零样本跨四类任务测试：1）推荐评分预测：MovieLens 100K RMSE 0.8874，Netflix小数据集RMSE 0.8617，均优于SVD等传统协同过滤基线；2）推理速度：1024×10矩阵补全速度比TabImpute快107×，仅需0.0389s；3）表格插补：UCI数据集NRMSE 0.998，优于ICE等8种基线；4）因果面板数据补全在5/6个测试集上取得最优结果。
### 核心结论
完全基于合成数据预训练的结构感知Transformer，可零样本跨场景实现高效矩阵补全，无需业务数据微调即可适配推荐等场景需求

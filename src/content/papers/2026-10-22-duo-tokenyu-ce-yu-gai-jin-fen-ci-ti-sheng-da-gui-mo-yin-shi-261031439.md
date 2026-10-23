---
title: Multi-Token Prediction and Alternative Tokenization Improve Learning Latent
  Multi-Hop Graph Search at Scale
title_zh: 多Token预测与改进分词提升大规模隐式多跳图搜索学习效果
authors:
- Arvid Frydenlund
- FuTe Wong
- Katherine Lambert
- Frank Rudzicz
affiliations:
- University of Toronto
- Vector Institute
- Manulife Applied AI Research
- Dalhousie University
arxiv_id: '2610.31439'
url: https://arxiv.org/abs/2610.31439
pdf_url: https://arxiv.org/pdf/2610.31439
published: '2026-10-22'
collected: '2026-10-23'
category: Reasoning
direction: 多跳推理 · 训练与分词优化
tags:
- Multi-hop Reasoning
- Multi-Token Prediction
- Tokenization
- Graph Search
- Training Objective
one_liner: 结合多Token预测与结构化分词方案，突破大规模隐式多跳图搜索的学习瓶颈
practical_value: '- 电商知识图谱多跳召回、用户意图推理类任务可替换NTP为MTP训练目标，提升样本效率，降低对数据拓扑分布的依赖

  - 商品关联图、用户行为图等结构输入的LLM任务可复用STAN结构化分词方案，消除位置嵌入引入的虚假关联，降低训练方差

  - 多跳推理任务训练时强制引入混合跳数采样（MMHT），避免模型锁定低难度样本损失为0导致的学习停滞，提升大尺度任务收敛率

  - 涉及结构输入的推理任务可在输入侧追加节点列表，无需修改模型架构即可大幅提升信息路由效率，降低推理错误率'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM在隐式多跳图搜索（如未知图最短路径生成）任务上存在明显scaling wall，图规模超过50节点时训练不稳定、难以收敛，核心原因被归结为next-token prediction（NTP）的监督信号不足和分词缺陷，但现有方法无法突破大尺度限制，且结论仅针对特定拓扑结构，无法泛化到通用多跳推理场景。

### 方法关键点
- 训练目标优化：基于Plackett-Luce损失实现multi-token prediction（MTP），从每个前缀位置预测后续所有路径节点，监督信号密度从NTP的线性提升为二次，隐式实现混合跳数训练（MMHT），效果不受图拓扑结构影响
- 输入优化1：在边列表后追加节点列表（+N），缓解因果LM的信息路由碎片化问题，无需修改模型结构即可提升信息聚合效率
- 输入优化2：提出结构化标注（STAN）分词，将每条边封装为单个super-token，用边标记替代位置嵌入，消除边顺序的虚假关联，同时将边列表序列长度压缩为原来的1/3

### 关键结果
在Erdős-Rényi图、欧几里得图、路径星图三类拓扑上测试，对比prefix LM基线：
1. 仅用STAN+N就能将50节点ER图的收敛速度提升3倍，且完全消除不同种子的训练方差
2. 搭配MTP后可稳定支持最大125节点的ER图、151节点的路径星图任务，收敛速度较NTP再提升50%，突破了此前50节点的scaling wall
3. 路径星图（NTP的对抗场景）上，MTP+STAN+N可将最大支持跳数从4提升到15，任务成功率达95%以上

### 核心结论
MTP对多跳推理任务的增益几乎不受拓扑结构影响，搭配结构化分词可在不提升模型规模的前提下突破多跳任务的scaling瓶颈

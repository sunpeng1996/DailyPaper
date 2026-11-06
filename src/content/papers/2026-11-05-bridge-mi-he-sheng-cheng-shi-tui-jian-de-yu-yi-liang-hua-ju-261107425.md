---
title: 'BRIDGE: Bridging the Semantic Quantization Gap for Generative Recommendation'
title_zh: BRIDGE：弥合生成式推荐的语义量化差距
authors:
- Yatong Xiao
- Mingjie Sun
- Peng Wang
- Wenjin Wu
- Peng Jiang
affiliations:
- Kuaishou Technology
arxiv_id: '2611.07425'
url: https://arxiv.org/abs/2611.07425
pdf_url: https://arxiv.org/pdf/2611.07425
published: '2026-11-05'
collected: '2026-11-06'
category: GenRec
direction: 生成式推荐 · 语义量化缺口优化
tags:
- Generative Recommendation
- Semantic ID
- RQ-VAE
- Knowledge Distillation
- Adaptive Computation
one_liner: 针对生成式推荐语义量化差距提出三个耦合机制，离线指标涨10%+，线上广告eCPM提0.65%
practical_value: '- 现有基于Semantic ID的生成式推荐链路可直接接入CGLR模块，将冻结的RQ-VAE码本聚类中心作为语义锚，提升首段高熵SID的预测准确率，减少错误级联

  - 训练阶段引入PESD机制，仅用预计算的item语义邻域信息作为特权信号生成软标签，无需额外标注即可缓解teacher forcing带来的曝光偏差

  - SID分层生成时采用EAR非均匀计算调度，给高难度的上层SID分配更多迭代次数，共享循环块权重不新增参数，同时提升推理QPS与效果

  - 该框架已在工业级电商广告场景验证有效，可直接在现有SID生成式召回链路做小流量AB测试，预期获得eCPM与QPS的双重收益'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前基于RQ-VAE生成Semantic ID（SID）的生成式推荐范式存在被普遍忽略的**语义量化差距（SQG）**：量化阶段用到的连续语义结构（码本中心、邻域几何关系、层级预测熵）在生成阶段完全丢失，仅给解码器输入离散ID，导致三大痛点：1）首段SID预测缺语义锚，错误易级联到所有下层；2）独热监督忽略item间语义相似度，加重曝光偏差；3）不同层级预测难度差异大但计算量均匀分配，资源错配影响效果。
### 方法关键点
- **码本锚定隐式推理（CGLR）**：SID生成前先执行推理阶段，用冻结的RQ-VAE一级码本聚类中心作为语义锚，约束隐层表征，解决grounding gap
- **特权EMA自蒸馏（PESD）**：EMA教师模型引入目标item的Top-K语义邻居嵌入作为特权信息，输出带邻域结构的软标签蒸馏给on-policy学生模型，缓解曝光偏差，解决neighborhood gap
- **感知难度的循环调度（EAR）**：对高熵的上层SID分配更多循环迭代次数，下层减少计算量，共享循环块权重不新增参数量，解决difficulty gap
### 关键结果
在Amazon Beauty/Sports/Toys三个公开数据集上，对比GR4AD、TIGER等SOTA生成式推荐基线，平均Recall@10提升10.9%、NDCG@10提升9.7%，最高分别达12.6%和10.7%；快手电商广告场景1周5%流量AB测试，eCPM提升0.65%，推理QPS提升20%。
### 核心结论
RQ-VAE的量化结构不是离线一次性工具，其隐含的语义层级、邻域、难度信息可以被复用为生成阶段的强归纳偏置，几乎无额外成本即可带来显著效果与效率提升。

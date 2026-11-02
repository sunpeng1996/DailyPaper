---
title: 'DAMI: Dual-Axis Memory Initialization for Enhanced Long-Context Retrieval
  in Gated Linear Attention'
title_zh: DAMI：双轴内存初始化提升门控线性注意力长上下文检索能力
authors:
- Zhangchi Feng
- Harry Jiang
- Yangyifei Luo
- Ray Zhang
- Richong Zhang
affiliations:
- SpeedAI
- Beihang University
arxiv_id: '2610.41994'
url: https://arxiv.org/abs/2610.41994
pdf_url: https://arxiv.org/pdf/2610.41994
published: '2026-10-30'
collected: '2026-11-02'
category: Training
direction: 长上下文SSM/线性注意力 初始化优化
tags:
- Long-Context
- Linear-Attention
- SSM
- Initialization
- Mamba
- RWKV
one_liner: 为5种门控线性注意力架构提供无参初始化方案，长上下文检索精度最高提升16.71pp
practical_value: '- 搭建基于Mamba/RWKV等线性注意力架构的长上下文RAG/Agent时，可直接复用DAMI初始化方案，无需新增参数即可提升远距信息召回准确率，落地无推理
  overhead

  - 推荐系统做长序列用户行为建模时，若用线性注意力/SSM降低计算成本，可借鉴双轴设计：head维度分配不同记忆时间尺度适配长短跨度行为，layer维度用低-高-低敏感度平衡长短期兴趣

  - 工程落地可复用小样本逐层校准的思路，仅用少量激活样本即可完成初始化参数适配，无需修改模型结构与推理逻辑，落地成本极低'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
线性注意力、SSM类架构推理复杂度为O(n)、KV cache固定大小，是长上下文大模型的主流选型，但其有限状态内存的衰减特性由A_log和dt_bias两个参数共同决定，实验发现训练后这两个参数与初始化值的皮尔逊相关系数高达0.87~0.99，初始化直接决定长上下文检索能力，现有单维度初始化方案未考虑两个参数的耦合效应，远距信息召回精度低。
### 方法关键点
- 双轴目标设计：head维度按几何间隔分配1~最大上下文长度的记忆时间尺度，覆盖不同距离的信息检索需求；layer维度采用低-高-低输入敏感度曲线，浅层低敏感度稳定token表示、中层高敏感度适配内容变化、深层低敏感度保留长期信息
- 数据驱动联合校准：预训练前用小批量校准样本逐层计算激活分布，先二分法求解dt_bias匹配层敏感度目标，再求解A_log匹配head时间尺度目标，全程无梯度、不新增可训练参数
- 跨架构适配：针对GDN、KDA、GDN2、Mamba-2、RWKV-7共5种主流架构做了适配，完全保留原生状态更新逻辑
### 关键实验
所有实验模型为100M参数，在5B tokens上训练，对比随机初始化、PoST单轴初始化两个baseline，在RULER NIAH长上下文检索基准上，DAMI平均精度提升5.29~16.71pp，其中KDA架构提升最高达16.71pp；语言建模、常识推理、2K真实场景检索性能与baseline持平无下降。
### 核心结论
门控线性注意力/SSM类架构的内存衰减参数训练后几乎不会偏离初始值，仅通过结构化初始化就能无成本提升长上下文检索能力，无需修改模型结构或增加训练开销。

---
title: 'Loopback Transformer: Towards a Unified View of Residual Looped Transformers'
title_zh: Loopback Transformer：残差循环Transformer的统一框架
authors:
- Xuan Ouyang
- Zefan Cai
- Chenlong Zhang
- Cheng Luo
- Ke Wan
- Junjie Hu
affiliations:
- University of Wisconsin–Madison
- University of California, Santa Barbara
- California Institute of Technology
- Microsoft
arxiv_id: '2611.07226'
url: https://arxiv.org/abs/2611.07226
pdf_url: https://arxiv.org/pdf/2611.07226
published: '2026-11-03'
collected: '2026-11-16'
category: LLM
direction: 大模型架构 · 循环Transformer参数优化
tags:
- Looped_Transformer
- Residual_Connection
- Parameter_Efficiency
- Transformer_Architecture
- LLM
one_liner: 基于残差深度内存视角设计循环Transformer，仅用40%-75%参数优于同计算量标准Transformer
practical_value: '- 垂域LLM/推荐序列建模模块可直接复用循环参数共享方案，在降低25%~60%参数的同时保持效果，适配端侧、低算力部署场景

  - 残差更新单独存储+几何衰减+内容注意力的权重分配逻辑，可迁移到用户行为序列建模，灵活控制不同周期行为的贡献，避免早期行为被稀释

  - 推理阶段无需重训即可增加循环次数的特性，可用于Agent迭代推理场景，动态调整推理深度匹配不同复杂度的任务需求'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
Looped Transformer通过参数共享大幅降低参数量，但传统残差设计无法灵活控制历史计算结果的复用权重：要么总更新权重随深度不断膨胀，要么原始输入与更新权重相互竞争，同时推理时增加循环次数容易出现「过思考」降质问题，亟需更合理的残差聚合机制。
### 方法关键点
- 提出深度内存视角，将残差连接类比为内存的写-传输-读过程，选择单独存储每个block的更新量而非完整输出，避免历史权重被重复加权
- 保留原始输入的独立通路，权重固定为1，与更新权重完全解耦，解决输入与更新竞争权重的问题
- 引入几何衰减给更新量设置近因先验，控制总更新权重不随循环次数无限增长，再通过注意力基于内容重分配更新权重，总权重保持不变
- 无需修改原有Transformer Block结构，仅调整残差聚合逻辑，迁移成本极低
### 关键实验
在ClimbMix预训练语料上，对比标准Transformer、Plain Loop、Hyperloop等7种循环残差设计，覆盖191M到3B共5个参数量级：
- 同等训练token和执行深度下，Loopback仅用标准Transformer 40%~75%的参数，验证损失更低，13个下游任务平均准确率最高，3B规模下数学题准确率从2.6%提升到6.4%
- 推理时支持增加最多2倍的循环次数，损失上涨幅度仅为普通循环Transformer的1/7~1/8，有效缓解过思考问题
### 核心结论
循环Transformer的效果上限，不仅取决于共享的Block本身，更取决于共享计算结果的存储和复用机制。

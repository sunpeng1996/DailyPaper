---
title: 'DAGFormer: Global Topology Prediction for Transformer Cross-Layer Connections'
title_zh: DAGFormer：面向Transformer跨层连接的全局拓扑预测
authors:
- Xiaocong Yang
- Yuren Hao
- ChengXiang Zhai
affiliations:
- University of Illinois Urbana-Champaign
arxiv_id: '2610.19625'
url: https://arxiv.org/abs/2610.19625
pdf_url: https://arxiv.org/pdf/2610.19625
published: '2026-10-13'
collected: '2026-10-19'
category: LLM
direction: LLM架构优化 · 动态跨层连接
tags:
- Transformer
- Dynamic Cross-Layer Connection
- Model Efficiency
- Pretraining
- Architecture Optimization
one_liner: 通过联合训练的全局拓扑预测器规划Transformer跨层连接，提升同等算力下模型性能
practical_value: '- 可借鉴「全局预规划+局部微调」的路由设计思路，优化推荐系统多塔/跨层特征融合架构，提升不同层级特征的传递效率

  - 同等参数规模下DAGFormer训练效率更高，可复用该架构训练电商/推荐垂直域小参数LLM，降低训练成本与部署门槛

  - 该架构结构化剪枝后性能衰减更慢，可用于端侧/边缘侧轻量LLM压缩，适配推荐场景端侧推理的低延迟要求'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有动态跨层连接的Transformer架构均采用层内局部路由决策，缺少全局拓扑视角的统一规划，无法实现跨层信息传递的全局最优调度，同等参数与算力投入下模型性能提升受限。
### 方法关键点
- 引入独立轻量拓扑预测器：仅输入原始token序列，通过2层小参数因果Transformer一次性预测主干网络所有层的跨层连接权重，输出Q/K/V/残差四个维度的加权矩阵
- 新增局部权重校正机制：每层内置零初始化的轻量微调网络，基于当前层输入对预测的全局连接权重做局部修正，兼顾全局规划合理性与局部计算适配性
- 兼容原生训练范式：初始化时连接权重默认仅读取上一层输出，训练初始状态与 vanilla Transformer 完全一致，无需额外适配即可复用现有训练管线
### 关键结果
- 基于OLMo-2 backbone在75M~1B参数规模下开展对比实验，训练数据为Dolma开源语料，基线覆盖 vanilla Transformer 及DenseFormer、hyper-conn等4种SOTA跨层路由架构
- WikiText-2困惑度比同规模 vanilla Transformer 低17%~25%，1B参数DAGFormer用5B token训练的效果超过 vanilla 模型用10B token训练的效果
- 13个下游任务平均准确率比 vanilla 高2.0~2.5个点，指令微调后AlpacaEval对 vanilla 的胜率达63%~70%，6种结构化剪枝场景下5种性能衰减幅度最小
### 核心结论
全局预规划+局部微调的动态跨层连接设计，可在仅增加少量训练开销的前提下显著提升Transformer的训练效率、下游性能与剪枝鲁棒性，是小参数LLM性能优化的高性价比方向

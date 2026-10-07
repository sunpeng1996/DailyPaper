---
title: 'HLA: Expressive Hybrid Linear Attention via Chunk-Wise Dynamic Mixing'
title_zh: HLA：基于分块动态混合的高表达性混合线性注意力
authors:
- Zhuokun Chen
- Xi Lin
- Xiyu Wu
- Jiahao He
- Jianfei Cai
- Bohan Zhuang
affiliations:
- Monash University
- Zhejiang University
arxiv_id: '2610.05842'
url: https://arxiv.org/abs/2610.05842
pdf_url: https://arxiv.org/pdf/2610.05842
published: '2026-10-04'
collected: '2026-10-07'
category: LLM
direction: 长上下文LLM · 线性注意力优化
tags:
- LinearAttention
- LongContext
- GDN
- EfficientInference
- AttentionOptimization
one_liner: 为Gated DeltaNet加入查询依赖的分块级注意力，低开销提升长上下文建模与泛化能力
practical_value: '- 长上下文Agent研发可复用HLA的「分块仿射状态+查询依赖路由」设计，在降低KV cache开销的同时提升历史稀疏信息（如对话记录、工具返回结果）的召回准确率，效果优于固定权重的分块混合方案

  - 生成式推荐场景下用GDN/Mamba类线性注意力建模超长用户行为序列时，可参考HLA的256token分块、32窗口池化的调优结论，平衡检索粒度和效率，历史状态存储比标准KV
  cache降低50%

  - 低算力场景的LLM长上下文适配可复用HLA的「冻结主干仅训练路由/池化模块」方案，适配成本极低，0.8B小模型在LongBench-V2上即可获得5.57个点的精度提升'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
线性注意力通过固定大小的循环状态实现高效长上下文自回归解码，避免KV cache随上下文长度膨胀，但现有方案存在两大痛点：一是早期存储的稀疏信息会随上下文增长被逐步衰减，二是固定分块混合权重无法适配不同查询的上下文依赖需求，导致长距离稀疏信息召回准确率低。

### 方法关键点
- 将GDN的循环更新拆解为分块级仿射状态转移，每个完整分块用(Aj,Bj)对表示，分别对应历史状态变换参数和新增记忆增量
- 对每个分块做窗口级自注意力池化得到路由代表向量，基于当前查询和代表向量的相似度计算sigmoid路由门控，推理时直接跳过门控值小于0.1的分块
- 路由门控通过插值历史分块仿射变换和单位矩阵，同时控制分块的新增记忆贡献和对更早状态的变换，加入有效支持正则鼓励路由权重集中，实现稀疏推理
- 预训练模型适配时冻结主干仅训练路由和池化模块，训练成本极低

### 关键结果
对比原生GDN、固定分块混合的MHLA baseline，在LongBench-V2、RULER长上下文基准测试：
- 预训练适配Qwen3.5全系列模型，0.8B规模下LongBench-V2相对GDN提升5.57pp，RULER提升3.97pp，解码开销仅增加18.8%
- 从零训练1.3B模型用4K上下文训练，推理可泛化到32K上下文，RULER得分相对GDN提升4.22pp
- 256token分块默认配置下，历史状态存储比标准KV cache降低50%

线性注意力的长上下文能力瓶颈不在于记忆容量，而在于查询依赖的稀疏历史信息访问机制，低开销的分块动态路由可在几乎不增加过多推理成本的前提下大幅提升长距离召回效果。

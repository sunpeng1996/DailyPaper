---
title: 'On the Design of Qwen3.8-Next Architecture: Evaluation, Efficiency, and Training
  Stability'
title_zh: Qwen3.8-Next架构设计：兼顾效果、效率与训练稳定性的MoE实践
authors:
- Zihan Qiu
- Zekun Wang
- Xiao Li
- Yanpeng Li
- Yang Xu
- Yixuan Wang
- Huaqing Zhang
- Rui Men
- Bochao Mao
- Chengruidong Zhang
affiliations:
- Qwen Team
arxiv_id: '2608.30320'
url: https://arxiv.org/abs/2608.30320
pdf_url: https://arxiv.org/pdf/2608.30320
published: '2026-08-30'
collected: '2026-09-01'
category: LLM
direction: 大语言模型架构 · MoE效率优化
tags:
- MoE
- SparseAttention
- GatedResidual
- NgramEmbedding
- TrainingStability
one_liner: 总参125B单token激活6B的MoE大模型，效果追平上代397B旗舰，训练FLOP仅为1/9
practical_value: '- 做长上下文Agent、超长用户行为序列建模的推荐/搜索业务，可复用QSA微块稀疏注意力设计，1M上下文下prefill提速7.6×、decode提速4.9×，几乎不损失效果

  - 训练大参数量LLM/推荐模型可复用Gated Residual设计，无需batch warmup，4倍最优学习率下无loss spike，训练稳定性大幅提升

  - 低延迟LLM推理场景（如电商实时文案生成、query推荐）可参考GDN+Attention分层混合token mixing设计，比SWA混合架构在7/9个基准上效果更优

  - 模型迭代不能仅看预训练loss，预训练loss与下游效果并不总是正相关，需结合业务下游指标做架构决策'
score: 9
source: huggingface-daily
depth: full_pdf
---

### 动机
现有大模型设计往往无法兼顾效果、训练/推理效率、训练稳定性三个维度，上代Qwen 397B旗舰计算成本过高，亟需在大幅降低计算开销的前提下保持同等效果水平。

### 方法关键点
- Token mixing采用分层混合架构：每4层中3层用Gated DeltaNet（GDN）线性压缩前缀降低计算量，1层用Qwen Sparse Attention（QSA），微块粒度索引将长序列索引复杂度从O(n²)降至O(n²/r)
- 残差流采用Gated Residual（GR）设计：扩展为4分支，通过元素级门控控制读写，移除跨分支混合算子降低内存开销，同时提升训练稳定性
- 新增n-gram嵌入层，表存储在主机内存异步预取，几乎不增加单token FLOP即可扩容模型容量
- 优化器采用Muon+AdamW组合：二维线性层用Muon，嵌入、MoE路由、GR低秩层用AdamW，最优学习率和batch size更高，无需batch warmup

### 关键结果
总参125B（单token激活6B）+51B offload的n-gram嵌入，14个预训练基准中8个领先上代397B旗舰，剩余6个最多低2.6个点，训练FLOP仅为上代1/9、训练token仅为1/3；4倍最优学习率下训练无loss spike，无需额外梯度裁剪。

### 核心结论
预训练loss和下游任务效果并不总是同向变化，模型架构设计必须同时评估效果、效率、稳定性三个维度，不能仅凭单一指标做决策。

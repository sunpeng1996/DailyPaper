---
title: 'Rethinking Semantic Alignment in LLM-Enhanced Collaborative Filtering: A Spectral
  Decoupling Approach'
title_zh: LLM增强协同过滤的语义对齐重思考：频谱解耦方法
authors:
- Yedong Jin
- Shaowen Peng
- Tsunenori Mine
- Shoko Wakamiya
- Eiji Aramaki
affiliations:
- Nara Institute of Science and Technology
- Kyushu University
arxiv_id: '2608.24363'
url: https://arxiv.org/abs/2608.24363
pdf_url: https://arxiv.org/pdf/2608.24363
published: '2026-08-25'
collected: '2026-08-26'
category: RecSys
direction: LLM增强协同过滤 · 频谱解耦
tags:
- Collaborative Filtering
- LLM4Rec
- Spectral Analysis
- Semantic Alignment
- Decoupled Fusion
one_liner: 提出无额外训练参数的预测层解耦框架UniSpecRec，高效融合协同与LLM语义信号，性能优于对齐式方案
practical_value: '- 现有LLM增强推荐可直接替换对齐式融合逻辑为预测层加权融合，无新增训练参数，计算开销低，可直接复用现有CF backbone与LLM
  embedding能力

  - 对预训练LLM输出的语义embedding做SVD后采用幂函数滤波（f(σ)=σ^p，p建议取0.1~0.6），可放大非主成分的有效信息，无需额外训练即可提升语义分支效果

  - 协同与语义分支的融合权重α可固定在0.3~0.4区间，无需逐场景复杂调参，即可在不同稀疏度的电商/内容推荐场景拿到接近最优的效果

  - 做LLM4Rec优化时不要强制对齐语义与协同空间，会丢失语义非主成分的有效信息，优先做信号独立处理后再融合'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有LLM增强协同过滤方案普遍将LLM生成的语义embedding通过投影层对齐到协同隐空间，会丢失语义信号中非主成分的有效信息，且对齐操作的必要性未得到验证，从频谱视角分析两类信号的分布差异可找到更高效的融合路径。
### 方法关键点
- 频谱分析验证：协同信号的有效信息集中在低频率主成分，而语义信号的非主成分同样包含大量推荐相关信息，对齐式训练会显著抑制语义非主成分的保留
- 提出UniSpecRec：两类信号独立在各自空间做专属频谱滤波，协同分支保留低通平滑成分，语义分支采用幂函数滤波放大非主成分贡献，仅在预测层做线性加权融合，无新增训练参数
- 架构兼容任意CF backbone，语义embedding的SVD为一次性离线操作，线上推理无额外overhead
### 关键结果
在Amazon Games、Toys、Books三个公开数据集上，对比LightGCN、AlphaRec、RLMRec等10+基线，采用LLaMA-3.2-3B作为语义编码器时，Recall@20相对最优交互基线SGFCF分别提升5.1%、15.3%、4.4%；推理速度比最快的对齐式基线AlphaRec快2.8~7.5倍，跨3款LLM编码器的性能波动比对齐方案低50%以上。
👉 最值得记住：LLM增强推荐无需强制语义到协同空间的对齐，预测层解耦融合既能保留全量语义信息，还能兼顾效率与效果

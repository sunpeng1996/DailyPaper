---
title: Cross-Lingual Alignment for Decoder-Only Models using MoE Routers
title_zh: 基于MoE路由器的Decoder-Only大模型跨语言对齐方法
authors:
- Lucas Bandarkar
- Clark Peng
- Ahmed Haj Ahmed
- Aditi Khandelwal
- Nanyun Peng
affiliations:
- University of California, Los Angeles
- Haverford College
- MILA - Quebec AI Institute
- McGill University
arxiv_id: '2610.01921'
url: https://arxiv.org/abs/2610.01921
pdf_url: https://arxiv.org/pdf/2610.01921
published: '2026-10-01'
collected: '2026-10-02'
category: Training
direction: LLM跨语言对齐 · MoE路由优化
tags:
- MoE
- Cross-Lingual Alignment
- Decoder-Only LLM
- Continual Pre-training
- KL Divergence
one_liner: 通过MoE中间层路由权重的对齐损失实现Decoder-Only大模型跨语言性能提升
practical_value: '- 跨境电商/多语种推荐场景下，可复用该对齐方案，用20万级平行语料对MoE推荐大模型做增量训练，即可提升小语种Query理解、商品推荐准确率，平均涨点接近1%

  - 多模态MoE模型做跨模态语义对齐时，可优先尝试路由权重均值池化作为对齐目标，比传统隐状态均值池化效果更稳定，避免特征抵消问题

  - MoE模型增量训练时，可复用文中的序列打包+源序列提前退出优化，将额外对齐损失的计算 overhead 控制在10%以内，无需大幅增加训练成本

  - 参数有限的场景下，可尝试仅更新MoE路由器参数（<0.1%参数量）即可实现接近全参数微调的对齐效果，适配小语种快速迭代需求'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
Decoder-Only大模型无天然序列级表示，传统跨语言对比学习无法直接适配，而多语种表示对齐程度直接决定小语种任务性能；现有基于隐状态均值池化的对齐方法存在特征抵消、噪声大的问题，无法满足MoE架构大模型的对齐需求。

### 方法关键点
- 基于跨语言路由 divergence 曲线筛选中间对齐层，仅在该层范围施加对齐损失，避免破坏模型语言特有能力
- 对平行语料的源/目标序列，先均值池化对应层的路由权重分布，再计算KL散度作为对齐损失，与LM损失加权后联合训练，仅回传目标序列梯度
- 采用源目标序列无Padding打包、源序列在对齐层后提前退出的优化，大幅降低对齐损失的计算开销

### 关键结果
在4个开源MoE模型、7个小语种的20万样本持续预训练实验中：
- 13/14个模型-语言对的下游任务平均得分优于纯LM训练基线，最高提升2.1个百分点，平均提升0.9个百分点
- 对比隐状态均值池化对齐方案，路由对齐在2个测试语种上分别多提升0.5、1.2个百分点，效果更稳定
- 仅更新路由器参数（占比<0.1%）时即可接近全参数训练的对齐效果，适合参数高效微调场景

### 核心结论
MoE路由权重是比隐状态更可靠的序列级表示，可作为跨语言、跨模态等对齐任务的优质目标。

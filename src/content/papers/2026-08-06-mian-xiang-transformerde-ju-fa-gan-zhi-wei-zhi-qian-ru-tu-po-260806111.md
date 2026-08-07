---
title: 'Beyond Sequence Order: Syntax-Informed Positional Embeddings for Transformers'
title_zh: 面向Transformer的句法感知位置嵌入：突破序列顺序限制
authors:
- Haris Riaz
- Hyungji Kim
- Mihai Surdeanu
affiliations:
- University of Arizona
arxiv_id: '2608.06111'
url: https://arxiv.org/abs/2608.06111
pdf_url: https://arxiv.org/pdf/2608.06111
published: '2026-08-06'
collected: '2026-08-07'
category: LLM
direction: LLM位置编码优化 · 句法先验注入
tags:
- Positional Embedding
- Transformer
- Syntax Inductive Bias
- SiPE
- Pretraining
one_liner: 提出兼容三类主流位置编码的轻量句法感知嵌入SiPE，不改动自注意力即可提升句法与下游任务表现
practical_value: '- 电商搜索/推荐场景的语义匹配、query理解小编码器（如RoBERTa、DeBERTa），可直接复用SiPE输入侧注入方案，仅新增千级参数即可提升语义理解准确率，无需改动原有模型架构，落地成本极低

  - Agent场景使用的轻量自回归解码器，可采用SiPE位置通路乘法注入方案，在仅增加一次轻量hexatagger预解析步骤的前提下，同时提升句法理解准确率、降低生成困惑度，减少Agent指令理解错误

  - 做领域预训练/适配时，可复用分架构选注入位点的结论：编码器优先选输入侧注入（效果稳定、实现简单），解码器优先选位置通路注入（收益最高），避免无效的架构调优'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
Transformer原生位置嵌入仅编码序列顺序，无法捕捉句法结构，导致语义理解、组合泛化能力不足；现有句法注入方案要么修改自Attention结构大幅提升推理成本，要么仅训练时注入句法信号推理时丢弃，效果和效率难以兼顾。

### 方法关键点
- 基于hexatagging将依存句法树转换为2类终端、5类非终端的离散标签，仅为每个词的第一个子词注入对应标签嵌入，新增参数量仅千级
- 完全兼容绝对、相对、旋转（RoPE）三类主流位置编码，无需修改自Attention、Transformer其他组件
- 分架构匹配最优注入策略：编码器直接将标签嵌入加到输入层，自回归解码器以乘法形式耦合到注意力的相对位置项，收益最高
- 训练时新增标签预测辅助损失，推理时仅需对单句做一次hexatag解析，无额外渐近计算开销

### 关键结果
在SyntaxGym、BLiMP（句法评估）、GLUE（下游任务）、BLLIP-LG（语言建模）数据集上验证，对比原生Transformer、TreeReg、TPT等基线：
- 自回归解码器Transformer-XL搭载SiPE后，SyntaxGym得分提升10.3%，困惑度下降9.0%，GLUE基准提升8.2%
- RoBERTa、DeBERTa、ModernBERT三类编码器搭载输入侧SiPE后，GLUE得分最高提升2.3%，OOD场景下增益进一步放大至最高4.21%

### 核心结论
轻量结构化先验注入位置通路的收益远高于复杂的自注意力结构修改，且可无缝适配所有主流Transformer架构。

---
title: 'UltraBERT: Beyond the Limit of BERT Pre-Training'
title_zh: UltraBERT：突破BERT预训练的性能上限
authors:
- Jungwoo Park
- Taewhoo Lee
- Jaewoo Kang
affiliations:
- Korea University
- AIGEN Sciences
- Amazon
arxiv_id: '2610.15028'
url: https://arxiv.org/abs/2610.15028
pdf_url: https://arxiv.org/pdf/2610.15028
published: '2026-10-09'
collected: '2026-10-14'
category: LLM
direction: 双向编码器预训练优化
tags:
- BERT
- Masked Language Modeling
- Knowledge Distillation
- Text Encoder
- Retrieval
- Classification
one_liner: 通过多掩码率混合、LM头解耦与差异化蒸馏，实现分类检索双SOTA的通用BERT编码器
practical_value: '- 训练业务场景的RAG/检索编码器时，可直接复用5%+50%掩码率4:1混合、LM头解耦的训练配方，不用分别训分类和检索两个独立模型，降低维护成本

  - 多任务训练出现梯度冲突时，可优先尝试输出头解耦方案，无需调整主干网络，适配电商推荐里点击/加购/收藏多目标预估、搜索里相关性/转化率多目标排序等场景

  - 垂直领域BERT预训练无需盲目堆训练token规模，1-2T token即可达到下游性能饱和，节省的算力可投入优化掩码策略、蒸馏策略等配方，ROI更高

  - 小规格编码器蒸馏时，仅对分类类任务（如语义匹配、意图识别）做蒸馏，检索类任务直接用原生MLM损失，可同时保留两类任务的最优性能'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有双向编码器的预训练配方仍沿用小数据时代的惯例，单掩码率的MLM目标导致模型只能在分类或检索单侧任务取得好效果，没有同时适配两类任务的通用强编码器；同时过往的缩放实验均在10B-100B小token规模下完成，编码器的真实性能上限、掩码率与任务的适配关系、蒸馏对不同任务的影响均不明确。

### 方法关键点
1. 大规模消融发现：BERT类编码器下游性能在1~2T token就饱和，继续加训练token无收益；低掩码率（3%~15%）适配分类任务，高掩码率（30%~50%）适配检索任务，和此前“大模型用更高掩码率”的结论相反；logit蒸馏仅对低掩码率的分类任务有增益，高掩码率的检索任务用蒸馏反而掉点。
2. 提出LM头解耦机制：同个batch内按4:1比例混合5%和50%掩码的样本，分别对接独立的LM头计算损失，避免梯度冲突。
3. 差异化蒸馏策略：仅对5%掩码的样本计算和1.3B教师模型的KL散度损失，50%掩码的样本用原生MLM损失，剪枝蒸馏得到380M、150M两个规格的UltraBERT，原生支持32K上下文。

### 关键结果
UltraBERT是首个同时在分类和检索任务取得SOTA的编码器：380M版本GLUE得分91.0，BEIR得分47.7；150M版本分类效果追平RoBERTa-large，参数量少2.3倍，检索效果超400M的Ettin-encoder，参数量小2.6倍；32K长上下文下LongEmbed指标领先所有同规模基线。

### 核心结论
双向编码器的任务特异性不是固有属性，通过优化预训练配方即可实现兼顾分类、检索的通用高性能编码器。

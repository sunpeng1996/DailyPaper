---
title: 'GRPO, Dr. GRPO, and DAPO Are Three Operations on One Number: The Group-Standard-Deviation
  Identity'
title_zh: GRPO、Dr.GRPO与DAPO的统一本质：基于组标准差的操作框架
authors:
- Yong Yi Bay
- Kathleen A. Yearick
affiliations:
- University of Illinois at Urbana-Champaign
arxiv_id: '2607.00152'
url: https://arxiv.org/abs/2607.00152
pdf_url: https://arxiv.org/pdf/2607.00152
published: '2026-06-30'
collected: '2026-07-02'
category: Training
direction: LLM RL训练 · GRPO系列方法优化
tags:
- GRPO
- RLVR
- LLM-training
- reward-normalization
- policy-optimization
one_liner: 证明GRPO、Dr.GRPO、DAPO三种LLM推理训练方法本质是对组奖励标准差的不同操作
practical_value: '- 做LLM驱动的Agent推理（比如电商智能导购、长尾query理解、个性化内容生成的RL对齐）时，可直接复用结论选择优化策略：需快速提升难样本效果选GRPO，需对齐整体业务准确率选Dr.GRPO，需节省训练算力选DAPO过滤σ=0的无效组

  - 工程上可基于组标准差σ做训练资源动态调度：对响应成功率p接近0或1的极难/极易样本，按公式G≳1/(8εp(1-p))分配采样次数，避免G=8/16的常规配置浪费算力，实测G=8时44%的组为无信号沉默组可直接过滤

  - 做二元奖励的RL对齐（比如推荐点击/未点击、广告转化/未转化、Agent回答正确/错误）时，可复用组标准差恒等式做梯度权重校准，无需额外引入critic即可估计每个样本的有效学习信号强度，降低训练复杂度'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
当前GRPO、Dr.GRPO、DAPO是LLM推理RL训练（RLVR）的三类主流方案，此前均被作为独立优化trick提出，底层逻辑不统一，从业者无法定量选择策略、调优参数，训练采样资源分配也缺乏理论依据。
### 方法关键点
- 推导二元奖励场景下的组标准差恒等式：单prompt的GRPO更新量严格等于组奖励标准差σ乘以正确与错误响应的得分差，其中σ=√(k(G−k))/G（k为G次采样中的正确答案数），当σ=0（全对/全错）时该组无任何有效学习信号
- 统一三类方法的底层差异：GRPO除以σ（优化方差稳定的arcsin√p目标）、Dr.GRPO移除σ除法（优化原始准确率p）、DAPO直接丢弃σ=0的沉默组（避免无效更新）
- 给出两个可直接落地的闭式公式：①组采样量公式G≳1/(8εp(1-p))，为不同难度样本分配达到梯度保真度1-ε所需的采样数；②沉默组概率公式p^G + (1-p)^G，可预先估算无效训练组的占比
### 关键结果
- 在21.56万条的Big-Math数据集上验证：GRPO相对Dr.GRPO，分配到极难/极易样本的梯度权重提升78%（13.9%→24.7%）
- 行业常用的G=8采样配置下，44%的采样组为无信号沉默组，即使提升到G=64仍有17%的沉默组
- 控制实验中，针对初始难度最高的25%样本，GRPO训练后最终准确率达0.99，Dr.GRPO仅为0.88，DAPO收敛最快但需要3.5倍的过采样开销

> 最值得记住的结论：GRPO系列方法的有效学习信号就是组内答案的分歧度，全对全错的样本组没有训练价值，统一采样数的配置会浪费大量算力在无信号样本上

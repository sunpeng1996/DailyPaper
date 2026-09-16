---
title: Self-Evolving Memory for Generative Recommendation
title_zh: 面向生成式推荐的自进化稀疏KV记忆框架LION
authors:
- Xinyu Lin
- Zhuosong Jiang
- Zixiao Suo
- Siqin Wang
- Hanqing Zeng
- Hanchao Yu
- Yinglong Xia
- Jiang Zhang
- Aashu Singh
- Fei Liu
affiliations:
- National University of Singapore
- Meta AI
arxiv_id: '2609.15598'
url: https://arxiv.org/abs/2609.15598
pdf_url: https://arxiv.org/pdf/2609.15598
published: '2026-09-14'
collected: '2026-09-16'
category: GenRec
direction: 生成式推荐 · 持续迭代优化
tags:
- Generative Recommendation
- Continual Learning
- KV Memory
- Sparse Activation
- Evolution Conflict
one_liner: 提出稀疏KV记忆层与巩固损失，解决生成式推荐持续迭代中的异质行为演化冲突问题
practical_value: '- 架构借鉴：可在生成式推荐Transformer中间层插入稀疏KV memory层，仅激活Top-K槽位做迭代更新，避免头部用户/热门商品梯度压制长尾，参数开销远低于用户级Adapter/LoRA，适合大规模部署

  - 优化trick：新增针对记忆输出的consolidation loss，仅在隔离的记忆空间施加监督，避免共享参数梯度冲突，长尾场景增益尤其显著，权重λ可在0.3~1.0范围调优适配不同业务分布

  - 工程实现：记忆激活的query可单独用用户全量行为序列计算，主干网络仅处理近期行为，兼顾长序列建模准确性与推理效率

  - 可复用结论：生成式推荐持续迭代时演化冲突真实存在，单纯全量微调/蒸馏会持续劣化长尾推荐效果，采用隔离式演化路径可同时兼顾头部与长尾性能'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
生成式推荐采用全共享参数空间做端到端item生成，在持续迭代适配流式用户行为时会出现演化冲突：活跃用户/热门行为的梯度会压制长尾用户/小众行为的更新，导致长尾推荐效果持续劣化，现有持续学习方案（重训、正则、蒸馏）均未解决异质行为在共享空间的梯度冲突问题。

### 方法关键点
- 架构设计：在Transformer中间插入稀疏KV memory层，基于用户表征相似度激活Top-K个记忆槽位，不同行为模式的更新被路由到不同参数空间，实现隔离式演化
- 优化策略：新增consolidation loss，直接监督记忆增强后的用户表征，为长尾小众行为提供更强梯度信号，避免其被头部梯度淹没
- 效率优化：记忆激活的query基于用户全量行为序列计算，主干网络仅处理近期行为序列，兼顾长程偏好建模与计算效率

### 关键结果
在Amazon Games、CDs、Toys三个真实数据集上对比7个主流基线，相比最优基线TIGER，LION的Recall@10分别提升29.8%、35.5%、15.6%，其中非活跃长尾用户的增益是活跃用户的2~3倍，梯度冲突降低90%以上，记忆规模缩减16倍时性能波动小于0.4%，参数开销远低于用户级个性化方案。

**最值得记住的一句话**：生成式推荐的持续迭代不能只依赖全量共享参数微调，通过稀疏记忆实现异质行为的隔离演化，是兼顾头部性能、长尾效果与迭代效率的可行路径。

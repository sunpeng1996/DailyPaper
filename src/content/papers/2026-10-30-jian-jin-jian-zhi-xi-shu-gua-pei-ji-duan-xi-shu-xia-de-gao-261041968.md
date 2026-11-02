---
title: 'Prune Gradually, Adapt Sparsely: Efficient Pruning of Large Language Models
  at Extreme Sparsity'
title_zh: 渐进剪枝+稀疏适配：极端稀疏下的高效大语言模型剪枝方法ETAPS
authors:
- Jean Lucien Randrianantenaina
- Hung Nguyen
- Nasib Ullah
- Jinbin Zhang
- Nilesh Gupta
- Inderjit S. Dhillon
- Rohit Babbar
affiliations:
- University of Bath
- Aalto University
- University of Texas at Austin
- Google
arxiv_id: '2610.41968'
url: https://arxiv.org/abs/2610.41968
pdf_url: https://arxiv.org/pdf/2610.41968
published: '2026-10-30'
collected: '2026-11-02'
category: Training
direction: 大语言模型压缩 · 极端稀疏剪枝
tags:
- LLM Pruning
- Sparse Fine-tuning
- Model Compression
- Efficient Inference
- Parameter Efficiency
one_liner: 提出ETAPS渐进剪枝框架，极端稀疏下效果超SOTA且内存降5倍、GPU耗时减49%
practical_value: '- 业务侧需在端侧/边缘节点部署小规格LLM做导购、文案生成、意图理解时，可直接使用ETAPS做90%+稀疏剪枝，单H200即可跑通7B模型，平衡效果与部署成本

  - 渐进式剪枝+小预算稀疏delta适配的思路可迁移到推荐系统大参数模型（双塔、多兴趣模型）压缩，无需全量微调即可在高压缩率下保留效果

  - 剪枝saliency打分可直接复用「权重大小×微批次平均绝对梯度」的组合规则，比纯权重大小的剪枝指标在高压缩率下效果提升显著

  - 做稀疏模型微调时可参考delta预算设置方法，用rank32 LoRA等价的参数量作为稀疏delta的固定预算，无需额外调参即可拿到不错效果'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
LLM部署推理成本高，极端稀疏（90%+参数剪枝）可大幅降低存储、减少推理延迟，但现有方案存在明显 trade-off：one-shot剪枝成本低但高稀疏下效果暴跌，SOTA方法ELSA效果好但需维护与模型同规模的优化器状态，内存开销极高，亟需平衡极端稀疏下的剪枝效果与成本。

### 方法关键点
- 渐进式剪枝调度：采用立方剪枝曲线分多阶段逐步提升稀疏率，避免一步剪到极端稀疏导致效果无法恢复；高稀疏阶段分配更长的适配时长，适配参数调整需求
- 稀疏delta适配：冻结原始预训练权重，仅训练固定小预算的稀疏delta（参数量等价于rank32 LoRA），优化器状态仅维护delta，大幅降低内存开销
- 梯度加权全局剪枝打分：每阶段适配时累计微批次的绝对梯度均值，与当前有效权重大小相乘作为剪枝重要性得分，全局选择保留参数，无需提前为各层分配稀疏率
- delta支持动态重分配：每轮剪枝后，delta的可训练位置会在当前保留参数中重新分配给梯度最大的坐标，提升适配效率

### 关键实验结果
在125M~70B共6类LLM上测试，对比Wanda、SparseGPT、ELSA等SOTA剪枝方法，指标采用WikiText-2/C4困惑度、下游零样本准确率：
- 50%~90%稀疏率下，困惑度比ELSA最高降低42%；90%~99%极端稀疏下，LLaMA-2-7B困惑度比ELSA低14%~25%
- 90%稀疏率下剪枝LLaMA-2-7B，仅需单张H200，持久状态内存比ELSA少5倍，GPU总耗时降低49%
- 可扩展到70B级大模型，90%稀疏下LLaMA-2-70B的C4困惑度仅为11.0

> 最值得记住的结论：极端稀疏剪枝无需全量优化整个模型，渐进式剪枝与小预算稀疏适配结合即可在大幅降低剪枝成本的同时拿到更优效果

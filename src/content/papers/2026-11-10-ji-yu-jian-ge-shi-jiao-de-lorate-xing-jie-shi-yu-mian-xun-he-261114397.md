---
title: 'A Margin Perspective on LoRA: Robustness to Catastrophic Forgetting and Adapter
  Merging (MaLoRA)'
title_zh: 基于间隔视角的LoRA特性解释与免训练合并方法MaLoRA
authors:
- Ziqing Xu
- Hancheng Min
- Lachlan Ewen MacDonald
- Salma Tarmoun
- Enrique Mallada
- Weijie Su
- Rene Vidal
affiliations:
- University of Pennsylvania
- Shanghai Jiao Tong University
- Johns Hopkins University
arxiv_id: '2611.14397'
url: https://arxiv.org/abs/2611.14397
pdf_url: https://arxiv.org/pdf/2611.14397
published: '2026-11-10'
collected: '2026-11-11'
category: Training
direction: 参数高效微调 · LoRA适配器合并
tags:
- LoRA
- Catastrophic Forgetting
- Adapter Merging
- Parameter Efficient Fine-tuning
- Max Margin
one_liner: 从间隔视角解释LoRA抗灾难性遗忘与适配器合并特性，提出免训练合并方法MaLoRA
practical_value: '- 电商多场景大模型微调时，可通过调整LoRA的L2正则/AdamW权重衰减平衡新垂类适配效果与通用场景效果保留，无需额外引入知识蒸馏即可降低灾难性遗忘风险

  - 多场景独立训练的LoRA适配器可直接采用MaLoRA方法合并，仅需计算各任务的平均分类间隔即可得到最优混合权重，无需重新训练，适配跨类目、跨地域的推荐模型快速部署需求

  - 合并适配器时仅需搜索1个全局缩放因子即可达到最优效果，相比网格搜索多任务混合系数的方案调参成本降低90%以上，适合大规模多LoRA的生产环境部署'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
LoRA是当前大模型参数高效微调的事实标准，除计算效率优势外，实践中还表现出两大核心特性：微调时对预训练能力的灾难性遗忘程度低、独立训练的多个适配器可直接合并为同时支持多任务的模型，但这两个特性长期缺乏统一的理论解释，现有适配器合并方法多为启发式设计，效果不稳定且调参成本高。
### 方法关键点
- 基于近正交任务假设下的多分类线性分类框架，分析带L2正则的LoRA优化目标，将最优适配器解按正则强度划分为三个区间：高正则区间适配器为0、中间正则区间最优适配器对齐微调数据的max-margin解、低正则区间适配器无闭式解
- 推导预训练、微调任务的归一化间隔闭式表达式，明确正则参数直接控制新任务适配度与旧能力遗忘的trade-off，给出平衡两类任务效果的最优正则值
- 推导多适配器合并的最优混合系数闭式解，提出免训练的MaLoRA合并算法：基于预训练模型与各适配器的任务平均分类间隔计算混合权重，仅需扫描1个全局缩放因子即可得到最优合并效果
### 关键实验
覆盖CIFAR-100、PACS等视觉数据集，以及MNLI、Amazon Reviews等NLP分类数据集，对比Soup、TA、TIES、DARE系列等6种主流适配器合并基线；MaLoRA取得93.32%的平均归一化准确率，相对精度损失仅6.68%，均为所有方法最优，额外计算开销仅2.35%。
### 核心结论
LoRA的抗遗忘与可合并性本质是正则约束下的分类间隔平衡效应，基于间隔的适配器合并无需训练即可超过多数启发式合并方法的效果。

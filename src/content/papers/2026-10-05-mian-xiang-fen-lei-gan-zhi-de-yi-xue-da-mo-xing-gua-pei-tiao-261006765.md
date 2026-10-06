---
title: Conditional Rank Allocation for Taxonomy-Aware Medical Language Model Adaptation
title_zh: 面向分类感知的医学大模型适配条件秩分配方法
authors:
- Guangyuan Dong
- Ziwei Hong
- Xuehao Zhou
- Zidong Yu
- Bingchen Liu
- Kehan Liu
- Chuang Liu
- Rong Fu
- Yuchao Hou
affiliations:
- National University of Singapore
- University of Pennsylvania
- Shandong University
- Syracuse University
- Shanghai Jiao Tong University School of Medicine
arxiv_id: '2610.06765'
url: https://arxiv.org/abs/2610.06765
pdf_url: https://arxiv.org/pdf/2610.06765
published: '2026-10-05'
collected: '2026-10-06'
category: Training
direction: 大模型参数高效微调 · 条件低秩适配
tags:
- LoRA
- Parameter-Efficient Fine-Tuning
- Conditional Routing
- Low-Rank Adaptation
- Domain Adaptation
one_liner: 提出ARBOR参数高效微调方法，基于分类标签动态选择低秩分量提升多场景医疗QA性能
practical_value: '- 多场景大模型适配可复用该思路，基于业务标签（如商品类目、用户分群、场景类型）动态选择LoRA分量，无需为每个场景单独训练LoRA权重，大幅降低存储和维护成本

  - 适配多类目电商/广告/搜索场景时，可引入类目、场景标签与query/用户表征的交互门控，提升不同垂类场景的模型效果，且支持随场景数量扩展持续放大增益

  - 共享低秩基+动态路由的架构可直接迁移到垂类Agent的模型微调，在几乎不增加推理耗时的前提下提升跨任务适配能力'
score: 7
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有LoRA等参数高效微调方法对所有输入采用固定低秩更新，无法适配多专科、多操作场景的差异化适配需求，多场景下存在明显效果上限。
### 方法关键点
1. 构建共享低秩基，为每个输入动态选择秩一分量组合，无需为每个场景单独训练适配权重
2. 设计加法门控融合query表征、分类标签、场景标签及三者交互，通过学习系数缩放Adapter残差
3. 理论证明正交等概率子任务下该方法可突破固定秩更新的效果瓶颈
### 关键结果
基于Qwen3-8B在4个医疗QA benchmark上平均准确率达69.69%，较LoRA r16、MoELoRA分别提升1.26、1.30pp；适配场景从1个扩展到7个专科时，相对LoRA的增益从0.08pp提升到1.94pp；原子聚类与专科标签的调整兰德指数达0.62，验证路由机制有效性

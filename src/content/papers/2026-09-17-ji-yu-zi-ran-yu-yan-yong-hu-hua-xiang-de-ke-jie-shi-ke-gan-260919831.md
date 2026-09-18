---
title: 'Reproducing Transparent and Scrutable Recommendations: Exploring Open-Weight
  Models via Natural-Language User Profiles'
title_zh: 基于自然语言用户画像的可解释可干预推荐系统复现研究
authors:
- Noah Mamié
- Laurin van den Bergh
affiliations:
- University of Zurich
arxiv_id: '2609.19831'
url: https://arxiv.org/abs/2609.19831
pdf_url: https://arxiv.org/pdf/2609.19831
published: '2026-09-17'
collected: '2026-09-18'
category: RecSys
direction: 生成式推荐 · 自然语言用户画像
tags:
- LLM4Rec
- Natural-Language-User-Profile
- Reproducibility
- Interpretability
- Recommender-System
one_liner: 复现UPR推荐框架，验证自然语言画像透明性并揭示回归目标对干预效果的限制
practical_value: '- 做电商可解释推荐时可直接复用UPR两阶段架构：先从用户评价生成自然语言画像，再基于画像+商品元数据打分，天然支持用户手动编辑偏好调整推荐

  - 业务中要实现有效的用户可干预推荐，不要用评分回归作为训练目标，必须替换为带负采样的排序目标，否则仅能整体偏移打分不会改变商品排序

  - 复现算法实验可参考本文工程方案：用uv锁依赖、统一基线与LLM评估协议、修正验证集/测试集混用问题，大幅提升复现稳定性

  - 做LLM推荐的可解释性分析时，可复用nnsight探针+UMAP可视化的方案，定位模型内部表征与外部行为的对齐问题'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
传统推荐系统的用户隐向量不可解释，用户无法手动干预推荐结果，2024年提出的UPR框架用自然语言用户画像解决该问题，但原工作存在可复现性不足、干预效果机制不明确的问题，需要系统复现并扩展验证。

### 方法关键点
- 完整复现UPR两阶段流程：第一阶段用Llama2-7B/Mistral-7B将用户历史评论生成自然语言用户画像，第二阶段微调序列分类模型，输入画像+物品元数据预测评分
- 扩展3组验证实验：上下文消融（3种用户表征×2种物品表征）、5随机种子鲁棒性测试、基于nnsight的反事实画像扰动可解释性分析
- 统一所有基线和LLM的评估协议，修复原代码的语法错误、依赖缺失、测试集验证集混用问题，提供全链路可复现代码库

### 关键实验
在Amazon Movies&TV、TripAdvisor数据集上对比MostPop、UserKNN、MF等基线：UPR在TripAdvisor上nDCG@10达0.961、MAP达0.939，性能接近最优MF基线；自然语言画像的推荐效果（nDCG@10 0.929）与全量原始评论（0.926）相当，但prompt长度大幅缩短；5种子实验指标方差极低（σ_MAP=0.0009），性能稳定；反事实实验显示回归目标训练的UPR修改画像仅能整体偏移评分，无法改变排序，排序目标的WMF模型个性化能力（百分位0.806）远高于UPR（0.510-0.542）。

### 核心结论
基于评分回归目标训练的自然语言用户画像推荐，仅能实现评分整体偏移无法改变排序，要实现有效的用户可干预推荐必须使用带负采样的排序训练目标。

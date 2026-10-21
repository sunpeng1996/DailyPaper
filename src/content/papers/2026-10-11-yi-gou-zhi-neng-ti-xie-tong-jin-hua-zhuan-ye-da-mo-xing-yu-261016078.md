---
title: Heterogeneous Agentic Coevolution
title_zh: 《异构智能体协同进化：专业大模型与LLM Agent双向优化框架》
authors:
- Wenqian Ye
- Ziwei Guan
- Zi Yang
- Shivani Modi
- Cici Cong Wu
- Yunlong He
- Yuxin Chen
- Zhengyu Zhang
- Liang Luo
- Venkatesh Ranganathan
affiliations:
- Meta AI
- University of Virginia
arxiv_id: '2610.16078'
url: https://arxiv.org/abs/2610.16078
pdf_url: https://arxiv.org/pdf/2610.16078
published: '2026-10-11'
collected: '2026-10-21'
category: Agent
direction: Agent 异构协同进化优化
tags:
- Heterogeneous Coevolution
- LLM Agent
- Specialized Foundation Model
- Reciprocal Learning
- Recommendation System
one_liner: 提出异构Agent协同进化框架HACE，实现专业基础模型与LLM Agent双向迭代性能突破
practical_value: '- 推荐系统训练到收敛后，可引入轻量LLM Agent做样本选择指导，基于Agent探索结果筛选高价值训练样本，进一步提升排序指标，实验显示可提升HR@10最高18.5%

  - 可复用HACE的双向验证机制：用当前专业模型的性能作为Agent贡献的奖励信号，Agent的优质输出反过来补充专业模型的训练集，避免人工设计迭代规则的成本

  - 模型融合阶段可采用「专业模型分数+λ*Agent排序分数」的加权融合策略，λ通过交叉验证自适应选择，兼顾专业模型的泛化性和Agent的探索收益

  - 算力有限的场景下不需要盲目选用最大参数的Agent，实验显示中等尺寸Agent（Gemma4-E4B）协同进化的收益远大于超大参数Agent'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
领域专用基础模型（如推荐系统的SASRec、HSTU）完成监督训练收敛后，常规训练手段无法进一步提升性能，需人工投入大量成本迭代特征、算法架构；现有自进化系统多固定LLM参数，无法适配专业模型的能力迭代，两者的进步无法互相复用。

### 方法关键点
- 核心框架包含三类组件：专业基础模型（Specialist）、LLM Agent、自适应交互Harness
- 双向互惠学习机制：Agent输出需超过当前Specialist的性能才会被验证通过，作为Agent强化自训练的监督信号；Agent的探索结果筛选出高价值训练样本，供Specialist做监督微调
- 进化搜索动态优化交互Harness：自适应调整信息传递规则、训练样本选择策略，适配两者不同进化阶段的交互需求
- 联合验证准入：每轮迭代只有Specialist+Harness的联合性能超过上一轮才会被保留，确保进化方向正向

### 关键实验
覆盖推荐、蛋白质功能预测、材料发现三个领域，推荐领域测试MovieLens 1M、4个Amazon品类数据集，对比ReST-EM、Meta-Harness等6种主流自进化方法：推荐任务HR@10相对基线平均提升12.1%，最高提升18.5%；蛋白质预测任务NDCG相对基线提升7.3%，远超其他方法最高0.6%的提升幅度。

### 核心结论
已经收敛的领域专业模型不需要推倒重来重训，通过与LLM Agent的双向协同进化即可突破性能天花板，且无需新增大规模标注数据。

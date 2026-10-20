---
title: Where is Physical RSI capability from? An Observational Scaling Law of LLM-as-policy
title_zh: 物理递归自提升能力来源：LLM作为策略的观测缩放定律
authors:
- Zekai Li
- Jiayi Yu
- Jinlu Zhang
- Luyang Niu
- Zekun Qi
- Jun Zheng
- Xuchuan Chen
- Dairu Liu
- Yintianrun Zhang
- He Wang
affiliations:
- Galbot Team
arxiv_id: '2610.26848'
url: https://arxiv.org/abs/2610.26848
pdf_url: https://arxiv.org/pdf/2610.26848
published: '2026-10-18'
collected: '2026-10-20'
category: Agent
direction: 具身LLM Agent · 自提升评估与缩放
tags:
- LLM Agent
- Embodied AI
- Scaling Law
- Self-Improvement
- Evaluation
one_liner: 提出五维物理RSI评估框架PhysRSI-eval，验证木桶假说并给出观测缩放规律
practical_value: '- 可复用五维评估框架做业务Agent自迭代效果评估：拆初始表现、提升效率、成功率、资源消耗、失败改进5个维度，替代单一终点指标，适合推荐系统调优Agent、电商客服Agent、运营Agent的效果度量

  - 物理木桶假说可迁移到业务Agent优化：先定位当前瓶颈再补能力，不要盲目堆某一项能力（如仅优化coding/推理能力无法弥补感知/空间推理短板），比如推荐系统query理解瓶颈若为场景感知，补语义匹配能力收益有限

  - 可复用「早期表现预测后期性能」方法：比如新推荐模型/策略上线时，用前几轮小流量AB测试数据预测长期效果，减少试错成本和流量损耗

  - 可复用自迭代经验沉淀机制：支持Agent把高频操作沉淀成可复用的工具/规则库，跨场景/跨任务迁移，提升电商运营Agent、商品上架Agent等的迭代效率'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前具身LLM Agent的物理递归自提升（RSI）能力缺乏系统性量化评估，单一终点得分无法区分初始能力、提升效率、资源消耗等关键差异，也无法判断提升是场景过拟合还是可迁移经验沉淀，难以支撑规模化的Agent能力优化。

### 方法关键点
- 提出PhysRSI-eval评估框架，固定模型权重和物理交互预算，跟踪跨轮次持久工作空间（代码、工具、笔记）的迭代变化
- 设计五维评估指标：首次尝试表现、提升效率、最终成功率、物理预算节省率、失败改进率，覆盖自提升的全链路特征
- 提出物理木桶假说：不同维度的自提升表现对应独立的能力瓶颈，单一能力强无法补全短板
- 从两个维度研究观测缩放规律：用公共基准能力预测不同模型的物理表现排序、用早期交互反馈预测后续提升轨迹
- 通过工作空间移除、冻结、跨任务迁移三类消融实验，验证自提升的泛化性

### 关键结果
在18个难度分层的RoboDojo双臂操作任务上评估6个主流VLM系统：空间推理能力与初始表现相关性ρ=0.94，感知能力与最终成功率、失败改进率相关性ρ=0.94，编码能力与所有维度相关性ρ≤0.37；移除历史工作空间后Agent后期成功率从41.7%降至8.3%，冻结工作空间在未见布局下仍有41.7%的成功率，跨任务迁移工作空间可让首次成功轮次最多提前8轮。

**最值得记住的一句话**：物理自提升的高最终得分、早增益、低交互成本三者不一定同时出现，不同能力维度存在独立瓶颈，不可用单一指标评估自提升Agent。

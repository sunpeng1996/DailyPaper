---
title: A foundation model of numerical intelligence with cross-disciplinary generalization
title_zh: 具备跨学科泛化能力的数值智能基础模型
authors:
- Chenghan Wu
- Zongmin Yu
- Liu Yang
affiliations:
- Department of Mathematics, National University of Singapore
arxiv_id: '2607.28432'
url: https://arxiv.org/abs/2607.28432
pdf_url: https://arxiv.org/pdf/2607.28432
published: '2026-07-30'
collected: '2026-08-01'
category: LLM
direction: 数值基础模型 · 跨学科泛化
tags:
- Foundation Model
- In-context Learning
- Graph Neural Network
- Cross-domain Generalization
- Numerical Intelligence
one_liner: 统一上下文算子网络UNICON无需重训即可跨学科实现逼近乃至超越领域专家的数值预测性能
practical_value: '- 可复用「上下文示例推理共性预测关系」的思路，优化推荐系统跨域冷启动预测效果，无需针对新领域重训大模型

  - 参考训练语料多样性提升跨域泛化性的结论，构建推荐系统多场景混合训练数据集，显著降低新场景冷启动成本

  - 可将UNICON作为数值预测模块接入LLM Agent链路，优化电商流量预测、销量预估、库存调度等数值类任务的跨场景性能'
score: 7
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有大模型的上下文学习能力多局限于文本场景，科学、社会系统及电商等商业场景需要能从数值上下文自主学习推理的数值智能能力，传统领域专属模型泛化性差，跨领域/跨场景需要重新训练，成本极高。
### 方法关键点
UNified In-Context Operator Networks（UNICON）数值基础模型以目标系统的图结构样本为上下文，自动推理样本间共享的预测关系，直接应用于同系统的查询任务，无需额外微调，支持与LLM Agent串联进一步提升性能。
### 关键结果
- 跨科学、社会系统（含训练阶段未覆盖的学科）无需重训即可逼近领域专属专家模型性能
- 与LLM Agent结合后，在训练未见过的学科任务上性能超越当前SOTA专家模型
- 训练语料的领域多样性越高，模型对未知领域的泛化性能越好

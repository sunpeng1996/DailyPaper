---
title: Sharpening Tax in Post-Training
title_zh: 大语言模型后训练过程中的锐化税度量与优化方法
authors:
- Changdae Oh
- Qi Zeng
- Qi Qi
- Andrey Zhmoginov
- Deren Lei
- Yun He
- Hoang Phan
- Hangoo Kang
- Azalia Mirhoseini
- Sharon Li
affiliations:
- Meta Superintelligence Labs
- University of Wisconsin–Madison
- New York University
- Stanford University
arxiv_id: '2610.01509'
url: https://arxiv.org/abs/2610.01509
pdf_url: https://arxiv.org/pdf/2610.01509
published: '2026-09-30'
collected: '2026-10-02'
category: Agent
direction: Agent 后训练性能权衡优化
tags:
- LLM
- Post-training
- RLHF
- Agent
- Sampling
- Evaluation
one_liner: 提出量化后训练覆盖度损失的Sharpening Tax指标，及PTGS方法兼顾Agent任务准确率与覆盖度
practical_value: '- 电商Agent工具调用、营销文案多候选生成等场景，可给预训练基模型搭配轻量prompt harness，在采样预算充足时获得比对齐后模型更高的解覆盖度，满足多样性需求

  - 可引入Sharpening Tax作为LLM对齐后的补充评估指标，仅需8次rollout即可预测长期覆盖度损失，平衡业务对单轮响应准确率和多候选多样性的诉求

  - 做LLM Agent策略RL微调（如导购Agent、推荐系统偏好对齐）时，可复用PTGS自适应采样方法，根据任务难度动态调整温度，同时提升pass@1和pass@K，避免策略坍缩'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM后训练（RL、DPO等）被普遍认为可解锁Agent多轮交互、工具调用等新能力，但此前仅在数学、编码任务观察到后训练存在「提升单轮准确率、损失解覆盖度」的tradeoff，该规律是否适用于预训练数据中少见的Agent任务尚不明确，且缺乏量化该损失的通用指标与优化方案。
### 方法关键点
- 提出**Sharpening Tax**：通过计算基模型与后训练模型pass@K曲线下的可扩展性面积差，量化后训练带来的测试时多采样增益损失，分为原始税TaxA和校准准确率后TaxS，仅需少量rollout即可估计。
- 提出**后验调温组采样（PTGS）**：基于Beta分布在线估计每个prompt的任务难度，难prompt升温鼓励探索、易prompt降温保证准确率，可即插即用接入PPO、GRPO等RL算法，无需修改原有更新逻辑。
### 关键结果
在BFCL v4、WebShop、ACEBench三个Agent基准，覆盖4个模型系列14组基/后训练模型对共42组测试中，36组场景下TaxS(128)为正，即后训练普遍存在覆盖度损失；仅需8次rollout的TaxS(8)即可预测32次rollout的TaxS(32)，斯皮尔曼相关系数达0.85。PTGS相比固定温度RL基线，pass@1最高提升14.6%，pass@128最高提升17.2%，Sharpening Tax最高降低69%。

最值得记住的结论：后训练主要提升模型解的可靠性而非可解决任务的边界，大模型规模下锐化税的成本会快速升高，需同时关注单轮准确率和多采样下的覆盖度。

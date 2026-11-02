---
title: 'R^2Orch: Recursive Self-Improvement for Agent Orchestration via Self-Play
  within a Skill-Internalization Loop'
title_zh: R²Orch：基于自博弈技能内化循环的Agent编排递归自改进框架
authors:
- Mingda Zhang
- Yun Huang
- Qiang Huang
- Yanjin Li
- Rui Qian
- Qichao Zhao
- Tiesunlong Shen
- Na Zhao
- Jian Wang
- Xiaoying Tang
affiliations:
- The Chinese University of Hong Kong, Shenzhen
- Fudan University
- University of Illinois Urbana-Champaign
- Tsinghua University
- National University of Singapore
arxiv_id: '2610.22740'
url: https://arxiv.org/abs/2610.22740
pdf_url: https://arxiv.org/pdf/2610.22740
published: '2026-10-21'
collected: '2026-11-02'
category: Agent
direction: Agent 编排自改进 · 自博弈
tags:
- Self-Play
- Agent Orchestration
- Skill Internalization
- Recursive Improvement
- RL
one_liner: 嵌套自博弈与技能退出双循环，实现无手工标注的Agent编排递归自改进
practical_value: '- 电商/导购Agent编排可直接复用双循环架构：内循环自博弈生成训练任务省去人工标注成本，外循环技能退出逐步移除prompt中的技能依赖，降低推理时token开销、缩短响应延迟

  - 做LLM/Agent RL训练可借鉴Recursive Learnability任务筛选trick：优先选择移除候选技能后rollout结果仍有差异的任务，避免GRPO优势崩溃，提升训练样本利用率

  - 企业内部Agent技能库管理可复用Skill Withdrawal评估方法：同一rollout组内随机隐藏待评估技能做对照，无额外开销即可判断技能是否可退休，避免技能库漂移'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有Agent编排学习依赖手工设计训练课程，GRPO等组式RL易出现优势崩溃（同任务所有rollout结果一致时无学习信号），技能评估依赖单一噪声分数易漂移，同时推理时需要携带大量技能prompt，成本高、泛化性差。

### 方法关键点
- 嵌套双循环架构：内循环为Proposer-Director自博弈，Proposer自动选择训练任务，Director学习生成Agent执行图；外循环为技能退出循环，逐步移除Director依赖的技能，最终实现零技能部署
- 递归可学习性目标：奖励Proposer选择移除候选技能后rollout结果仍存在差异的任务，避免优势崩溃，保证训练全程有充足学习信号
- 技能退出机制：同一rollout组随机拆分，部分隐藏待评估技能，通过两组结果的贝叶斯后验对比判断技能是否可移除，无额外推理开销，评估结果无偏
- 训练闭环：任务失败案例蒸馏为新技能，技能逐步内化到模型参数，技能退出后Proposer自动挖掘新的难例任务，形成自增强循环

### 关键实验
在12个基准数据集（问答、数学、代码、交互任务）上测试，零技能部署下R²Orch全面优于所有基线，IID任务平均准确率89.79%，OOD任务平均78.79%，对比之前SOTA的PATS方法平均提升3.79个百分点；训练好的Director无需重训可直接迁移到6种不同的Worker大模型，弱模型性能提升最多20个百分点。

最值得记住的一句话：Agent的自改进不需要依赖外部标注数据，通过自博弈+技能内化的双循环设计，就能在降低推理成本的同时实现性能持续提升。

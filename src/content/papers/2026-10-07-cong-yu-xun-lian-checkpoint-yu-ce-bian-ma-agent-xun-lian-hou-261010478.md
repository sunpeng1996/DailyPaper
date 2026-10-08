---
title: 'Before They Can Solve: Predicting Post-Training Coding-Agent Performance from
  Base Models'
title_zh: 从预训练 checkpoint 预测编码 Agent 训练后性能的高效评估框架
authors:
- Tan Yu
- Alexander Bukharin
- Khushi Bhardwaj
- Jennifer Williams
- Zirui Liu
- Jonathan Lingjie Li
- Soumye Singhal
- Joseph Jennings
- Sanjeev Satheesh
- Yash Jain
affiliations:
- NVIDIA
- University of Minnesota – Twin Cities
- University of California, Berkeley
arxiv_id: '2610.10478'
url: https://arxiv.org/abs/2610.10478
pdf_url: https://arxiv.org/pdf/2610.10478
published: '2026-10-07'
collected: '2026-10-08'
category: Agent
direction: Agent 预训练 checkpoint 潜力评估
tags:
- Agent Evaluation
- Base Model Probing
- Coding Agent
- Post-training Prediction
- LLM Probing
one_liner: 提出基于成功Agent轨迹决定性步骤的三类探测方法，高相关性预测编码Agent训练后性能
practical_value: '- 做电商/推荐领域Agent底座选型时，可复用「决定性步骤探测」思路：拿到同领域成功Agent轨迹后，仅在关键决策点做少量探测即可快速排序底座，无需全量SFT/RLHF，大幅降低选型算力成本

  - 多步决策类Agent离线评估可复用「轨迹重放+关键决策点验证」框架：不用全量跑端到端仿真，仅验证核心决策点的正确性即可预判上线效果，提升评估效率

  - 构造MCQ类评估数据集时，需给每个选项做可执行的业务校验（如推荐场景校验选项对应的真实转化率），避免无效问题导致评估偏差，这一点从论文审计APTBench的缺陷可得到印证'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
编码Agent底座选型需先投入大量算力完成训练、端到端测试，成本极高；传统端到端Agent评估对未训练的底座模型难度过大（pass@K接近0），单步编码任务评估又和训练后Agent性能相关性极低（如HumanEval的Spearman ρ仅为-0.394），无法支撑高效选型。
### 方法关键点
- 基于coverage原则设计：优秀底座会给训练后可收敛的优质行为分配足够概率质量，无需底座具备完整Agent交互能力
- 重放前沿Agent的成功轨迹，通过任务自带验证器定位**决定性步骤T***：首个让任务从失败切换为成功的动作点，仅在该点做探测
- 三类互补探测维度：① Decisive-Action BPB：底座给黄金动作分配的字节归一化负对数似然，越低越好；② Patch MCQ：底座从验证器筛选的正负动作中选对正确动作的准确率；③ 前缀条件pass@K：底座在T*前缀下采样K次生成动作的通过率
- 工程优化：计算BPB时屏蔽聊天模板格式化token，消除格式偏好干扰；MCQ用循环打乱选项顺序消除位置偏差
### 关键结果
在10组公开底座+对应训练后Agent对上验证，以SWE-bench Verified pass@1为训练后性能真值：
- DeepSWE轨迹的Decisive-Action BPB与真值Spearman ρ达0.964，Patch MCQ达0.867，前缀条件pass@16达0.952，远超最强传统基线RepoBench XFirst的0.830
- 所有探测方法的相关性都远高于传统单步编码基准
### 核心结论
评估底座的Agent潜力不需要让它跑通完整端到端交互，只要验证它在关键决策点上对正确行为的概率覆盖度即可

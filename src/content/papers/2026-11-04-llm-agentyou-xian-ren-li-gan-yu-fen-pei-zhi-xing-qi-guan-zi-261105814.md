---
title: 'Learning When Human Decisions Matter: Executor-Relative Consultation Value
  for LLM Agents'
title_zh: LLM Agent有限人力干预分配：执行器关联咨询价值学习方法
authors:
- Shuli Jiang
- Khushbu Pahwa
- Yuting Zhang
- Yi Zhang
- Wei Xia
- Stefano Soatto
affiliations:
- AWS Agentic AI
arxiv_id: '2611.05814'
url: https://arxiv.org/abs/2611.05814
pdf_url: https://arxiv.org/pdf/2611.05814
published: '2026-11-04'
collected: '2026-11-05'
category: Agent
direction: Agent 人力干预调度优化
tags:
- LLM Agent
- Human-in-the-loop
- Value Distillation
- Budget Allocation
- Monte Carlo Rollout
one_liner: 通过离线蒸馏蒙特卡洛执行器滚出的咨询价值，实现有限人力预算下的低开销最优分配
practical_value: '- 电商客服Agent、推荐系统主动偏好询访场景可直接复用CVD框架：离线用业务执行器滚出不同咨询点的效用增益，蒸馏为轻量预测器，上线无实时rollout开销，人力利用率最高提升132%

  - 存在多咨询点互补/冗余的场景（如用户偏好多轮询问、商家资质校验节点选择），可采用排列不变的集合价值模型建模关联，比独立打分基线效果提升显著

  - 线上高并发场景可采用贪心+单次交换的局部搜索做近似分配，可还原90%~100%的最优分配效果，大幅降低推理延迟

  - 执行器迭代（如替换下游大模型/策略）时，优先测试跨执行器迁移能力，特征结构相似的任务可复用旧标注数据，减少90%以上的新标注成本'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
LLM Agent落地规模快速扩张，但人力咨询/审核产能无法匹配其处理效率，传统干预选择方法未考虑不同执行器对人力输入的利用能力差异，也无法处理咨询点互补冗余、顺序决策机会成本等问题，缺乏低成本的有限人力预算最优分配落地方案。
### 方法关键点
- 提出Consultation Value Distillation (CVD) 框架：离线采样不同咨询组合，通过Monte Carlo执行器滚出获得对应下游效用，蒸馏为轻量预测器，部署阶段无需实时rollout
- 批量场景采用基于DeepSets的排列不变集合价值模型，直接预测整组咨询价值，自动捕捉咨询点间的互补性与冗余性
- 顺序场景采用延续性感知预测器，同时计算当前咨询增益与剩余预算留到后续使用的机会成本，支持动态分配
- 采用小模型集成提升预测鲁棒性，部署阶段支持贪心+局部搜索的近似分配，大幅降低搜索开销
### 关键结果
覆盖6类任务、2个SOTA执行器（Sonnet 5、GPT-6.1 Sol）测试，对比Prompt、Value of Information (VoI)、独立打分Local Value基线：批量Animals任务归一化增益达0.58，是Local Value的2.32倍、VoI的11.6倍；顺序TB-H任务归一化增益达0.91，较Local Value提升13.75%；仅需10%训练滚出样本即可保留90%以上性能，贪心+局部搜索近似分配与最优枚举匹配度达90%~100%。

人力干预的价值不由决策本身的重要性决定，而由下游执行器利用该人力输入提升最终效用的潜力决定。

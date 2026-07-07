---
title: 'LLM-as-a-Verifier: A General-Purpose Verification Framework'
title_zh: LLM-as-a-Verifier：通用跨域智能体验证框架
authors:
- Jacky Kwok
- Shulu Li
- Pranav Atreya
- Yuejiang Liu
- Yixing Jiang
- Chelsea Finn
- Marco Pavone
- Ion Stoica
- Azalia Mirhoseini
affiliations:
- Stanford University
- UC Berkeley
- NVIDIA Research
arxiv_id: '2607.05391'
url: https://arxiv.org/abs/2607.05391
pdf_url: https://arxiv.org/pdf/2607.05391
published: '2026-07-05'
collected: '2026-07-07'
category: Agent
direction: Agent 通用跨域验证框架优化
tags:
- LLM-as-a-Verifier
- Agent Verification
- Reward Model
- Test-time Scaling
- Reinforcement Learning
one_liner: 无需额外训练的概率式LLM验证框架，跨多领域取得SOTA验证效果
practical_value: '- 做电商智能导购、运营Agent等Agent类应用的效果验证时，可复用基于评分token logits期望的连续打分方法，替代传统离散LM
  judge，大幅降低候选结果平局率，提升排序准确率

  - 面对广告文案择优、推荐策略候选池选优等多候选排序场景，可使用Probabilistic Pivot Tournament算法，将比较成本从O(N²)降到O(Nk²)，在有限预算下实现更高择优精度

  - 做RL优化的推荐/广告策略时，可将该框架输出的细粒度验证信号作为稠密奖励，提升SAC、GRPO等算法的样本效率，减少训练步数需求

  - 长流程电商Agent（如售后自动处理Agent、用户旅程运营Agent）可复用该框架的任务进度估算能力，实现异常轨迹的实时监测与提前拦截'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM生成能力已随预训练、后训练、测试时计算三大缩放轴持续提升，但验证环节能力长期滞后：传统离散LM Judge打分粗糙、复杂候选平局率高达27%，训练得到的奖励模型泛化性差、跨域适配成本高，无法释放best-of-N采样带来的潜在性能提升（如Terminal-Bench V2 oracle Pass@5可达92.1%，但传统选优器无法接近该上限）。
### 方法关键点
- 连续概率打分：不取最高概率的离散评分token，直接计算所有评分token logits的加权期望得到[0,1]区间连续分数，彻底消除平局
- 三维度缩放验证能力：提升评分token粒度（最高20级）增强区分度、重复多次评估降低方差、拆解评估标准为多个子维度减少偏差，三者协同提升准确率
- 概率Pivot锦标赛（PPT）排序：通过环形初筛消去位置偏置，选top-k候选作为pivot后仅比较非pivot与pivot、pivot间的配对，将排序成本从O(N²)降至O(Nk²)
### 关键结果
无需额外训练，跨领域取得SOTA：Terminal-Bench V2准确率86.5%、SWE-Bench Verified 78.2%、RoboRewardBench偏好准确率87.4%、MedAgentBench 73.3%；作为稠密RL奖励时，机器人任务样本效率提升1.8倍，数学推理任务提升1.1倍；任务进度估算Spearman相关系数最高达0.966。
最值得记住的结论：验证是LLM性能提升的第四大独立缩放轴，其收益可超过单纯缩放模型参数

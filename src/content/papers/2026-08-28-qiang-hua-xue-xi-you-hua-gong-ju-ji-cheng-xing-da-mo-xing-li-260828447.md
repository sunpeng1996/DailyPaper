---
title: 'Learning to Use Tools: Reinforcement Learning for Tool-Integrated Mathematical
  Reasoning'
title_zh: 强化学习优化工具集成型大模型数学推理能力
authors:
- Minghui Xu
- Zi Wang
affiliations:
- Stanford University
arxiv_id: '2608.28447'
url: https://arxiv.org/abs/2608.28447
pdf_url: https://arxiv.org/pdf/2608.28447
published: '2026-08-28'
collected: '2026-08-31'
category: Agent
direction: LLM工具调用 · 强化学习推理优化
tags:
- Tool Use
- Reinforcement Learning
- Mathematical Reasoning
- DAPO
- GRPO
- RLOO
one_liner: 对比4种RL算法优化工具集成数学推理，Tool-DAPO将pass@1从35.8%提升至66.0%
practical_value: '- 电商Agent涉及数值计算类任务（如优惠算价、库存校验、ROI预估）时，可复用本文的工具集成流程：先基于历史错误样本构造带工具调用的SFT数据集，再用RL微调，低成本降低算术错误率

  - 对结果可自动校验的任务，优先选用DAPO算法：其动态过滤全对/全错采样组的机制，可提升训练效率，本文中100步Tool-DAPO效果优于200步Tool-RLOO，训练耗时减少61%

  - RL优化工具调用能力时，可把「工具调用频次」作为训练过程的监控指标，本文发现RL训练过程中工具调用频次与任务准确率正相关，可快速判断训练是否收敛'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
LLM在多步数值推理场景下易出现算术错误，仅靠SFT训练工具调用无法充分优化工具调用时机与合理性；现有Countdown数学推理任务公共测试集仅50条样本，评估噪声大，缺乏不同RL算法在工具集成推理场景下的系统性对比基准。

### 方法关键点
- 工具集成SFT数据集构造：遍历原始SFT样本的错误类型，在算术错误位置插入`<tool>`计算器调用标签及`<obs>`返回结果，结合参考模型生成的正确后续推理，生成标准化工具调用训练样本
- 对比4种on-policy RL算法：RLOO、RLOO++、GRPO、DAPO，仅以最终答案正确性作为奖励信号，RL训练时仅对模型生成的非工具返回部分计算损失，避免干扰工具调用格式学习
- 构造1024条无训练集重叠的Countdown测试集，消除数据泄露影响，降低评估噪声

### 关键结果
在1024条新测试集上：工具集成直接将无工具SFT的pass@1从26.4%提升至35.8%；Tool-DAPO效果最优，pass@1从Tool-SFT的35.8%提升至66.0%，较Tool-RLOO高9.3个百分点，且100步训练耗时仅为200步Tool-RLOO的39%。

### 核心结论
RL优化工具调用的收益主要来自提升已有正确推理轨迹的采样概率，当采样组内无正确轨迹时几乎无法获得优化信号，难例问题需结合更强的搜索机制解决。

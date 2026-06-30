---
title: 'AsyncOPD: How Stale Can On-Policy Distillation Be?'
title_zh: AsyncOPD：异步on-policy蒸馏能容忍多大的stale数据
authors:
- Wonjun Kang
- Kevin Galim
- Seunghyuk Oh
- Minjun Kang
- Sanghyun Park
- Donghoon Kim
- Minjae Lee
- Minseo Kim
- Rishabh Tiwari
- Yuchen Zeng
affiliations:
- FuriosaAI
- Ajou University
- UC Berkeley
- Microsoft Research
- KRAFTON
arxiv_id: '2606.24143'
url: https://arxiv.org/abs/2606.24143
pdf_url: https://arxiv.org/pdf/2606.24143
published: '2026-06-22'
collected: '2026-06-30'
category: Training
direction: LLM 蒸馏 · 异步训练优化
tags:
- On-policy distillation
- Asynchronous Training
- LLM Post-training
- Knowledge Distillation
- Stale Data
one_liner: 系统研究异步on-policy蒸馏的stale问题，提出AsyncOPD训练pipeline，提速同时保精度
practical_value: '- 做LLM后训练（Agent微调、推荐大模型对齐等场景），若要异步训练提吞吐量，优先选择forward KL目标，其对stale数据的鲁棒性远优于reverse
  KL

  - 反向KL场景下，无需复用复杂的异步RL稳定方法，「更新阶段用当前学生重算优势项+不加PPO裁剪」的简单方案效果更好，工程成本更低

  - 缓存teacher打分时，多样本蒙特卡洛采样优于稀疏top-k缓存，既保持无偏性，又降低方差，避免了top-k的支持不匹配问题

  - 全异步流式调度比固定步偏移的step-off调度进一步提升硬件利用率，吞吐量可再提50%以上，精度无明显下降'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：On-policy蒸馏(OPD)是LLM后训练推理能力的主流方案，和RL一样存在同步训练系统瓶颈：生成长rollout耗时久，训练端常闲置等待。异步训练解耦rollout生成与模型更新可提升硬件利用率，但会引入stale策略数据；现有研究未系统分析OPD场景下stale数据的影响，尤其实际场景中全词表teacher logit存储传输成本过高，只能用有限teacher打分缓存，该约束下的stale问题缺乏研究。

**方法关键点**：
1. KL方向决定stale鲁棒性：forward KL是teacher加权，对stale rollout更鲁棒；reverse KL是学生加权，当前学生动作容易落在缓存teacher打分范围外，精度退化更快
2. 反向KL场景验证：复杂异步RL稳定方法（Decoupled PPO、M2PO等）不优于「learner更新时用当前学生重算token级优势+不裁剪」的简单方案
3. 缓存优化：稀疏top-k缓存的stale支持存在不可修复的偏差，单样本MC无偏但方差高，多样本MC每个步缓存多个旧策略采样，保持无偏性同时降低方差
4. 设计全异步流式AsyncOPD pipeline，无需等待整批rollout完成，进一步提升阶段重叠率

**关键结果**：基于Qwen3系列模型在过滤后的DeepMath数据集训练，在AIME24/25、AMC测试，对比同步训练，AsyncOPD提升训练吞吐量1.6×~3.8×，最终精度与同步训练相当。

最值得记住的结论：异步OPD的stale问题可以用简单设计解决，无需引入复杂的RL优化方法

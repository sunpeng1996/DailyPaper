---
title: What Makes a Social Agent's Interactions Effective? Learning from Verifiable
  Outcomes in Paired Worlds
title_zh: 社交Agent交互有效性评估：基于配对场景可验证结果的学习方法
authors:
- Caixin Kang
- Ke Wang
- Yuchuan Wu
- Xiaoqiang Wang
- Ling Li
- Bingxue Qiu
- Yongbin Li
- Yoichi Sato
affiliations:
- Alibaba Group
- The University of Tokyo
arxiv_id: '2610.20195'
url: https://arxiv.org/abs/2610.20195
pdf_url: https://arxiv.org/pdf/2610.20195
published: '2026-10-13'
collected: '2026-10-15'
category: Agent
direction: Agent 社交交互评估与强化学习优化
tags:
- Social Agent
- RL
- Benchmark
- Credit Assignment
- LLM Evaluation
one_liner: 提出社交Agent交互验证基准HICO-Bench与配对信用优化算法PaCPO提升可验证交互成功率
practical_value: '- 电商客服、协商类Agent评估可复用「规则校验方案可行性+LLM校验对话支撑性」的双层逻辑，替代纯LLM对话打分，解决现有评估高估效果的问题

  - 训练交互类Agent时，可复用PaCPO的配对场景信用分配思路，仅需终端奖励即可完成逐轮信用分配，无需额外标注逐轮反馈，降低训练数据成本

  - 构造交互类Agent测试集时，可参考配对场景（仅单关键私有条件不同）的设计，快速定位模型对关键信息的感知、适配缺陷'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有社交Agent评估仅依赖LLM对对话本身的打分，不校验最终达成的方案是否符合双方私有约束（如预算、时间、权限），大量高评分对话实际无法落地；同时RL训练交互Agent时，仅能获得对话结束后的终端奖励，无法精准分配到单轮交互，信用分配难度高。
### 方法关键点
- 搭建HICO-Bench基准：包含180个日常协调场景（资源分配、权限审批、调度等6类），每个场景设2个仅单私有条件不同的配对世界，正确方案完全不重叠；核心指标Verified Success需同时通过**规则校验的Feasibility**（双方记录的方案一致且满足所有约束）、**LLM校验的Integrity**（对话内容支撑达成的方案）
- 提出Paired-Credit Policy Optimization（PaCPO）算法：每轮交互后探测Agent当前的暂定方案，跨配对世界校验方案适配性，按适配度将终端奖励重分配到对应轮次，不改变单条对话的总奖励值
### 关键实验
- 13款LLM基准测试显示，36%Goal评分≥8/10的对话未通过Verified Success，现有评估高估了Agent的交互能力
- 基于Qwen3-8B训练，相同训练数据量下，PaCPO将Verified Success从20.4%提升至28.3%，优于PPO（25.0%）、GRPO（26.3%）等基线方法
### 核心结论
社交交互的有效性不能只看对话流畅度，必须同时校验最终方案的可行性以及对话对方案的支撑性

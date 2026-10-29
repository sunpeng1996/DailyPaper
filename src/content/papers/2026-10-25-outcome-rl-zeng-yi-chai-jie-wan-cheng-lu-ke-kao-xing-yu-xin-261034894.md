---
title: 'What Outcome RL Buys: Finishing, Reliability, Rarely Reach'
title_zh: Outcome RL 增益拆解：完成率、可靠性与新问题覆盖能力
authors:
- Shan Yang
affiliations:
- Independent Researcher
arxiv_id: '2610.34894'
url: https://arxiv.org/abs/2610.34894
pdf_url: https://arxiv.org/pdf/2610.34894
published: '2026-10-25'
collected: '2026-10-29'
category: Training
direction: 大模型训练 · Outcome RL 效果拆解
tags:
- Outcome RL
- Reasoning LLM
- pass@1
- Reinforcement Learning
- Model Evaluation
one_liner: 将Outcome RL的pass@1增益拆为三类，证明其几乎不会带来基准模型没有的推理能力
practical_value: '- 用RL优化电商/推荐场景的Agent决策、query改写等任务时，不要预期RL能学到基准模型没有的新知识，优先优化现有能力的触发率和输出效率

  - 评估RL微调后的模型效果必须绑定token budget，同时上报完成率fin@1和准确率pass@1，避免把输出变短的增益误判为能力提升

  - 低延迟业务场景下如果token预算紧张，可通过Outcome RL强制模型缩短输出，能快速提升固定预算下的任务完成率

  - 若需要模型解决基准模型完全不会的新问题，优先做SFT注入知识，Outcome RL无法带来跨问题的新知识迁移'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有Outcome RL训练的推理模型只上报pass@1增益，无法区分增益是来自新增推理知识还是行为优化，也未剥离token budget的干扰，业界一直不清楚RL训练到底能带来什么实际价值，甚至存在「RL能让模型学会新推理能力」的误解。
### 方法关键点
- 将固定token预算下的pass@1增益精确拆为三个独立维度：Finishing（预算内完成输出的比例提升）、Reliability（完成输出后答案正确的比例提升）、Reach（解决基准模型8次采样全错的新问题的净增益）
- 覆盖20个1.5B~32B的开源RL推理模型，对应匹配其基准思维模型，在物理、竞赛数学两个数据集上对比，每个问题采样8次，同时测试训练时的token cap和更高预算下的表现
- 补充受控实验：给8B模型喂物理题的前置解题知识，验证RL能否将注入的知识迁移到未见过的问题上
### 关键结果
- token预算紧张（4k/8k）时，82%的pass@1增益来自Finishing，给基准模型增加token配额就能追平大部分差距
- 当基准模型在预算内完成率≥90%时，增益全部来自Reliability，且RL用到的正确解题步骤100%在基准模型的采样中出现过，只是RL提升了正确步骤的触发稳定性
- Reach的净增益最高仅2.1个百分点，96.5%的RL独解问题要么是采样误差，要么是答案格式匹配问题，无实际新增推理能力
### 核心结论
Outcome RL本质是优化模型的行为模式（输出长度、正确步骤触发率），不会生成基准模型没有的新知识，不要用它解决基准模型完全不会的问题

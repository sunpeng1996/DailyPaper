---
title: 'From RLVR to RLSVR: Task Transformation Induces Self-Verifiable Rewards for
  Open-Ended LLM Self-Improvement'
title_zh: 从RLVR到RLSVR：基于任务转换的开放域LLM自验证自提升
authors:
- Qinsi Wang
- Jing Shi
- Huazheng Wang
- Kun Wan
- Yiran Wu
- Bo Liu
- Qingyun Wu
- Hai Helen Li
- Yiran Chen
- Handong Zhao
affiliations:
- Duke University
- Adobe Inc.
- Oregon State University
- Pennsylvania State University
- Amazon
arxiv_id: '2607.23802'
url: https://arxiv.org/abs/2607.23802
pdf_url: https://arxiv.org/pdf/2607.23802
published: '2026-07-25'
collected: '2026-08-03'
category: Training
direction: LLM自提升 · 自验证强化学习
tags:
- RLVR
- RLSVR
- Self-Play
- LLM-Self-Improvement
- Reinforcement-Learning
one_liner: 提出RLSVR自训练范式及SpyRL实例，实现开放域LLM无需外部评审的自提升
practical_value: '- 电商商品卖点生成、评价摘要等生成式文案场景可复用SpyRL框架：给部分Agent截断商品/评价信息作为spy，通过多Agent投票识别spy的方式自动生成质量奖励，无需额外训练奖励模型或调用大模型评审，大幅降本

  - 多Agent自玩训练可复用交替优化策略：固定执行端更新检测端、固定检测端更新执行端，避免同时更新导致的训练不稳定，同时引入角色优势估计（RAE）校准不同信息权限的Agent奖励偏差，提升训练效果

  - 主观生成任务的质量评估可参考信息不对称投票机制：无需人工标注，通过多输出投票排名间接衡量生成质量，可用于商品文案、营销内容自动化A/B测试的粗筛环节'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
RLVR仅能在数学、代码等有确定性验证规则的领域实现LLM可扩展强化学习训练，开放域生成任务（摘要、创意写作等）依赖RLHF、LLM-as-Judge等方式获取奖励，存在评估偏差、评审能力瓶颈、推理成本高的问题，亟需无需外部标注/评审的自监督式RL训练范式。

### 方法关键点
- 提出RLSVR范式，借鉴自监督学习pretext任务思路，将开放域原任务转换为可验证的代理环境，通过环境注入的潜变量自动生成自验证奖励，无需外部评审
- 实例化SpyRL框架，模仿「谁是卧底」游戏：每轮设置n-1个拥有完整输入的平民Agent、1个拥有截断/退化输入的卧底Agent，所有Agent执行相同目标任务后互相投票识别卧底
- 两阶段耦合优化：检测端奖励基于投票是否命中预设卧底直接计算（完全可验证），执行端奖励与收到的怀疑票数负相关，交替固定一端更新另一端，加入角色优势估计校准不同角色的奖励偏差

### 关键结果
- 在摘要、创意写作两个开放域任务上，基于Qwen3-8B的SpyRL相对基线获得75.4%、77.3%的GPT-4o pairwise win率，在数学推理任务上相对基线分别提升8.97%（4B）、6.16%（8B）的准确率
- 人工评估显示SpyRL在创意写作任务上相对基线整体win率达80%以上，投票数与GPT-4o质量排名强正相关，训练成本比基于GPT-4o的rubric奖励方案低900美元以上

### 核心结论
可验证性并非任务的固有属性，可通过合理的任务转换人工构造，从而实现开放域任务无需外部评审的规模化自提升

---
title: Language-model groups overstate consensus when replaying human deliberation
  on a reasoning task
title_zh: 复刻人类推理任务审议时，大语言模型群体存在共识高估偏差
authors:
- Tengfei Shao
affiliations:
- Waseda University
arxiv_id: '2609.20543'
url: https://arxiv.org/abs/2609.20543
pdf_url: https://arxiv.org/pdf/2609.20543
published: '2026-09-17'
collected: '2026-09-18'
category: Agent
direction: 多Agent模拟人类审议的偏差验证
tags:
- LLM Agent
- Collective Deliberation
- Consensus Bias
- Human Simulation
- MultiAgent
one_liner: 通过Wason推理任务对照实验，证实LLM智能体群体模拟人类审议时存在显著共识高估偏差
practical_value: '- 做营销受众调研、用户偏好模拟类多Agent实验时，不能直接用LLM群体共识作为人类共识参考，需根据任务类型对共识率做打折校准，推理模式可按5-6折校准，chat模式按6-7折校准

  - 搭建多Agent协作决策系统（如广告策略评审团、推荐规则迭代群议）时，需增加多样性约束：给Agent添加角色保真prompt降低趋同性，或强制保留少数派意见输出，避免推理模式下的过早收敛甚至错误共识

  - 做舆情仿真、用户评论生成等需要还原人类意见分布的场景时，要给Agent增加「潜水（不发言）」逻辑、限制信念迁移速率，避免输出的意见分布过度趋同，不符合真实人类行为

  - 用Agent替代人类做决策评估时，必须拆分正确共识和错误共识，不能将共识率等同于准确率，非标准化任务中高共识反而可能对应高错误率'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前越来越多场景用LLM Agent群体模拟人类审议、社会实验、群体决策，但现有验证仅关注群体均值匹配，忽略了意见分布、共识结构的还原度，高共识是否符合人类真实行为缺乏严格对照，易导致模拟结果失真甚至误导决策。

### 方法关键点
- 信念锚定设计：每个Agent对应真实人类参与者的讨论前答案初始化，屏蔽LLM自带任务能力的干扰，仅测试审议过程的行为还原度
- 多维度控制变量：对比DeepSeek的chat/推理两种模式、3种角色锚定脚手架（无提示/角色保真提示/每轮重注初始信念）、3种种子，加入Qwen3-14B做跨模型鲁棒性验证
- 同规则评分：人类与Agent群体用完全相同的代码计算共识率、准确率，排除度量偏差
- 鲁棒性对照：设置禁用提前停止、任务同构重映射（移除可记忆的标准答案）、隐藏peer消息三类对照实验

### 关键结果
基于DeliData公开的100组人类Wason推理任务讨论数据测试，人类共识率按不同度量在24.0%~57.0%之间；参与匹配的无潜水组中，人类共识率为51.1%，chat模式Agent共识率85.2%、推理模式95.6%，分别高出34.1、44.4个百分点；移除标准答案后推理模式Agent近100%达成共识，但74%的共识是错误答案；跨模型验证Qwen3-14B也存在41.7个百分点的共识高估。

### 核心结论
LLM Agent群体的高共识既不等于集体准确率，也不等于人类真实的共识水平，未经验证的Agent共识不能替代人类真实审议结果。

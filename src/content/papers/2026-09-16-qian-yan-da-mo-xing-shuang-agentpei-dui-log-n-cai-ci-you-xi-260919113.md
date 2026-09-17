---
title: 'Playing log(N)-Questions over Wikipedia Abstracts: Communication Efficiency
  Between Paired Frontier Models'
title_zh: 前沿大模型双Agent配对log(N)猜词游戏的通信效率评估
authors:
- Peter Potash
arxiv_id: '2609.19113'
url: https://arxiv.org/abs/2609.19113
pdf_url: https://arxiv.org/pdf/2609.19113
published: '2026-09-16'
collected: '2026-09-17'
category: Eval
direction: 双Agent通信 · 大模型能力评测
tags:
- MultiAgent
- LLM Evaluation
- Long Context
- Communication Efficiency
- Zero-shot Coordination
one_liner: 通过双Agent yes/no猜文档任务评测6款前沿大模型的自通信与长上下文能力
practical_value: '- 可复用双同模型Agent配对任务作为LLM4Rec系统的模块一致性测试：比如用户偏好理解Agent与推荐文案生成Agent的语义对齐测试，快速定位跨模块语义偏差

  - 平衡分区最大化信息增益的结论可直接用于对话式推荐提问策略设计：每次交互提问尽量均分候选商品集，最低限度降低交互轮次提升转化率

  - 推理token消耗与效果弱相关的结论可用于业务成本优化：相同效果下优先选择低推理消耗的模型/算力档位，无需盲目堆推理预算

  - 长上下文内容过滤的二分定位法可直接复用：电商场景拼接多商品描述、用户长行为序列时，快速定位触发过滤的敏感片段，降低链路故障率'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有长上下文评测多聚焦检索类任务，无法衡量大模型在不对称上下文下的跨实例自通信能力，也难以量化多步推理、全局语义聚合的综合表现；同时同模型双Agent零样本协作的失败原因缺乏低成本可解释的拆解方法。
### 方法关键点
- 设计log₂(N)轮yes/no猜文档游戏：提问方获取N篇维基百科摘要，回答方仅可见目标文档和当前问题，提问方需在固定轮次内猜对目标，同模型同时扮演两个角色
- 创新O(1)复杂度错误拆解机制：仅需裁判标注目标文档和最终猜测的问答一致性，即可将损失分为回答错误、候选区分失败、最终预测错误三类
- 严格配对对照设计：所有模型使用完全相同的文档集、目标和提示词，排除数据差异干扰
### 关键结果
- 评测6款前沿大模型共408场游戏，总成本363美元：Kimi K3、Gemini 3.8 Flash等5款模型胜率66%~82%，Claude Opus 5仅41%，排名与通用能力榜完全反转
- 前五款模型胜率随log₂(N)线性下降，相关系数r=-0.973，仅用单轮可靠性参数p=0.928即可拟合跨3个量级数据集的表现
- 错误拆分显示51%损失来自回答对齐错误，46%来自分区不足未区分候选，仅3%来自最终预测错误；单轮信息熵与胜率相关系数r=+0.88，推理token消耗与性能相关系数r=-0.05，成本与性能无相关性
### 核心结论
大模型多Agent协作的失败97%来自通信对齐问题而非推理能力不足，优先优化跨Agent语义一致性比提升单模型推理能力收益更高。

---
title: 'Critical-State RL: Diagnosing Trainable States for Multi-Turn Tool Use'
title_zh: 关键状态强化学习：为多轮工具使用定位可训练决策节点
authors:
- Zixiang Chen
- Wenting Zhao
- Zhepeng Cen
- Akshara Prabhakar
- Jielin Qiu
- Jianguo Zhang
- Zhiwei Liu
- Tulika Manoj Awalgaonkar
- Liangwei Yang
- Shelby Heinecke
affiliations:
- Salesforce AI Research
arxiv_id: '2609.24985'
url: https://arxiv.org/abs/2609.24985
pdf_url: https://arxiv.org/pdf/2609.24985
published: '2026-09-21'
collected: '2026-09-22'
category: Agent
direction: Agent 多轮工具调用 RL 训练优化
tags:
- Reinforcement Learning
- Multi-Turn Tool Use
- Credit Assignment
- LLM Agent
- Local Training
one_liner: 通过嵌套采样分离动作相关奖励波动与下游噪声，精准选择多轮交互的可训练节点
practical_value: '- 多轮电商导购、搜索推荐Agent训练优化：替代全链路RL的粗放训练方式，先用嵌套采样方法定位哪一轮决策存在真实优化空间，仅对该轮次传递梯度，避免无效训练甚至效果下降，同时降低算力成本

  - 多轮决策的局部奖励设计：参考文中分层奖励思路，比如电商多轮加购、下单路径的Agent决策，可将当前动作合法性校验（如是否违规改价、是否重复调用接口）与下游转化结果得分结合，获得比端到端奖励更准确的训练信号

  - 大模型Agent微调工程优化：仅对关键节点的生成token计算梯度，其余轮次仅作为上下文输入或奖励计算单元，适合业务上高频迭代的广告投放智能体、客服Agent等场景，大幅降低微调的显存占用和训练时长'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
多轮工具调用任务中轨迹级奖励无法定位可优化决策节点，下游交互随机性导致奖励波动无法反映当前动作优劣，全链路RL训练算力成本高、易出现负向效果，长路径电商导购、多轮搜索等Agent场景的错误梯度分配会直接损伤业务效果。
### 方法关键点
- 定义可训练节点三重判定条件：动作充足性（局部奖励能反映当前动作对最终结果的影响）、优化空间（存在优于参考策略的动作）、可训练性（不同动作对应奖励均值存在显著差异）
- 嵌套采样分离信号与噪声：固定上下文采样多组动作，每个动作固定后重采样下游交互，拆分动作相关奖励方差与下游随机噪声，选择方差最大的节点作为训练目标
- 仅对选中节点做contextual-bandit训练，其余轮次仅提供上下文或计算奖励，不传递梯度
### 关键结果
在BFCL v4多轮工具调用基准上对比全链路Monte-Carlo RTG、固定轮次训练等baseline：
- 缺工具任务（miss_func）选择工具可用后的恢复轮次训练，准确率从0.14提升至0.283，涨幅14.3pp；训练错误轮次准确率反而下降4.5pp
- 缺参数任务（miss_param）选择参数补全前的决策轮次训练，准确率从0.435提升至0.473，涨幅3.8pp；训练错误轮次仅上涨1pp
- 落地真实业务日志的重复调用规避任务，与GPT-4.1的一致性从37%提升至75%；内存管理任务准确率提升16pp
> 最值得记住的结论：多轮Agent训练的核心不是选择训练方法，而是先精准定位值得训练的节点，错误的训练位置带来的效果损失远大于训练方法的差异

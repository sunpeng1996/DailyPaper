---
title: 'LLM Agents for Deliberative Collaboration: A Study on Joint Decision Making
  Under Partial Observability'
title_zh: 部分可观测场景下LLM Agent协商协作与联合决策研究
authors:
- Chenxu Wang
- Yongkun Yang
- Boyuan Du
- Shiwei Lin
- Huaping Liu
affiliations:
- Tsinghua University
- Fuzhou University
arxiv_id: '2607.06157'
url: https://arxiv.org/abs/2607.06157
pdf_url: https://arxiv.org/pdf/2607.06157
published: '2026-07-07'
collected: '2026-07-08'
category: MultiAgent
direction: 多Agent 部分可观测协商决策优化
tags:
- MultiAgent
- Deliberative Collaboration
- Partial Observability
- Joint Decision Making
- LLM Agent
one_liner: 提出部分可观测下多Agent协商协作框架与基准，系统评估主流LLM的联合决策能力
practical_value: '- 做分布式运营/推荐多Agent协作时，可复用「部分观测-信息对齐-联合决策」三段式架构，拆分观测、规划、对话、决策4个模块，适配对称协作/领导制两类业务模式

  - 多Agent工具调用设计可参考结论：中小参数LLM搭配数值计算/整数规划工具可大幅提升决策正确率，大模型易出现拒绝采纳工具输出的问题，需在prompt中加强制工具结果对齐约束

  - 电商多角色（运营/库存/商品）Agent联合做活动选品、资源分配时，可直接复用基准的任务形式化方法，将问题转化为带约束的组合优化问题，量化协作效果

  - 工程上多Agent协商轮次无需设置过高，实验显示6轮协商足够覆盖绝大多数信息对齐需求，更高轮次不会带来明显收益还会增加推理成本'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前多Agent协作研究大多假设全观测信息，而真实业务场景中每个Agent仅能拿到局部、非对称信息，需通过协商对齐信息才能做出最优联合决策，现有框架缺乏对这类场景的统一定义和标准化测评基准。

### 方法关键点
- 形式化定义部分可观测多Agent联合决策问题为(s, O₁…Oₙ, D, R)五元组，每个Agent仅持有局部观测，目标是通过多轮协商最大化全局共享奖励
- 设计覆盖3类场景的可扩展基准：数值观测菜单设计、语义观测菜单设计、非对称角色任务分配，所有任务均可转化为整数规划问题计算理论最优奖励上界
- 提出通用协商Agent架构，包含观测、规划、决策、对话四大模块，支持调用外部整数规划求解器、计算器两类工具辅助决策
- 定义归一化奖励(NR)、有效决策率(VR)两类核心指标，同时引入全观测集中式基线、全观测协商Oracle基线做对比

### 关键实验
在180个测试任务上测评7款主流LLM，设置最多6轮协商，核心结果：1）SOTA大模型在简单数值观测场景NR可达95%以上，但在语义观测、任务分配复杂场景NR仅为55%-80%；2）协商过程可提供反思纠错机会，部分场景下比集中式基线NR最高提升19pct；3）中小模型加工具后NR最高提升30pct，但GPT-5.1等大模型工具采纳率最低可达0%，工具增益不明显。

最值得记住的结论：多Agent协作的核心瓶颈不是单模型推理能力，而是跨Agent的信息对齐准确率和工具结果服从度。

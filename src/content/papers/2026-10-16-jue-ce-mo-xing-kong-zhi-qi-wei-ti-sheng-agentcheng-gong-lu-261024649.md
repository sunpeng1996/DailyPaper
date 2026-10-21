---
title: 'Good Judgment, Bad Advice: Decision-Model Controllers Raise Agent Cost Without
  Improving Success'
title_zh: 决策模型控制器未提升Agent成功率反而推高运行成本
authors:
- Naman Vats
affiliations:
- Birla Institute of Technology, Mesra
arxiv_id: '2610.24649'
url: https://arxiv.org/abs/2610.24649
pdf_url: https://arxiv.org/pdf/2610.24649
published: '2026-10-16'
collected: '2026-10-21'
category: Agent
direction: Agent 控制层决策模型性能评估
tags:
- Agent
- LLM Controller
- Cost Optimization
- Agent Evaluation
- Decision Making
one_liner: 通过安慰剂对照实验验证Agent决策层专用小模型未降本提效反而使成本上升19%
practical_value: '- 做Agent控制逻辑优化不要仅看离线决策AUROC，必须做端到端成本+成功率的联合评估，离线指标好不代表线上业务收益

  - 不要盲目上专用决策小模型，先测试简单规则甚至随机干预的基准，多数情况下专用模型的额外收益无法覆盖其带来的轨迹拉长成本

  - 给控制器设置干预阈值时必须结合业务场景的base rate，例如电商Agent用户请求的自然完成率较高时，不要频繁触发校验，避免产生多余开销

  - 设计Agent控制动作时要确保成本节约类动作（如提前终止无效请求）可被实际触发，否则只会增加无效运行开销'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前Agent架构普遍将停止、校验、路径切换等小决策委托给低成本小模型执行，行业默认这类决策模型能在不降低成功率的前提下降低整体运行成本，但过往评估仅关注离线决策精度，未验证干预后的端到端实际收益，存在明显的评估缺口。
### 方法关键点
- 固定主推理Agent为Claude Sonnet 5.5，仅替换控制层逻辑，设置5组对照：无控制器、规则控制器、Claude Haiku小LLM控制器、专用决策模型Jev 1.13、安慰剂控制器（采样Jev开发阶段决策频率随机输出）
- 设定4类确定性决策触发点：连续命令失败、无进展重复操作、Agent发起结束请求、每10步自动checkpoint
- 控制器输出仅映射为固定引导语，不向Agent注入任务相关的额外信息，排除控制逻辑外的变量干扰
### 关键结果
- 实验基于Terminal-Bench 2.1的21个held-out任务，共315次对照试验
- Jev对比无控制器组，成功率完全一致（73.0%），单次尝试成本上升19%；Jev比Haiku控制器成本低19%，但比安慰剂控制器高22%，所有控制器组的成功率无统计显著差异
- 离线评估Jev的结束请求排序AUROC达0.78，远高于规则的0.62和Haiku的0.60，但校准度极差，87%的正确结束请求被要求二次校验，直接导致运行轨迹拉长、成本上升
> 最值得记住的结论：**决策信号的离线精度高不代表端到端收益好，有用信号和有效干预之间的核心gap是适配场景base rate的动作策略**

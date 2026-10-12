---
title: 'RATED: Reliability-Aware AI Agent Tool Retrieval via Execution Dynamics'
title_zh: RATED：基于执行动态的可靠性感知AI Agent工具检索
authors:
- Weiliang Chen
- Song Liao
affiliations:
- Texas Tech University
arxiv_id: '2610.13889'
url: https://arxiv.org/abs/2610.13889
pdf_url: https://arxiv.org/pdf/2610.13889
published: '2026-10-09'
collected: '2026-10-12'
category: Agent
direction: Agent 工具检索可靠性优化
tags:
- Tool Retrieval
- Contextual Bandit
- Contrastive Learning
- AI Agent
- LinUCB
one_liner: 将冻结双编码器语义匹配与折扣LinUCB重排结合的高可靠AI Agent工具检索框架
practical_value: '- 电商/广告/Agent系统的工具/API/插件召回场景，可复用「静态语义召回+轻量在线重排」架构，无需重训大模型即可适配服务故障、限流等动态场景，比批RL更新方案延迟低两个量级

  - 新工具冷启动的先验分数可直接复用「名称-描述语义一致性+来源可信度+文档质量」三个无标注信号加权方案，无需人工标注即可实现冷启动排序

  - 排序信号融合权重可直接参考论文最优配置：75%语义分、15%在线反馈分、10%静态先验分，兼顾相关性与动态可靠性

  - 折扣LinUCB实现时采用对角协方差矩阵简化计算，单步重排开销<1ms，完全满足线上低延迟交互要求'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有AI Agent工具检索仅优化语义相关性，完全忽略运行时工具可用性，真实开源工具生态中超50%的工具存在断链、鉴权失败、服务宕机等问题，静态检索方案在工具故障时会持续返回不可用选项，严重影响Agent执行成功率。

### 方法关键点
- 语义召回层采用冻结DRAGON双编码器，基于合成的EcoAgent-Syn数据集做对比微调后固定，新增工具仅需编码文档即可接入，无需重训
- 动态重排层采用折扣LinUCB上下文老虎机，基于工具执行的成功/失败二元反馈实时更新权重，旧反馈按γ=0.95折扣，优先响应近期故障信号
- 最终排序融合三类信号：75%语义匹配分、15%老虎机可靠性分、10%元数据静态先验分，静态先验由工具元数据自动计算解决冷启动问题
- 开源EcoAgent基准数据集，包含5172个真实工具、21万+查询-工具对，支持静态检索精度与动态故障场景下的可靠性评估

### 关键实验
在EcoAgent-Real真实查询集上，MRR相比ToolLLM API检索器相对提升52.2%；30%工具故障率的模拟场景下，故障选择率从ToolLLM的86.2%降至2.9%，端到端延迟仅比纯编码推理增加0.172ms，几乎无感知。

**最值得记住的一句话**：高可用Agent工具检索不能仅依赖离线语义匹配，必须结合低开销的在线执行反馈动态调整排序，才能适配真实环境的非稳态故障。

---
title: 'From Test-Time Scaling to Reusable Memory: Measuring Crystallization in Text-to-SQL'
title_zh: 从测试时伸缩到可复用记忆：Text-to-SQL 任务的结晶度度量
authors:
- Jiaqian Wang
- Yutao Qi
- Wenjin Hou
- Yuanxi Che
- Muning Wen
affiliations:
- Xidian University
- Shanghai Jiao Tong University
arxiv_id: '2608.07213'
url: https://arxiv.org/abs/2608.07213
pdf_url: https://arxiv.org/pdf/2608.07213
published: '2026-08-07'
collected: '2026-08-10'
category: Agent
direction: Agent 可复用记忆度量与优化
tags:
- Text-to-SQL
- Agent Memory
- Test-time Scaling
- Experience Reuse
- Execution Feedback
one_liner: 提出Text-to-SQL结晶度度量框架，量化可复用修复经验的迁移价值，明确记忆模块最优设计方向
practical_value: '- 电商智能客服/订单查询类Text-to-SQL Agent可复用经验：将验证通过的历史修复查询存入记忆库，无需每次调用昂贵的测试时修复链路，兼顾性能与推理成本

  - 记忆模块优化优先做高ROI动作：优先保障验证逻辑可靠性、检索覆盖度，无需过度投入复杂检索器、多格式记忆存储等方向

  - 记忆系统评估可复用拆分框架：区分历史问题回放、同域跨问题迁移、跨域迁移三类增益，而非仅看端到端总指标，可精准定位优化瓶颈'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有Text-to-SQL测试时修复的额外计算资源通常随单次请求结束被丢弃，即使留存经验也缺乏合理评估框架，无法区分旧问题复用增益、新问题迁移增益，难以量化记忆的长期价值（即结晶度）。

### 方法关键点
固定单轮求解器能力，控制变量测试不同记忆设计的效果，拆分三类独立评估维度：历史问题回放准确率、同库跨问题保留增益、同库未见问题迁移增益。

### 关键结果数字
在BIRD数据集上，存储验证后的修正查询可将未见问题首次尝试准确率提升4.34个百分点，达到同问题按需修复增益上限的44.4%；核心增益来自数据库专属内容，可靠验证、更广检索覆盖可稳定提效，复杂检索器、丰富记忆格式无额外收益。

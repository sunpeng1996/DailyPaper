---
title: 'From Controlled to the Wild: Evaluation of Pentesting Agents for the Real-World'
title_zh: 从受控环境到真实场景：渗透测试Agent的落地评估方案
authors:
- Pedro Conde
- Henrique Branquinho
- Valerio Mazzone
- Bruno Mendes
- André Baptista
- Nuno Moniz
affiliations:
- Ethiack
- University of Notre Dame
arxiv_id: '2605.10834'
url: https://arxiv.org/abs/2605.10834
pdf_url: https://arxiv.org/pdf/2605.10834
published: '2026-07-13'
collected: '2026-07-18'
category: Eval
direction: Agent性能评估 · 真实场景适配
tags:
- Agent
- LLM
- Evaluation
- Benchmark
- Real-world Deployment
one_liner: 提出面向真实渗透测试场景的Agent评估协议，配套开源专家标注数据集与代码
practical_value: '- 做落地Agent性能评估时，可借鉴「从预设任务完成率转向实际价值产出」的框架设计思路，避免实验室指标与业务效果脱节

  - 处理评估结果歧义问题时，可复用结构化真值+LLM语义匹配+二分冲突消解的组合方案，降低人工标注成本同时提升评估准确率

  - 针对随机性强的Agent系统，采用多次重复累积评估+效率指标的方案，可更客观量化真实落地性能，避免单次实验波动干扰'
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
现有AI渗透测试Agent的评估方案多在受控简化环境中针对夺旗、远程代码执行等预设目标设计，无法覆盖真实场景所需的开放探索、战略决策等能力，输出的评估结果对落地选型参考价值有限。
### 方法关键点
将评估核心从任务完成率转向经校验的漏洞发现，支持覆盖多攻击面、多漏洞类型的复杂目标测试；评估流程融合结构化真值、LLM语义匹配做漏洞识别，引入二分消解机制处理真实场景下的结果歧义，配套真值持续更新、随机Agent重复累积评估、效率指标、精简测试集选择等模块，支持可持续的实验对比。
### 关键结果
配套开源专家标注真值数据集与评估代码，相比现有SOTA评估方案，可输出更贴合真实业务需求的Agent性能对比结果，评估的业务参考性提升显著。

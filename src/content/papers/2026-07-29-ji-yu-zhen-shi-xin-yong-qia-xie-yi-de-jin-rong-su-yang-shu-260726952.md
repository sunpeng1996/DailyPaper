---
title: 'Credit Cards, Confusion, Computation, and Consequences: What Can We Uncover
  About Language Model Reasoning?'
title_zh: 基于真实信用卡协议的金融素养数值推理基准与LLM能力评估
authors:
- Arnav Hiray
- Agam Shah
- Caleb Lu
- Meghaj Tarte
- Harsit Mittal
- Sudheer Chava
affiliations:
- Georgia Institute of Technology
arxiv_id: '2607.26952'
url: https://arxiv.org/abs/2607.26952
pdf_url: https://arxiv.org/pdf/2607.26952
published: '2026-07-29'
collected: '2026-07-30'
category: Reasoning
direction: 金融领域LLM数值推理能力评估
tags:
- Numerical Reasoning
- Financial LLM
- Benchmark
- Chain-of-Thought
- Program-of-Thought
one_liner: 构建首个基于真实信用卡协议的金融素养推理基准，验证PoT提示显著提升数值推理性能
practical_value: '- 做电商分期、会员计费、退款规则咨询等带数值计算的规则类Agent时，优先用PoT替代CoT，可提升1%-6%准确率，对小参数开源模型收益更高

  - 面向用户的咨询类Query尽量适配第一人称表述，匹配LLM指令微调数据分布，可提升约40%的回答正确率

  - 处理多条件分支、大小比较的规则类问题时，可新增规则抽取+符号计算后校验模块，减少70%左右的规则误用、条件遗漏类错误

  - 构建垂直领域推理评测集时，可参考其从真实业务规则文档人工标注的方法，保证评测数据贴合实际业务场景'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前美国信用卡债务规模达1.2万亿美元，消费者金融素养连续8年维持在50%左右，超半数用户已开始使用LLM辅助个人金融决策，但现有金融推理基准集中于股票、企业财报等专业场景，缺乏针对个人金融素养的真实场景评测数据，无法验证LLM处理信用卡协议这类多条件、高风险规则类推理的可靠性，模型错误会给低收入等脆弱群体带来额外损失。
### 方法关键点
- 从CFPB数据库选取覆盖80%市场份额的27份主流信用卡协议，覆盖高端卡、日常零售卡、次级卡三类产品，统一转换为LLM可读取的Markdown格式
- 由具备CFA、量化金融背景的专业团队标注1800个问答对，其中492个为第一人称用户真实视角问题，单题平均需要4.4次数学运算，覆盖利息计算、费用、滞纳金、还款规则等核心场景
- 评测11款主流开源/闭源LLM、LRM，对比CoT、PoT两种提示策略的效果，采用±0.2%、±5%两种误差容忍度的准确率作为核心指标
### 关键结果
- PoT相对CoT在±5%误差容忍度下可带来0.9%~6.2%的准确率提升，对基线性能较弱的模型增益更大，可有效缩小开源与闭源模型的性能差距
- 开源GPT-OSS 120B在PoT提示下准确率达79.2%，超过闭源GPT-5、Gemini 3.0 Pro的同期表现
- 错误分析显示仅14%的错误来自算术计算，70%来自金融规则误用、54%来自条件遗漏；包含比较运算的问题正确率下降74%，第一人称提问比第三人称准确率高42%
### 核心结论
LLM在规则类数值推理场景的失败大多不是算术能力不足，而是规则理解错误、条件遗漏，将逻辑推理与数值计算解耦的PoT提示是性价比最高的优化手段

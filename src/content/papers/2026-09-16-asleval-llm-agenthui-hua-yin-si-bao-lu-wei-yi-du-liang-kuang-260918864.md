---
title: 'ASLEval: Measuring Privacy Exposure Displacement in LLM Agent Sessions'
title_zh: ASLEval：LLM Agent会话隐私暴露位移度量框架
authors:
- Guosen Wu
- Huizhen Huang
- Guoxiong Long
- Tao Huang
- Chen Hou
affiliations:
- School of Computer and Big Data, Minjiang University
arxiv_id: '2609.18864'
url: https://arxiv.org/abs/2609.18864
pdf_url: https://arxiv.org/pdf/2609.18864
published: '2026-09-16'
collected: '2026-09-17'
category: Eval
direction: LLM Agent 全会话隐私暴露评估
tags:
- LLM Agent
- Privacy Evaluation
- Benchmark
- Session Measurement
- Privacy Leakage
one_liner: 提出授权感知的ASLEval框架，度量LLM Agent全会话隐私暴露的三类局部评估偏差
practical_value: '- 企业级Agent（电商智能客服、商家运营助手、导购Agent等）隐私审计时，需枚举所有用户可见出口（最终回复、控制台提示、中间操作反馈、文件共享等）统一校验，避免仅检查指定出口漏检46.9%的隐私泄露

  - 做Agent红队攻防测试时，不要将探针的自报告作为隐私泄露ground truth，需提前预设隐私目标集做事后匹配，探针自报告漏检率最高达23.9%、误报率超69%

  - Agent工具接口设计时，单纯修改输入输出字段名无法降低隐私泄露风险，最小化LLM可见的工具返回内容可降低45.7%的泄露概率，需同步做内容筛选避免粗暴截断导致任务成功率从80%降至0'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有LLM Agent隐私评估多依赖指定动作、最终回复、攻击者报告等局部代理指标，会漏检多步会话中其他出口的未授权隐私暴露，不同评估路径的结果缺乏统一真值，导致隐私风险被严重低估。
### 方法关键点
- 定义三类隐私暴露位移：出口位移（仅检测预期出口漏检其他可见出口泄露）、识别位移（攻击者自报告存在漏报误报）、路径位移（内部工具路径与可见暴露的关联偏差）
- 提前预设隐藏隐私目标集、授权规则、全可见出口边界，会话过程仅允许盲探针发送合法请求、观察公开反馈，全程不泄露目标集信息
- 事后基于预设目标集做授权感知的全可见出口匹配，内部工具调用、返回日志仅作为路径诊断依据，不直接判定为隐私泄露
### 关键结果
在PIA、AgentDojo Workspace、WorkBench三个企业级环境，覆盖DeepSeek、GLM两类模型测试：
1. 仅检测预期出口会漏检46.9%的全可见出口隐私暴露，攻击者自报告漏检23.9%、误报率最高达69.4%
2. 开启单个出口防护（如邮件过滤）几乎不降低全会话泄露率，泄露会转移到控制台等其他未防护出口
3. 最小化LLM可见的工具返回内容可降低45.7%的隐私泄露风险，但粗暴实施会导致正常任务成功率从80%降至0，API成本提升5.76倍

最值得记住的结论：LLM Agent隐私评估不能依赖局部指标，必须提前注册全可见出口边界、预设隐私真值集，同时披露隐私防护效果与任务效用的trade-off。

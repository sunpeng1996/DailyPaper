---
title: 'FormBharo: Designing and Evaluating a Voice Agent for Conversational Form
  Filling in Rural India'
title_zh: FormBharo：面向印度农村会话式表单填写的语音代理设计与评估
authors:
- Aman Dalmia
- Sanskriti Midha
- Jigar Doshi
affiliations:
- Artpark, Indian Institute of Science
- ARMMAN
arxiv_id: '2608.06027'
url: https://arxiv.org/abs/2608.06027
pdf_url: https://arxiv.org/pdf/2608.06027
published: '2026-08-06'
collected: '2026-08-07'
category: Agent
direction: 语音Agent 低资源会话任务落地
tags:
- VoiceAgent
- Hybrid LLM Architecture
- End-to-end Evaluation
- Low-resource NLP
- Form Filling
one_liner: 提出混合LLM+规则的低资源语音表单填写Agent，配套开源印地语评测基准
practical_value: '- 复杂交互类Agent可采用「LLM做语义理解+规则做流程控制/校验」的混合架构，用低成本小模型匹配大模型端到端效果，大幅降低部署成本

  - 多组件级联的Agent系统不要只看单组件指标，必须做端到端效果评估，误差在链路中会同时存在传播和抵消效应

  - 多目标选型（准确率/延迟/成本）可先用硬约束过滤不符合要求的候选，再在Pareto最优集上用加权求和做量化排序，适配业务优先级

  - 语音场景ASR效果评估不要只用WER，可采用LLM-WER过滤语义等价的转录误差，评估结果更贴合下游任务实际表现'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
印度低收入低识字群体无法自主填写社会福利表单，福利申领完全依赖一线工作人员人工录入，效率极低受容量上限；现有语音交互系统在口音混杂、背景噪音、低资源语言场景下准确率差，且落地受严格的成本、延迟约束，难以规模化应用。

### 方法关键点
- 混合架构设计：LLM仅负责用户语义提取（EXTRACT模块）和自然语言回复生成（REPLY模块），表单字段校验、流程分支跳转、重试逻辑全部用规则实现，减少LLM幻觉同时降低推理成本
- 开源评测基准FormVoiceAgentBench：包含380条印地语真实录音、960通模拟通话、3760个多轮测试用例，覆盖真实声学噪音、地域口音、语速变化等实际场景特征
- 评估与选型流程：同时做组件级单元测试和全链路集成测试，用LLM judge评估开放域提取/回复的语义正确性；多目标选型采用硬约束过滤→Pareto最优集筛选→加权求和量化排序的流程，适配业务优先级

### 关键结果数字
对比5款ASR、11款LLM的实验显示：1）用带误差的真实语音转录代替参考转录时，表单完成率最高下降41个百分点；2）规则层可修复大量LLM提取错误，小模型端到端效果可追平甚至超过GPT-5.5等前沿大模型，参考转录下Gemini 3 Flash单轮提取准确率仅95.96%，但经规则修复后表单完成率达100%；3）组件级指标完全无法预测端到端效果，GPT-5.5单轮提取准确率达99.79%但表单完成率排名更低。

### 核心结论
多组件级联的Agent系统，最优选型只能通过端到端评估得到，没有单一模型能同时在准确率、成本、延迟三个维度上最优

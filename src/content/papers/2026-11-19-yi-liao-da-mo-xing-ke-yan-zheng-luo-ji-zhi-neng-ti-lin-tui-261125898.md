---
title: 'Verifiable Logic in Medical LLMs: A Critical Review of Agentic Clinical Reasoning
  Optimization and Neuro-Symbolic Grounding'
title_zh: 《医疗大模型可验证逻辑：智能体临床推理优化与神经符号落地综述》
authors:
- Youssef ElNahas
- Adel Ammar
- Soumaya Chaffar
- Wadii Boulila
affiliations:
- University of Prince Mugrin
- Prince Sultan University
arxiv_id: '2611.25898'
url: https://arxiv.org/abs/2611.25898
pdf_url: https://arxiv.org/pdf/2611.25898
published: '2026-11-19'
collected: '2026-11-20'
category: Agent
direction: 医疗Agent · 可验证推理优化
tags:
- LLM
- Agent
- Neuro-Symbolic
- Reasoning Verification
- Hallucination Mitigation
one_liner: 系统性梳理医疗LLM推理错误范式，提出融合智能体流程与神经符号校验的可验证临床推理框架
practical_value: '- 多Agent系统中要加入独立的符号校验层，避免早期错误通过协作级联放大，可复用在电商导购多Agent的商品信息、优惠规则校验场景

  - Process Reward Model（PRM）的校验边界是训练数据分布，高风险场景（如电商合规文案生成、金融推荐）必须补充外部规则校验，不能完全依赖PRM

  - 静态评估指标无法检测推理路径错误，推荐/搜索系统的效果评估可加入路径级校验，比如从用户Query到召回结果的逻辑链一致性检测

  - hallucination cascade机制可迁移到RAG系统的错误排查：优先校验上游检索、工具调用环节的正确性，而非仅校验最终输出'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前医疗LLM仅靠最终答案准确率评估，无法检测无效推理、幻觉、因果推断错误等安全隐患，多Agent协作系统还会出现早期错误跨节点级联放大的问题，现有研究分别聚焦Agent架构优化或神经符号落地，缺乏统一的可验证推理框架指导安全落地。
### 方法关键点
- 划分5类可验证推理机制：演绎验证、本体校验、证据落地验证、概率学习验证、结构化流程验证
- 归纳4类临床LLM幻觉亚型：捷径学习与伪相关、上下文遗漏与对抗脆弱性、校准偏差与过度自信、多模态跨域脆弱性
- 定义智能体-符号融合框架，将Agent全流程推理节点对应到符号校验干预点，从架构层面约束推理合法性
### 关键结果
- 基于2024-2026年98篇核心研究分析：带符号否决层的系统在其编码域内安全指标提升显著，PRM的校验能力严格受限于训练数据分布
- 多Agent临床系统的共识机制存在98.42%的观点重复率，权威偏差从第一轮的35.30%上升到第三轮的68.75%
- 现有静态基准89%缺乏鲁棒性测试、91%忽略不确定性处理，完全无法检测结果正确但推理路径错误的问题
### 核心结论
高风险场景下的AI安全本质是架构问题，仅靠训练、校准、Prompt优化无法替代全流程的可验证推理校验

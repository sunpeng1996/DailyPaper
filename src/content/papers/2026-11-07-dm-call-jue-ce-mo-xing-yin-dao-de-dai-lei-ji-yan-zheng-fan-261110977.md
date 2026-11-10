---
title: 'DM-Call: Decision-Model-Guided Function Calling with Cumulative Verification
  Feedback'
title_zh: DM-Call：决策模型引导的带累积验证反馈的工具调用框架
authors:
- Minhyeong Yu
- Wonduk Seo
- Seunghyun Lee
affiliations:
- Enhans
- University College London
arxiv_id: '2611.10977'
url: https://arxiv.org/abs/2611.10977
pdf_url: https://arxiv.org/pdf/2611.10977
published: '2026-11-07'
collected: '2026-11-10'
category: Agent
direction: Agent 工具调用优化
tags:
- function_calling
- agent
- verification
- iterative_refinement
- feedback_mechanism
one_liner: 将分模块决策验证与累积混合反馈结合，低成本提升LLM工具调用准确率
practical_value: '- 电商导购Agent、商品查询API调用场景可直接复用DM-Call的分模块验证逻辑：分别校验接口选择和参数正确性，避免语义错误的无效调用

  - 混合反馈设计可迁移到生成式推荐的prompt迭代：把数值置信度+语义标签结合作为反馈信号，提升小模型生成item/query的准确率

  - 修复预算r=3的最优trade-off结论可直接用在业务工程：超过3轮迭代后准确率提升<2%但p95延迟翻倍，业务侧无需设置过高重试次数

  - 弱LLM场景收益更明显：用小模型做工具调用时加这套验证框架，准确率提升可达10pp，成本远低于直接换大模型'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有LLM函数调用仅做语法校验无法识别语义错误（比如选错接口、参数不符合用户意图），自纠错、多Agent辩论等方法要么推理成本高，要么不区分错误类型、不保留历史反馈信号，迭代效率低。

### 方法关键点
- 架构拆分生成器G和独立决策模型D，D分别输出函数选择置信度$p_f$、参数正确性置信度$p_a$，仅当两个置信度≥0.5且通过语法校验才接受调用
- 引入累积反馈机制：保留所有历史失败调用的校验结果、语法错误信息，作为后续迭代的上下文输入
- 混合反馈表示Φ：把数值置信度分箱映射为5档语义标签（从very likely incorrect到very likely correct），同时保留数值和标签作为反馈信号
- 设置修复预算阈值，超过r次修复失败则返回初始结果，控制推理成本

### 关键实验
在BFCL（3035条单轮用例）、API-Bank（156条首调用用例）上测试4种LLM生成器，对比直接生成、Self-Refine、多Agent辩论等基线：
- 对最小的gpt-5-nano，DM-Call比直接生成准确率提升10.5pp，成本仅为多Agent方法的1/3
- 整体平均准确率比基线高0.3-1.3pp，r=3时达到最优trade-off：p95延迟9.7s，比r=10低14.6s，准确率仅低1.8pp
- 混合反馈比单纯数值/文本反馈平均准确率高0.1-0.6pp，在小模型上收益更显著

### 核心结论
工具调用优化不需要盲目堆多Agent或者大模型，拆分验证模块+累积历史反馈就能用极低的额外成本拿到显著的准确率收益

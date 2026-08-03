---
title: 'Data Turnstile: A Scalable Open Framework for Function-Calling Data Generation'
title_zh: Data Turnstile：可扩展开源函数调用训练数据生成框架
authors:
- Goutham Ramakrishnan
- Megha Sharma
affiliations:
- Amazon AGI
arxiv_id: '2607.29250'
url: https://arxiv.org/abs/2607.29250
pdf_url: https://arxiv.org/pdf/2607.29250
published: '2026-07-31'
collected: '2026-08-03'
category: Training
direction: SLM工具调用 · 合成数据生成
tags:
- Synthetic Data
- Function Calling
- Small Language Model
- SFT
- Agent
one_liner: 分步生成加校验的函数调用数据框架，让SLM工具调用能力追平大3-19倍的模型
practical_value: '- 业务自定义Agent开发可直接复用该框架，输入内部API schema即可生成专属SFT数据，无需人工标注，大幅降低小模型工具调用能力的训练成本

  - SLM工具调用训练时可对API CALL token施加3-5倍加权损失，强化核心指令的学习效果，尤其适合低延迟要求的端侧/业务场景小模型

  - CoT使用需场景适配：单轮工具调用场景禁用CoT，可避免过度推理幻觉、降低推理延迟；多轮复杂诊断类Agent任务必须保留CoT，提升多步推理准确率

  - 合成数据生成可采用模板+参数采样+动态扰动的方式，比纯温度采样的多样性和可控性更高，还可灵活调整数据分布适配业务需求'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
SLM因低延迟、低成本、隐私合规性优势，非常适合电商/客服等场景的端侧Agent部署，但工具调用能力远弱于大模型，核心瓶颈是高质量训练数据稀缺——现有合成数据生成方案要么单步生成质量差、错误多，要么依赖闭源大模型、需要真实API执行后端，成本高且不可控。
### 方法关键点
- 将多轮工具调用交互拆解为USER、API CALL、API OBS、ASSISTANT、THINKING五种角色的DAG生成流程，每个角色独立生成，附加专属校验规则，生成失败带错误反馈重试，避免错误传导
- 通过模板定义、参数采样、动态扰动（如模拟API报错、用户不配合等场景）灵活控制数据复杂度和多样性，支持自定义API、业务政策，无需真实API后端，可使用开源模型本地生成
- 训练时可对API CALL token施加加权损失，强化工具调用核心指令的学习效果
### 关键结果
- 单轮BFCL基准：Qwen3-0.6B经其生成数据SFT后，无CoT准确率达75.9%，比base带CoT的67.4%高8.5pp，接近7倍参数的Qwen3-4B（79.9%）
- 多轮τ2-bench电信域：Qwen3-1.7B SFT后pass@1达31.1%，较base提升4.7倍，超过19倍参数的Qwen2.5-32B-Instruct（27.4%）；0.6B版本较base提升7倍，接近32B模型表现
- 已开源1000+API、10万+多轮交互的合成数据集，可直接用于SLM工具调用训练

高质量结构化合成数据可极大弥补SLM的容量不足，甚至让小模型在垂直工具调用场景超过大几十倍的通用大模型

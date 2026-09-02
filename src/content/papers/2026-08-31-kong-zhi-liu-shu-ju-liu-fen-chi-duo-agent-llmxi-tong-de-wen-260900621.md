---
title: 'Control-Data Flow Separation: Stable Prompt Optimization in Multi-Agent LLMs'
title_zh: 控制流-数据流分离：多Agent LLM系统的稳定提示优化
authors:
- Wentao Zhang
- Syed Shariyar Murtaza
- Junaid Ahmad Bhatti
- Utkarsh Soni
- Yifan Nie
- Eugene Wen
- Yuntian Deng
affiliations:
- University of Waterloo
- Manulife
arxiv_id: '2609.00621'
url: https://arxiv.org/abs/2609.00621
pdf_url: https://arxiv.org/pdf/2609.00621
published: '2026-08-31'
collected: '2026-09-02'
category: Agent
direction: 多Agent系统 · 提示优化稳定性
tags:
- Multi-Agent
- Prompt Optimization
- Control Flow
- Data Flow
- Schema Validation
one_liner: 提出控制流-数据流分离架构，实现多Agent LLM提示优化时零协议失效且持续提升任务性能
practical_value: '- 电商/广告场景的多Agent pipeline（如智能客服、营销文案生成、用户反馈处理）可直接复用该设计，将路由、格式校验、终止信号等控制逻辑封装为不可被prompt优化修改的结构化schema，避免prompt迭代时流程崩溃

  - 搭配TextGrad、DSPy等现有提示优化工具使用时，仅开放数据通道的prompt给优化器，控制通道完全冻结，可在保证流程100%稳定的前提下实现业务效果迭代，无需为了稳定性牺牲优化空间

  - 工程实现上可复用开源Python库cdsep的开发模式，用Pydantic/dataclass定义控制schema，自动生成格式引导prompt，内置重试/兜底逻辑，大幅降低多Agent系统的开发和维护成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
多Agent LLM系统的prompt同时承担两项纠缠的职责：生成任务相关的业务内容、定义程序依赖的执行协议（路由规则、输出格式、终止信号等）。直接对prompt做端到端优化时，调整内容生成逻辑的改动极易破坏协议规则，导致流程崩溃、无有效输出，现有提示优化框架均未解决该稳定性问题。

### 方法关键点
- 核心设计为**控制流-数据流分离**：每个Agent输出拆分为双通道，控制通道是带类型校验的结构化程序对象，由程序控制器消费，完全冻结不允许优化器修改，承载路由、终止等执行逻辑；数据通道为自由文本，由其他Agent和优化器消费，支持正常prompt优化
- 控制通道通过Python dataclass/Pydantic定义schema，框架自动生成不可编辑的格式引导prompt，运行时先校验控制字段有效性，失败则重试或走兜底逻辑，确保仅合法控制值进入路由环节
- 优化器仅可修改数据通道对应的prompt，可调整Agent在合法控制选项内的决策，但无法修改控制协议本身

### 关键结果
在BBH推理、MARG论文评审生成、合成/行业验证保险核保4类任务上验证，对比Fixed Prompt、Naive TextGrad、DSPy全系列基线，核心结果：1. 所有场景下协议稳定性达100%，而Naive TextGrad在多Agent场景（如MARG）稳定性直接降至0%；2. 任务表现全面领先：BBH准确率78.3%超最优DSPy基线4pct，MARG Jaccard达44.4%超DSPy MIPROv2，行业保险核保准确率36.7%超行业原生固定prompt5pct；3. 跨OpenAI/Anthropic/Google三类LLM家族均保持100%稳定性，Naive方案全部崩溃。

**最值得记住的一句话**：多Agent系统的稳定性核心是把程序依赖的控制逻辑和可优化的业务逻辑彻底解耦，不要把协议规则写在可编辑的prompt里

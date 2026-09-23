---
title: 'Measuring the Serving Stack Instead of the Model: Hidden Confounds in Local
  Tool-Use Evaluation'
title_zh: 本地Agent工具调用评估隐藏混淆：被测对象是服务栈而非模型
authors:
- Lijuan Tang
- Yuemeng Zheng
affiliations:
- Northeastern University, Seattle
arxiv_id: '2609.26693'
url: https://arxiv.org/abs/2609.26693
pdf_url: https://arxiv.org/pdf/2609.26693
published: '2026-09-22'
collected: '2026-09-23'
category: Agent
direction: Agent工具调用 · 评估协议与服务栈优化
tags:
- Agent Evaluation
- Tool Calling
- Serving Stack
- Local LLM
- Evaluation Protocol
one_liner: 揭示本地Agent工具调用评估的服务层干扰，提出标准化评估检查清单
practical_value: '- 做内部Agent工具调用能力评估时，首先排查服务层拦截：Ollama/vLLM默认会拦截部分模型的`tools`请求，电商场景常用的小模型评估前要先验证服务栈支持性，不能直接把0%调用成功率归因为模型能力差

  - 评估时在Prompt中加明确的工具列表+JSON调用格式提示，可大幅提升多数模型的工具调用保真率；对有原生工具调用支持的模型（如Llama 3.2）保留原生通道，不要强行转文本协议避免性能下降

  - 工具调用成功率不能只报全局turn-pooled值，必须报per-seed均值+置信区间，避免单条长循环episode拉高整体结果误导判断；同时要把服务层失败、超时、重试耗尽单独分类统计，不要计入模型错误

  - 用constrained decoding解决工具调用格式问题时要注意弱能力小模型可能出现非终止循环，需要配套超时/强制终止判断逻辑'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
本地小模型Agent在电商智能客服、运营自动化、推荐系统链路调优场景落地需求激增，但过往工具调用评估默认服务层是透明的，常出现相同模型在不同服务栈下评估结果差异极大，甚至具备工具调用能力的模型被测出0%成功率的问题，背后干扰因素未被系统梳理，评估结果可靠性极低。

### 方法关键点
- 控制模型权重完全一致，交叉验证Ollama、llama.cpp、vLLM、SGLang四个主流服务栈的工具请求处理逻辑
- 设计三组对照配置：native（默认带`tools`参数）、native+hint（保留`tools`参数+Prompt注入工具列表+调用格式提示）、text-tools（移除`tools`参数，全部工具描述放在Prompt中）
- 定义工具调用保真率为模型实际生成turn中合法符合schema调用的占比，单独统计服务层拒绝、重试耗尽等非模型生成的turn，同时报告turn-pooled和per-seed两种统计口径的结果

### 关键实验结果
- 测试覆盖Qwen2.5-Coder全尺寸、Llama3.2、Phi-3、Gemma-3等主流本地小模型
- Native模式下Phi-3、Gemma-3的请求100%被Ollama拦截，模型从未运行却被测出0%保真率；加hint后Qwen系列模型保真率最高提升60pct，Llama3.2用原生+hint达82%保真率，换成统一文本协议骤降到44%
- 四个服务栈对完全相同的`tools`请求处理逻辑完全不同，turn-pooled和per-seed保真率差异最高达55pct

**最值得记住的一句话**：如果不控制服务层变量，你测出来的Agent工具调用能力指标，本质是服务栈的表现而非模型本身的能力。

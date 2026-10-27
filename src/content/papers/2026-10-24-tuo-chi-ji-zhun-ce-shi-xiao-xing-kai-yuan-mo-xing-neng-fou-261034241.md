---
title: 'Beyond Benchmarks: Can Small Open-Weight Models Get Real Coding Work Done?'
title_zh: 脱离基准测试：小型开源模型能否完成真实编码任务
authors:
- Vaibhav Jain
affiliations:
- Independent Researcher, India
arxiv_id: '2610.34241'
url: https://arxiv.org/abs/2610.34241
pdf_url: https://arxiv.org/pdf/2610.34241
published: '2026-10-24'
collected: '2026-10-27'
category: Agent
direction: 编码Agent 小模型端到端落地验证
tags:
- Coding Agent
- Small LLM
- Model Serving
- Tool Calling
- KV Cache
- Task Verification
one_liner: 通过全链路工程实践量化小型开源编码模型完成真实编码任务的表现与落地约束
practical_value: '- 落地Agent时不要只看模型基准分，要验证「模型加载→输出连贯文本→工具调用可解析→任务通过校验」全链路，每一步都可能掉坑，API兼容不代表工具调用符合预期

  - KV cache复用对长会话Agent延迟影响极大，实测冷启动TTFT达69.4s，高复用场景仅2.8s，工程上要做会话亲和、前缀消息不可变、避免无关请求刷掉缓存

  - Agent任务校验要区分「格式校验」和「行为校验」，过于严格的静态格式规则会误杀近50%功能正确的输出，可增加格式容错+二次校验环节

  - 用小模型做Agent子任务worker时，要核算端到端成本而非只算模型推理成本，实测部分场景下委托小模型的端到端成本反而比直接用大模型高40%以上'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有模型性能评估多依赖基准测试，无法反映真实落地时全链路工程问题，实际场景中「模型能加载跑通」和「能完成可落地的真实任务」存在巨大gap，尤其是小开源模型用于Agent场景的端到端表现、工程约束、成本收益都缺乏实测数据。

### 方法关键点
- 拆分编码Agent落地为5层工程链路：分布式推理→可复现服务配置→编码Agent集成→会话连续性保障→任务校验，定义4级成功标准：模型可服务→输出连贯文本→工具调用可解析→任务通过隐藏行为校验
- 实测多个运行时（vLLM/SGLang/llama.cpp/MLX）、多款30B级MoE小开源编码模型的全链路表现
- 用Claude Opus 5.5作为固定父Agent，设计两类编码任务测试集，设置直接用大模型、委托小模型两种对比路径，成本核算采用公开API等价定价

### 关键实验
- 45轮编码任务测试：直接用大模型通过率100%，委托Qwen3-Coder 30B优化模式通过率80%，自适应委托模式通过率93.3%，委托场景单位成功成本比直接用大模型高47%~57%
- 第二组15类合成编码任务共90轮测试：直接用大模型通过率100%，委托Nemotron Cascade 2通过率26.7%，委托Qwen3-Coder 30B通过率0%
- 缓存性能实测：冷前缀请求TTFT中位数69.4s，高复用请求仅2.8s；过于严格的参数名格式校验误杀了19/36功能完全符合要求的输出

### 最值得记住的一句话
Agent落地的成功标准从来不是模型能输出正确的文本，而是全链路打通后输出的结果能通过真实任务的行为校验，每一层工程链路都可能成为性能瓶颈。

---
title: How to Speculate about Uncertainty in Agentic Coding? A Draft-Model Gate Method
title_zh: 智能体编码任务的不确定性推测方法：基于草稿模型的门控机制
authors:
- Konstantin Grotov
- Valentin Malykh
affiliations:
- Tel Aviv University
- IITU
arxiv_id: '2609.05274'
url: https://arxiv.org/abs/2609.05274
pdf_url: https://arxiv.org/pdf/2609.05274
published: '2026-09-04'
collected: '2026-09-07'
category: Agent
direction: Agent 黑盒不确定性量化优化
tags:
- LLM Agent
- Uncertainty Quantification
- Speculative Decoding
- Black-box Model
- Cost Efficiency
one_liner: 逆用投机解码思路，用小开源草稿模型实现黑盒智能体预执行错误预判，降低执行错误与Token成本
practical_value: '- 电商导购、自动化营销、客服类工具调用Agent可直接复用该框架：无需获取闭源大模型logits，仅用4B级小草稿模型对Agent输出轨迹做单次前向打分，即可提前拦截错误工具调用/生成内容，避免后续执行重试的API成本与延迟

  - 多步Agent的异常检测可复用阶段拆分trick：将推理（reasoning）与动作（action）阶段的特征分开统计，可避免推理阶段的高熵噪声掩盖动作阶段的错误信号，实测能提升5~6个AUROC的预判效果

  - 闭源API Agent的不确定性量化落地成本极低：仅需用几千条业务场景的Agent历史轨迹微调小草稿模型，校准后即可跨任务、跨Agent迁移使用，无需修改原Agent逻辑'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
生产环境部署的LLM Agent多为闭源API服务，无法获取内部logits、权重、激活值等信息，传统不确定性估计方法要么依赖白盒访问，要么需要多次采样成本过高；Agent常出现「自信错误」，仅在动作执行后才能发现问题，触发大量重试导致token成本、延迟激增，在代码生成、SQL查询、工具调用等有明确执行校验的场景损失尤为突出。
### 方法关键点
- 逆用投机解码思路：小开源草稿模型不对大Agent的输出做生成预测，而是对其已生成的轨迹做teacher-forcing打分，单次前向传播即可得到投机surprisal、投机gap、投机熵三个token级信号，完全不需要访问大Agent的内部信息
- 阶段感知特征提取：利用Agent轨迹「先推理后动作」的结构特性，将推理（reasoning）和动作（action）两个阶段的信号分开处理，每个阶段的三个信号分别计算均值、方差、最值、趋势等8种统计量，加两个阶段的长度总共得到50维特征，避免推理阶段的高熵噪声掩盖动作阶段的错误相关信号
- 轻量化校准与下游策略对接：用L1正则的逻辑回归做校准器，输出动作执行失败概率，可直接对接veto门控、模型路由、人工介入等下游策略；本次实现的预执行veto门控在预判失败时触发轻量重规划，替代昂贵的执行-失败-重试流程
### 关键结果
在SWE-Bench Verified、DA-Code两个代码Agent基准测试，对比 verbalized confidence、白盒HTC等基线，用4B草稿模型对齐480B Qwen3-Coder、闭源Claude 3.5 Sonnet，可将执行错误率降低6~8个百分点，单任务token成本降低14~19%，无需在目标数据集重训即可实现跨分布、跨Agent迁移。
> 最值得记住的一句话：黑盒Agent的不确定性信号完全可以从输出轨迹本身提前获取，无需依赖模型内部信息，小成本的草稿模型打分即可大幅降低生产部署的错误与成本

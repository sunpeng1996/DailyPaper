---
title: 'Flide: Accelerating Decision Inference with Exact State Forking'
title_zh: Flide：基于精确状态分叉的决策推理加速引擎
authors:
- Bobo Li
- Jiajia Song
- Hao Fei
- Wynne Hsu
- Mong Li Lee
affiliations:
- National University of Singapore
- University of Oxford
arxiv_id: '2610.42148'
url: https://arxiv.org/abs/2610.42148
pdf_url: https://arxiv.org/pdf/2610.42148
published: '2026-10-30'
collected: '2026-11-02'
category: Agent
direction: Agent 决策推理引擎性能优化
tags:
- Inference Engine
- State Forking
- LLM Agent
- Efficient Serving
- ForkAttention
one_liner: 提出支持精确状态分叉的决策推理引擎Flide，比vLLM/SGLang最快快9.5倍，结果与单样本前向传播完全一致
practical_value: '- 电商智能客服、导购Agent的多分支决策场景（意图判定、合规校验、召回分支判定）可复用ForkAttention机制，共享用户上下文仅计算一次，无分隔符带来的概率偏移，精度更高且延迟降低数倍

  - 多轮交互推荐/导购Agent可复用增量状态分叉方案，checkpoint历史对话状态，每轮仅计算新增token和待判定分支，单步执行速度比vLLM提升4.4~7.2倍

  - 广告/推荐实时低延迟打分场景可复用Flat-Graph执行架构，用GPU常驻元数据存储请求依赖，少量预录制CUDA Graph即可覆盖不同请求组合，消除kernel
  launch开销提升吞吐'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前LLM Agent的决策类任务（路由、动作判定、结果打分）依赖的Jev等决策模型，现有生成式推理引擎要么重复计算共享前缀开销极高，要么多item打分引入分隔符破坏输出概率，动态批处理还会带来结果波动，无法同时满足高吞吐和精确性要求，成为Agent规模化落地的核心性能瓶颈。

### 方法关键点
- 核心思路将决策请求的逻辑树结构（共享上下文为树干，多个问题为分支）与物理执行层的扁平token流解耦，分支间计算互不干扰
- 提出ForkAttention，同时支持标准注意力层和Gated DeltaNet循环层的精确状态分叉，每个分支计算结果与独立前向传播完全一致，无需修改输入添加分隔符
- 设计Flat-Graph执行架构，请求依赖存储在GPU常驻元数据中，少量预录制CUDA Graph即可适配不同分支结构的请求，大幅降低kernel启动开销
- 支持增量状态分叉，可checkpoint历史状态，多轮Agent交互仅需计算新增token和分支，无需重算全量上下文

### 关键实验结果
在RACE、QuALITY、MultiRC等公开数据集上对比vLLM、SGLang、vllm-jev等主流引擎：多问题共享上下文场景下推理速度最高比vLLM/SGLang快9.5倍，吞吐量最高高8.5倍；Open-Jev决策模型上比专用vllm-jev引擎最快快3倍；输出与float32参考值的总变异距离最小，可选bitwise确定性模式下不同负载结果完全一致；多轮Agent轨迹场景下单步延迟比基线低一个数量级，每秒执行步数是最强基线的4.4~7.2倍。

### 核心结论
决策类推理不需要为了吞吐牺牲精度，通过逻辑结构与物理执行解耦的设计，可同时实现一个数量级的性能提升和严格的计算精确性。

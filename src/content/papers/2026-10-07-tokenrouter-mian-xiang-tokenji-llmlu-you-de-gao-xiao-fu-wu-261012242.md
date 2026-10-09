---
title: 'TokenRouter: Efficient Serving System for Token-Level LLM Routing'
title_zh: TokenRouter：面向Token级LLM路由的高效服务系统
authors:
- Tianyu Fu
- Tengxuan Liu
- Ruoxi Wang
- Yixin Dong
- Yi Ge
- Yichen You
- Yu Wang
affiliations:
- Tsinghua University
- Carnegie Mellon University
arxiv_id: '2610.12242'
url: https://arxiv.org/abs/2610.12242
pdf_url: https://arxiv.org/pdf/2610.12242
published: '2026-10-07'
collected: '2026-10-09'
category: LLM
direction: LLM服务 · Token级路由效率优化
tags:
- LLM-Serving
- Token-Level-Routing
- Inference-Optimization
- Scheduling
- Async-Execution
one_liner: 提出基于请求中心编程、模型中心执行的Token级LLM路由服务系统，吞吐量最高提升64.15倍
practical_value: '- 做LLM驱动的电商文案生成、导购Agent时，可直接复用Token级路由方案：简单内容用SLM生成，难生成内容路由到LLM，TokenRouter可直接作为落地框架，在保证质量的前提下降低推理成本

  - 复用延迟批调度（Delayed Batching）的工程思路，针对流量波动大的推荐/搜索Query理解场景，通过可控短等待聚合同模型请求，提升单卡推理吞吐量，降低SLO
  violations

  - 跨模型切换的handoff-resume机制可直接复用在多Agent协作场景，保留请求的KV cache状态避免重复计算，大幅降低Agent间调用的额外开销'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM服务系统都基于单模型假设设计，Token级路由（逐token切换大小模型，比query级路由能多省50%以上大模型调用量）落地时会遇到步骤失步、批次准入延迟、实现复杂度高三大问题，现有系统支持Token级路由时吞吐量损失严重，无法发挥Token级路由的成本优势。

### 方法关键点
- 核心设计遵循「请求中心编程，模型中心执行」原则：开发者只需实现`route`（判断每个请求下一步路由到哪个模型）、`send`（定义跨模型传递的状态）、`receive`（定义接收外部请求的状态转换）三个函数即可完成路由逻辑开发，无需感知底层调度细节
- 异步三循环执行架构：每个模型对应独立子服务，分别运行客户端交互、解码、跨模型通信三个异步循环，通过pending状态的handoff-resume机制保留请求KV cache，避免跨模型切换时重复计算
- 延迟批调度器：通过离散马尔可夫链数学模型推导最优批次阈值，短时间等待聚合同模型请求，降低批次碎片化，平衡等待延迟和批次利用率

### 关键结果
在AIME、CommonsenseQA、GSM8K、SWE-Smith等数据集上，对比5种Token路由算法官方实现、基于SGLang的标准服务基线，跨短输出推理、长输出推理、Agent任务三类workload，吞吐量提升2.01~64.15×，端到端延迟降低2.03~63.64×，在同等SLO约束下比query级路由的成本质量Pareto frontier更优。

### 核心结论
Token级路由的理论成本优势要落地，核心是解决跨模型调度的系统开销，而非仅优化路由算法本身。

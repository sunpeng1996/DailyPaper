---
title: 'CPU-ARC: Agentic Reasoning Caching for on-CPU Reasoning Reuse'
title_zh: CPU-ARC：面向CPU端推理复用的代理推理缓存
authors:
- Peter Belcak
- Greg Heinrich
- Saurav Muralidharan
- Shizhe Diao
- Pavlo Molchanov
affiliations:
- NVIDIA
arxiv_id: '2611.09891'
url: https://arxiv.org/abs/2611.09891
pdf_url: https://arxiv.org/pdf/2611.09891
published: '2026-11-05'
collected: '2026-11-09'
category: Agent
direction: Agent推理优化 · 低成本推理复用
tags:
- Reasoning Cache
- SLM
- CPU Inference
- Semantic Function
- Cost Optimization
one_liner: 将LLM推理轨迹转为CPU可执行语义函数缓存，调用成本较源大模型低16-291倍且效果持平
practical_value: '- 电商/推荐场景下的高频Agent推理任务（如促销规则计算、商品属性解析、客服标准问题应答）可复用该思路，将大模型推理轨迹固化为语义函数缓存，大幅降低大模型调用成本与响应延迟

  - 可借鉴语义函数的自然语言绑定设计，无需固定函数/参数标识符，新增或迭代业务规则时无需修改现有调用逻辑，适配电商业务规则快速迭代的需求

  - 采用「大模型处理低频新场景→积累足够样本后构建ARC缓存→高频场景切缓存」的链路，平衡效果与成本，如广告投放的定向规则判定、订单合规校验等场景均可套用

  - 缓存成熟后可编译为纯Python可执行文件，移除向量检索依赖，进一步降低延迟，可直接部署在边缘节点或端侧轻量Agent中'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM每次推理均从零开始，Agent系统中大量同逻辑不同参数的重复推理任务会造成极高的算力浪费与延迟；传统KV缓存、语义缓存仅能匹配完全相同或语义相似的请求，对参数变化的同逻辑任务泛化性差，且无法保证结果正确性。
### 方法关键点
- 核心将源大模型的推理Trace拆解为可独立复用的语义函数，每个函数为CPU可执行的Python代码，输入输出、子函数调用均通过自然语言描述做语义匹配，无需固定标识符
- 缓存构建仅在首次处理任务时执行，分输入输出隔离、推理步骤拆解、可变参数识别、执行计划生成、代码校验5个阶段，仅构建阶段需要用到大模型，推理阶段仅需SLM与CPU执行
- 支持缓存编译，成熟后可将动态语义查找替换为直接函数调用，完全移除向量检索依赖，进一步降低推理延迟
### 关键结果
在MATH-500、AIME、GPQA、GSM8K等8个数学/科学推理基准上测试，缓存准确率与源大模型持平甚至更高，对表述改写、参数变化的扰动通过率均超过90%；调用成本较源大模型低16~291倍，构建成本为单次源大模型调用的12~84倍，高频场景下13~90次调用即可覆盖构建成本实现盈利。
### 核心结论
对于高频重复的同逻辑推理任务，将大模型的推理过程固化为CPU可执行的代码，是比微调小模型、语义缓存更高效、更可靠的降本方案

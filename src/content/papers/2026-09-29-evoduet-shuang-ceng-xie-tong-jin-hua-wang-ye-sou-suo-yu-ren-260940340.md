---
title: 'EvoDuet: Bilevel Co-Evolution of Web Searching and Task Solving for Scientific
  Discovery'
title_zh: EvoDuet：双层协同进化网页搜索与任务求解的科学发现框架
authors:
- Young-Jun Lee
- Jinheon Baek
- Soyeong Jeong
- Minki Kang
- Seungyeon Jwa
- Jonghyun Choi
- Seungho Han
- Dongyeop Kang
affiliations:
- University of Minnesota
- KAIST
- Seoul National University
- Hanyang University
arxiv_id: '2609.40340'
url: https://arxiv.org/abs/2609.40340
pdf_url: https://arxiv.org/pdf/2609.40340
published: '2026-09-29'
collected: '2026-10-01'
category: Agent
direction: Agent 工具调用与进化优化
tags:
- LLM Agent
- Evolutionary Search
- Web Retrieval
- Bilevel Optimization
- Scientific Discovery
one_liner: 提出双层协同进化框架，同步优化web查询与任务解，提升LLM驱动的进化搜索效果
practical_value: '- 可复用知识缺口检索门逻辑：在电商导购Agent、搜索Query优化场景中，让LLM自主判断是否需要调用检索、复用历史检索结果还是直接生成，降低无效检索成本

  - 可迁移查询进化+假设证据评分机制：在生成式推荐的Item冷启动、营销文案迭代场景中，基于预期效果评分迭代检索Query，提升外部知识匹配精准度

  - 可复用双层循环架构：在A/B测试迭代、推荐排序策略自动优化场景中，外层优化策略/候选，内层优化检索/信息输入，减少无效尝试成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM驱动的进化搜索仅依赖模型参数知识和迭代历史，引入外部知识时查询固定易重复检索相同内容，导致搜索停滞，无法解决需要外部新知识的优化任务。

### 方法关键点
- 双层协同进化架构：外层循环优化候选解决方案，内层循环优化web搜索查询，两层共享任务目标
- 知识缺口检索门：LLM自主判断当前知识状态，选择三种操作：无检索直接生成、复用历史存储文档、发起新检索
- 内层假设证据评分：无需实际生成候选，直接预测检索到的文档能带来的方案得分，基于得分迭代查询、筛选高价值文档
- 并行候选生成：检索到高价值文档时并行生成多个候选，提升探索效率

### 关键实验结果
在21个科学优化任务上对比基线OpenEvolve：
- 单候选每轮时，GPT-5.6-Luna的归一化发现增益(NDG)从74.1%提升至78.0%，Gemini-3.8-Flash从61.3%提升至82.3%，但Qwen3.5-9B无增益甚至性能下降
- 超越8个任务的之前SOTA得分，平级3个任务，在去噪任务上达到同等效果成本仅为之前SOTA的1/6.9
- 兼容Top-K、EvoX等现有进化搜索框架，均能带来稳定增益

> 最值得记住：协同进化的收益和基座LLM能力强相关，弱模型无法正确判断知识缺口、应用检索知识，反而会被检索内容干扰导致性能下降

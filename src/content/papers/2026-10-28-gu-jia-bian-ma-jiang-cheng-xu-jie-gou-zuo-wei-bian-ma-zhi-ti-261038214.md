---
title: 'Skeleton Coding: Program Structure as a Specification for Agents'
title_zh: 骨架编码：将程序结构作为编码智能体的开发规范
authors:
- Aditya Golatkar
- Alessandro Achille
- Renos Zabounidis
- Vlad Sobal
- Yangruibo Ding
- Baishakhi Ray
- Jonathan Buck
- Guy Van den Broeck
- Maryam Fazel
- Pietro Perona
affiliations:
- AWS Agentic AI
- Amazon
arxiv_id: '2610.38214'
url: https://arxiv.org/abs/2610.38214
pdf_url: https://arxiv.org/pdf/2610.38214
published: '2026-10-28'
collected: '2026-10-30'
category: Agent
direction: Agent 编码智能体开发范式优化
tags:
- CodingAgent
- SkeletonCoding
- LLM4Code
- AgentSpecification
- ProgramSynthesis
one_liner: 提出开发者预先指定代码结构骨架的编码范式，大幅降低编码智能体的测试需求与错误率
practical_value: '- 做业务Agent开发时，不要仅通过Prompt给出行为约束，需预先定义模块拆分、函数签名、数据结构等骨架，可大幅降低生成结果错误率，减少调试成本，例如电商营销活动生成Agent，先定优惠计算、库存校验、人群匹配模块接口，比仅给规则准确率高30%以上

  - 结构约束可缩小大小模型效果gap，内部Agent工具可先定义骨架，用Qwen3.8-27B级别小模型即可达到接近大模型的效果，推理成本降15~26倍，适合推荐系统特征工程、规则生成等高并发低延迟场景

  - 迭代式Agent开发时保留骨架作为不变量，可降低24.7%的代码侵蚀概率，避免业务逻辑迭代过程中旧逻辑被意外破坏，例如推荐策略迭代Agent每次仅修改对应模块实现，骨架不变可降低回测成本30%以上'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有编码智能体仅依赖端到端测试、输入输出示例等行为约束，无法保证生成代码符合开发者预期：不同代码结构需要的测试用例数量差异极大，开发者无法提前预判需要多少测试覆盖边缘case，且架构层面的可维护性、性能要求等根本无法通过端到端测试验证，导致生成代码错误率高、迭代成本高、代码质量差。

### 方法关键点
- 提出Skeleton Coding范式：开发者预先指定代码结构骨架，包括数据类型、模块边界、函数签名、数据流向、单函数前后置约束、全局不变量，仅将具体实现交给编码智能体完成
- 理论证明合理骨架可指数级降低测试需求：一是缩小代码搜索空间，二是暴露中间状态支持局部测试，三是可直接定义测试无法覆盖的架构约束
- 骨架支持版本管理、评审，可作为迭代过程的不变量避免代码侵蚀

### 关键实验
在SCBench、SDDBench、ProgramBench三个代码生成基准上测试GPT-5.6 Sol、GPT-5.6 Luna、Qwen3.8-27B、GLM5.2四个模型，对比仅任务描述、端到端行为约束、自然语言架构文档等baseline：骨架编码相比最优端到端行为约束平均降低测试错误率48.4%；即使提供完整参考实现Oracle，加骨架仍可降低错误率27%；缩小大小模型效果差距52.4%，实现成本降15~26倍；平均降低代码侵蚀24.7%。

### 核心结论
对于智能体的任务约束，先定结构再定行为，比仅给行为约束的效率和效果高一个数量级。

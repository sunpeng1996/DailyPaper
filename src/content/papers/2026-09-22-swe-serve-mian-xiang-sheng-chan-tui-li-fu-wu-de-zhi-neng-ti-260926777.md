---
title: 'SWE-Serve: Benchmarking Agentic Engineering For Production Inference Serving'
title_zh: SWE-Serve：面向生产推理服务的智能体工程能力评测基准
authors:
- Jennifer Williams
- Dave Farris
- Jeff Farris
- Jiantao Jiao
affiliations:
- NVIDIA
- University of California, Berkeley
arxiv_id: '2609.26777'
url: https://arxiv.org/abs/2609.26777
pdf_url: https://arxiv.org/pdf/2609.26777
published: '2026-09-22'
collected: '2026-09-23'
category: Agent
direction: Agent 生产级推理工程能力评测
tags:
- AgentEvaluation
- InferenceServing
- ProductionBenchmark
- SWEAgent
- CodeAgent
one_liner: 推出53个SGLang生产环境衍生的推理工程任务基准，量化Agent本地实现到生产可用的正确性差距
practical_value: '- 维护推荐/广告/RAG等大模型推理服务时，可复用这套测试逻辑：除单元/集成测试外，必须加端到端服务级校验，避免本地跑通上线失效

  - 评测内部代码Agent能力时，可参照SWE-Serve的任务构造方法，基于自研推理栈构建贴合业务的私有评测集，更真实反映落地能力

  - 推理服务的测试体系可参考其分层设计：F2P测新功能正确性、P2P做回归防护、E2E测生产链路可用性、性能门限校准保障延迟达标'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有代码智能体评测基准对生产推理工程场景覆盖不足：通用软件工程基准不针对推理服务，推理性能基准仅测孤立Kernel优化或局部任务，无法量化「本地实现正确→生产链路可用」的正确性差距，大量Agent生成的补丁通过局部测试但上线后失效。
### 方法关键点
- 任务基于2025年12月后SGLang合并的生产PR构建，共53个可执行任务，覆盖模型适配、解码优化、KV cache管理、分布式调度、服务API开发等6大类推理工程场景，支持CPU/单H100运行
- 测试体系分层设计：F2P测试验证新增功能正确性、P2P测试保障原有功能无回归、E2E测试校验完整服务链路的生产正确性，配套性能门限校准、对抗性验证保障任务有效性
- 闭-book评测规则，禁止Agent检索上游PR解决方案，全流程轨迹审计保障评测公平性
### 关键结果
- 测试11个前沿大模型+31种推理努力配置，最优配置（Claude Opus 5、GPT-5.6 Sol）的pass@1达75%
- 剔除E2E测试后，19个带E2E任务的平均通过率从45.9%提升至69.4%，约1/3通过局部测试的补丁无法通过生产链路校验
- 跨多运行时域的任务通过率比单域任务低21.3pp，要求持久状态/并发协调的GPU任务通过率分别低20.8pp、29.0pp

**最值得记住的一句话**：Agent生成的代码本地跑通离生产可用至少有23个百分点的差距，全链路E2E测试是推理服务上线不可替代的校验环节。

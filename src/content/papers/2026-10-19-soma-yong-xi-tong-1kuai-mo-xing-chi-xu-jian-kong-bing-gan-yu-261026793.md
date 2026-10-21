---
title: 'SOMA: Continuous Monitoring and Intervention for System Two Reasoning with
  System One Models'
title_zh: SOMA：用系统1快模型持续监控并干预系统2推理过程
authors:
- Ruizhi Qian
- Lei Shi
- Tianyu Hu
- Bo Yan
- Song Wang
- Yu Tian
affiliations:
- University of Central Florida
arxiv_id: '2610.26793'
url: https://arxiv.org/abs/2610.26793
pdf_url: https://arxiv.org/pdf/2610.26793
published: '2026-10-19'
collected: '2026-10-21'
category: Reasoning
direction: 大语言模型推理 · 双系统认知监控
tags:
- Dual-Process
- Reasoning
- Metacognition
- Inference Optimization
- Black-box Control
one_liner: 基于双系统认知框架，用无训练S1快模型全程监控S2推理，减少冗余计算同时提升推理质量
practical_value: '- 可复用三层架构搭建业务Agent的监控体系：用轻量快模型（小分类LLM、规则引擎替代）全程监控电商导购/客服Agent的思考、对话轨迹，无需修改Agent本体，仅通过自然语言定义违规行为、提醒语、接管动作，即可快速适配违规推荐、偏离用户意图等风险场景。

  - 推理成本优化：针对生成式推荐文案创作、RAG问答等业务的冗余推理问题，复用先提醒后接管的两阶段控制逻辑，定期扫描推理文本累计置信度触发干预，无需训练即可降低推理token消耗，缩减推理成本。

  - 黑盒大模型干预方案：业务侧仅能调用商用大模型API、无白盒权限时，可复用纯文本观测的设计，无需访问模型隐层状态即可实现推理干预，适配无模型开发权限的业务场景。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
当前S1快模型仅作为S2推理前的路由网关，S2启动后无实时监控，易出现重复验证、明知缺失信息仍强制输出等冗余或错误推理问题；现有推理监控方案大多需要训练、白盒访问权限，单场景适配成本高，难以快速复用。
### 方法关键点
- 三层架构设计：场景层用纯自然语言定义监控规则（含行为描述语句、干预提醒语、最终接管动作），感知层调用S1模型定期扫描S2推理文本输出行为发生概率，控制层累计对数几率证据，先触发提醒、行为持续才执行接管。
- 无训练黑盒适配：无需修改S2模型参数，无需额外训练，新增监控场景仅需调整自然语言规则即可快速上线。
- 轻量阈值校准：仅需百级样本的小校准集即可选择接管阈值，平衡干预收益与误接管风险。
### 关键实验
在过思考、不可答问题两个场景验证，S2选用Qwen3-8B、DeepSeek-R1-Distill-Llama-8B，S1选用Jev，对比BF、DEER、Dynasor-CoT等基线：过思考场景下分别降低36%、16%推理token，平均准确率分别提升0.3、0.4个百分点；不可答问题场景下分别提升16.7、21.2个百分点的拒答率，同时降低32%、48%推理token。
### 最值得记住的一句话
S1快模型可作为通用推理监控层而非仅作为推理前网关，仅靠自然语言规则即可实现跨场景的无训练黑盒推理干预。

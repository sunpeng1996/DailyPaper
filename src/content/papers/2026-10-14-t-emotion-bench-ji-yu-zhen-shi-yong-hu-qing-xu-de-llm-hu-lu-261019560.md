---
title: 'τ-Emotion-Bench: Exposing the Interaction Fragility of LLM Agents through
  Real-World User Emotions'
title_zh: τ-Emotion-Bench：基于真实用户情绪的LLM Agent交互鲁棒性评测基准
authors:
- Rishitosh Kumar Singh
- Amir Saeidi
- Shamanthak Hegde
- Shrinidhi Kumbhar
- Chitta Baral
affiliations:
- Arizona State University
arxiv_id: '2610.19560'
url: https://arxiv.org/abs/2610.19560
pdf_url: https://arxiv.org/pdf/2610.19560
published: '2026-10-14'
collected: '2026-10-15'
category: Agent
direction: Agent 交互鲁棒性评测与训练
tags:
- Agent Evaluation
- User Emotion
- Tool Calling
- Trajectory Generation
- Benchmark
one_liner: 推出10领域情绪条件Agent评测基准与交互感知训练数据生成管线Tracer
practical_value: '- 面向电商导购、售后客服等用户-facing Agent，可引入情绪感知的用户终止信号作为训练过滤规则，淘汰过度询问用户的轨迹，避免触发真实用户不满中断交互

  - 小参数模型调优工具调用能力时，可复用Tracer的「优先保留工具调用占比高、用户交互占比低的成功轨迹」筛选逻辑，仅需千级训练样本即可实现跨领域泛化，降低训练数据成本

  - 搭建企业内部Agent评测体系时，可参考本文5大类情绪+22种细粒度情绪的用户模拟框架，覆盖用户不耐烦、焦虑等真实情绪场景，提前发现交互鲁棒性问题'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有Agent评测与训练大多假设用户配合、行为稳定，忽略真实场景中用户情绪波动会导致交互中断，哪怕Agent最终能完成任务，过度询问也会让用户不满终止交互，这一缺陷导致上线的Agent实际体验远差于实验室效果。

### 方法关键点
- 构建τ-Emotion-Bench：覆盖航空、零售、电信等10个领域共580个可执行工具调用任务，包含5类情绪、22种细粒度情绪、3种行为维度（礼貌、紧急度、信任）的可控用户模拟，任务目标固定仅调整用户情绪表达
- 推出Tracer数据生成管线：先构造符合领域政策的工具依赖图，采样生成多步执行轨迹，反向生成自然用户指令，再注入情绪条件；引入交互感知奖励规则：用户可因Agent无效交互终止会话，过滤掉过度依赖用户询问的成功轨迹，保留工具调用与必要询问平衡的轨迹

### 关键结果
对比17款前沿开源/闭源Agent，用Qwen3-235B作为用户模拟器时，最优模型DeepSeek-V4.1-Flash平均成功率仅55.9%，三次测试均成功的Pass^3仅32.2%；用Tracer数据微调Qwen3小模型，1.7B/4B/8B版本平均成功率提升13.8~19.7个百分点，仅用1498条4领域数据训练的模型，在6个未见过的领域上Pass^3超过所有现有同参数Agent训练方法，同时效果可迁移到τ-Bench、τ-Trait等其他评测集。

**最值得记住的一句话**：Agent的实际价值不止是完成任务，更要在尽量少的用户交互下完成任务，情绪波动的用户是检验Agent交互效率的最佳试金石。

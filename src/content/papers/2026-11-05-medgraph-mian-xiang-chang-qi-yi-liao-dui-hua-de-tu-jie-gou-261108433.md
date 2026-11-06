---
title: 'MedGraph: Maintaining Patient State with Graph Memory for Long-Term Medical
  Dialogue'
title_zh: MedGraph：面向长期医疗对话的图结构患者状态记忆系统
authors:
- Donghua Zhang
- Zizheng Wang
- Ze Dong
- Yiding Feng
- Siyu Qian
affiliations:
- University of Michigan
- Georgetown University
- Johns Hopkins University
- Harvard University
arxiv_id: '2611.08433'
url: https://arxiv.org/abs/2611.08433
pdf_url: https://arxiv.org/pdf/2611.08433
published: '2026-11-05'
collected: '2026-11-06'
category: Agent
direction: Agent 长周期记忆架构优化
tags:
- LLM Agent
- Graph Memory
- Long-term Memory
- Fact Extraction
- Medical Dialogue
one_liner: 针对长期医疗对话三类记忆错误，提出多层图记忆系统，跨骨干模型准确率领先超10个百分点
practical_value: '- 可复用Bad case归因框架：先采样错误样本统计核心问题，再针对性设计记忆方案，可直接迁移到电商导购、用户运营等Agent的记忆系统排障和迭代

  - 分层记忆架构可直接复用：L1存原始交互文本、L2存带时间/主体标签的结构化事实链、L3存高优先级用户偏好（如禁忌、过敏、预算上限），每次回答强制携带L3内容，避免遗漏关键约束

  - 事实链检索策略适配时序偏好场景：将同一用户+同一商品/偏好类型的历史记录组成时序链，检索时以链为单位返回对应时间点的状态，可解决用户偏好变化回溯、消费行为时序推理的问题

  - 主体归属绑定机制：抽取事实时显式绑定归属主体，检索时仅返回目标主体的事实，可避免多用户咨询、代人咨询场景下的信息错配，适合家庭账号、企业账号的多角色推荐场景'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有通用LLM记忆系统（RAG、GraphRAG、Mem0等）在长周期多轮对话场景中存在三类高频错误：返回过时状态、错配信息归属主体、遗漏高优先级关键信息，在医疗对话等高风险场景会直接导致有害建议，现有方案无法适配长时序、多主体、高安全要求的记忆需求。
### 方法关键点
1. 三层记忆架构：L1留存原始对话文本作为溯源依据；L2构建带时间戳、主体归属、类型标签的结构化事实图，同一主体+实体+类型的事实组成时序链，通过supersedes边关联新旧状态，保留完整历史；L3为高优先级画像，全量存储安全类事实（过敏、禁忌等），每次回答强制携带，无需检索匹配。
2. 低开销记忆构建：每轮对话仅调用1次LLM抽取结构化事实，自动解析相对时间、标准化实体、绑定归属主体，重复事实不新增节点仅更新提及时间，大幅降低构建成本。
3. 精准检索逻辑：仅召回目标主体的事实，以事实链为检索单位，返回匹配事实、问题对应时间点的状态、前序状态，补充因果关联事实和对应时间窗口的原始对话片段，保证时序推理的准确性。
### 关键结果
在MedMemoryBench的967个长周期医疗对话问题上测试，对比Embedding RAG、Mem0、MemOS等5个主流记忆系统：GPT骨干下整体准确率达51.9%，比最强基线高10.5个百分点；Qwen开源骨干下准确率达46.1%，比最强基线高10.4个百分点；记忆构建Token消耗仅为Mem0、REMem的一半，单问题响应速度为所有方案最快。
### 核心结论
长周期Agent记忆的性能收益超过一半来自结构化事实抽取，而非复杂的检索策略

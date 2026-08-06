---
title: Hierarchical Graph Memory for LLM Agents with Path-level Localization and Rewrite
title_zh: 面向LLM Agent的支持路径级定位与重写的层次化图记忆框架
authors:
- Xiawei Yue
- Boran Wang
- Xiaoqing Zhang
- Shuxin Zheng
- Ziwei Zhang
affiliations:
- Nankai University
- Zhongguancun Academy
- Beihang University
arxiv_id: '2608.05095'
url: https://arxiv.org/abs/2608.05095
pdf_url: https://arxiv.org/pdf/2608.05095
published: '2026-08-05'
collected: '2026-08-06'
category: Agent
direction: Agent长时记忆 · 层次化图结构优化
tags:
- LLM Agent
- Graph Memory
- Hierarchical Memory
- Memory Update
- Long-term Reasoning
one_liner: 提出层次化图记忆框架HiGram，大幅提升LLM Agent长时推理的回答质量与Token效率
practical_value: '- 电商客服Agent、个性化推荐Agent的长时用户记忆可复用这套层次化存储结构：上层按用户ID、商品类目做粗索引，下层存储具体交互/偏好事实，减少检索无关内容，降低Token消耗。

  - 用户偏好变更、商品上下架等记忆更新场景，可借鉴路径级定位+协同重写机制：先定位受影响的关联记忆路径，再同步更新记忆单元和依赖关系，避免反复检索全量记忆，同时解决记忆冲突问题。

  - 做Agent记忆性能优化时可参考这套评估思路：除回答准确率外，新增Token效率、冲突场景下的一致性指标，更贴合业务落地的成本与可靠性要求。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有LLM Agent的图记忆多采用扁平结构，随着历史记忆累积，检索会引入大量无关上下文，证据选择成本高；且更新时仅独立修改单个记忆单元，需反复重写才能覆盖关联变更，Token消耗高、记忆一致性差，无法适配长时推理、动态记忆更新的需求。

### 方法关键点
- 层次化图记忆架构：上层设主体、对象类目、上下文三类抽象节点，下层存储细粒度记忆单元与显式依赖边，实现粗到细的记忆索引，无需遍历全量记忆即可定位相关区域。
- MicroGraph路径级定位：基于主体+类目构造局部子图作为检索锚点，收到查询和更新请求时，先提取临时记忆单元的锚点匹配候选MicroGraph，构造支持子图后再筛选出受影响的证据路径，锁定重写范围。
- 协同重写机制：在定位到的路径内同步执行单元内重写（更新记忆单元状态、有效期）和单元间重写（调整依赖边、标记失效关联记忆），无需修改路径外内容。

### 关键结果
在LoCoMo长时对话QA数据集上，对比Mem0、A-MEM、MemGPT、ReadAgent等基线，基于GPT-4o时平均F1达52.51，相对次优方案提升10.3%，Token消耗仅为全上下文方案的8.2%；在MemConflict记忆冲突数据集上，整体Macro-AA达67.84%，相对次优方案提升22.5%，证据检索SEH@3达81.06%。

### 核心结论
Agent记忆优化的核心是让存储、检索、更新的粒度和推理所需的证据结构粒度对齐，而不是盲目扩大上下文窗口或者增加记忆容量。

---
title: 'PACE: Towards Surfacing Hidden Conflicts in User Requests'
title_zh: PACE：面向用户请求隐性冲突的检测基准与多Agent框架
authors:
- Yoojin Kim
- Jihyoung Jang
- Hyounghun Kim
affiliations:
- Department of Computer Science and Engineering, POSTECH
- Graduate School of Artificial Intelligence, POSTECH
arxiv_id: '2609.03293'
url: https://arxiv.org/abs/2609.03293
pdf_url: https://arxiv.org/pdf/2609.03293
published: '2026-09-02'
collected: '2026-09-04'
category: Agent
direction: Agent 个人助理冲突感知推理
tags:
- Multi-Agent
- RAG
- Conflict Detection
- Personal Assistant
- Benchmark
one_liner: 提出用户请求隐性冲突检测基准PACE与多Agent检索框架PACEMAKER，提升上下文决策准确率
practical_value: '- 搭建电商/生活服务类个性化Agent时，可复用冲突感知查询规划逻辑：对用户的预约、下单类请求，生成反事实探测查询（如「该请求是否和用户已有行程冲突」「是否违反同行人饮食禁忌」），定向召回用户知识库中弱关联的约束证据，避免误执行不符合用户隐性需求的请求

  - 检索融合阶段可引入Weighted RRF策略，给冲突探测类查询的召回结果分配更高权重，在不降低语义相关性召回效果的前提下，提升决策关键证据的优先级，适合需要风险判断的推荐/助理场景

  - 对于分散存储的用户长周期行为、属性、社交关联知识，可预构建KNN语义关联图，采用BFS多跳遍历扩展召回池，解决单步检索无法覆盖弱关联冲突证据的问题，提升复杂约束下的决策准确率

  - 大模型推理前必须经过多轮Agent过滤筛选决策相关证据，直接喂全量KB会导致大模型推理准确率下降10pct以上，该结论可直接复用在所有基于个人知识库的LLM应用中'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有个性化助理普遍仅关注用户请求的执行准确性，忽略了请求与用户隐性约束（行程、偏好、环境状态、关联人限制等）的潜在冲突；现有冲突检测方法依赖输入中的显式风险信号，而真实场景中冲突证据往往分散存储在个人知识库，与原始请求语义关联度极低，单步检索难以召回，导致助理要么盲目执行错误请求，要么过度拒绝合理请求，严重影响用户体验。
### 方法关键点
- 构建PACE基准数据集：包含3.2K条表面合理的用户请求、对应个人知识库（单实例平均2035条原子事实，单请求平均需4条事实联合判断），覆盖时间、个人、状态三类冲突场景，与人类判断一致性达93.3%
- 提出PACEMAKER多Agent检索框架：1）冲突感知查询规划：生成原始查询+多组反事实冲突探测查询，定向挖掘隐性约束证据；2）混合检索融合：采用Weighted RRF加权融合稠密/稀疏检索结果，反事实查询结果权重更高；3）多跳图遍历：基于预构建的KNN知识图做BFS多跳扩展，覆盖弱关联冲突证据；4）两轮冲突过滤：检索前、遍历后分别过滤无关文档，仅保留决策核心证据
### 关键实验结果
在PACE数据集上对比全量KB、稀疏/稠密检索、GraphRAG、HippoRAG等基线，采用GPT-5.4-mini配置时，PACEMAKER的Recall@5达36.05%，整体PASS率达75.35%，冲突类请求PASS率达59.17%，相比最强检索基线分别提升16.28pct、9.82pct、18.9pct，仅比Oracle上限低11.78pct。
### 核心结论
隐性冲突检测的核心不是召回语义最相关的文档，而是定向召回所有能判断请求可行性的决策关键证据，哪怕证据与原始请求语义关联度极低

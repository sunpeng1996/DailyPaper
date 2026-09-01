---
title: 'MedCache: Efficient and Temporally Valid Memory for Longitudinal Clinical
  Agents'
title_zh: MedCache：面向纵向临床Agent的高效时序有效记忆框架
authors:
- Hei Ting
- Chan
- Chenwei Wu
- Xueshen Liu
- Boyuan Zheng
- Liyue Shen
- Jiasi Chen
- Z. Morley Mao
affiliations:
- University of Michigan, Ann Arbor
arxiv_id: '2608.29528'
url: https://arxiv.org/abs/2608.29528
pdf_url: https://arxiv.org/pdf/2608.29528
published: '2026-08-30'
collected: '2026-09-01'
category: Agent
direction: Agent 长时序记忆优化
tags:
- Agent_Memory
- Temporal_Validity
- Multi_Agent
- RAG
- Longitudinal_Reasoning
one_liner: 提出结合时序校验、重叠专科视图、自适应推理的混合Agent记忆框架，性能效率双优
practical_value: '- 时序记忆过滤Trick：长时序用户行为/偏好记忆不要全量存储，给每个行为打有效时间窗，自动过滤过期无效行为（如用户半年前的婴幼儿商品需求自动失效），大幅减少无效上下文干扰，提升推理准确率

  - 重叠分域内存设计：用户特征/行为不要按业务域严格隔离，跨域共享特征（如价格敏感属性）同步存入所有相关域的内存分区，避免跨域检索时特征漏召回

  - 路由+自适应推理架构：先通过轻量分类器做查询路由，简单查询（如历史订单查询）走单Agent处理，复杂跨域查询（如大促凑单推荐）走多Agent协同，同时可复用稳定业务规则前缀的KV
  cache，平衡准确率、推理成本与延迟

  - 评测基准构建思路：长上下文记忆系统评测需单独覆盖长上下文检索、跨时间聚合、跨域推理三类任务，便于定位错误根因'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
纵向医疗Agent需要维护跨就诊、跨专科的动态患者状态，但现有单/多Agent记忆系统普遍存在三类问题：过时证据干扰推理、严格专科分区导致共享证据遗漏、多Agent推理成本过高，且缺乏针对性的长时序记忆评测基准。

### 方法关键点
- 构建LEMMA-Bench评测基准：基于MIMIC-IV数据集的91例平均病史跨度5.8年的多专科就诊记录，覆盖长上下文证据检索、跨时间证据聚合、跨专科推理三类核心任务
- MedCache两阶段混合架构：1）离线层：将诊疗记录转化为带生效时间窗的标准化事实，分配到重叠的专科内存分区，共享事实跨分区存储同一ID便于去重；2）查询层：通过轻量门控路由筛选相关专科内存，自适应选择推理路径：单域查询走单Agent直接回答，跨域查询走多专科Agent协同后由协调器输出结果
- 工程优化：利用vLLM前缀缓存复用稳定的专科指南前缀，降低推理延迟

### 关键结果
- 相比最优基线ClinicalAgents，MedCache推理准确率提升2.1pct至93.6%，单查询输入Token从31.5k降至8.7k，压缩3.6倍，位于准确率-效率帕累托前沿
- 新增大量过时/无关干扰证据时，MedCache准确率稳定在70.8%，远高于RAG的20.8%、全量上下文基线的33.3%
- 专科指南模块从8个扩容到24个时，MedCache首Token延迟稳定在0.165s，中心化系统延迟从0.212s升至0.716s，MedCache延迟优势扩大到4.34倍

> 最值得记住的结论：长时序记忆系统的核心瓶颈不是存储的历史总量，而是保留有效信息、灵活组织跨域关联、按需调用推理资源的能力

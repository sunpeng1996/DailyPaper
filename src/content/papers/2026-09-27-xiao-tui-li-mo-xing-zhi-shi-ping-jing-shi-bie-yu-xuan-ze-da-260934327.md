---
title: 'Knowing When Thinking Is Not Enough: Teaching Small Reasoning Models to Reason
  Beyond Their Parametric Knowledge'
title_zh: 小推理模型知识瓶颈识别与选择性大模型调用框架FlyBy
authors:
- Chanuk Lee
- Minki Kang
- Sangwoo Park
- Woongyeong Yeo
- Jinheon Baek
- Sung Ju Hwang
affiliations:
- KAIST
- DeepAuto.ai
arxiv_id: '2609.34327'
url: https://arxiv.org/abs/2609.34327
pdf_url: https://arxiv.org/pdf/2609.34327
published: '2026-09-27'
collected: '2026-09-29'
category: Agent
direction: Agent 推理瓶颈诊断与外部资源调度
tags:
- Small Reasoning Model
- Tool Use
- Reinforcement Learning
- Cost Optimization
- Reasoning Bottleneck
one_liner: 提出区分执行与知识瓶颈的FlyBy框架，让小推理模型选择性调用大模型，以更低成本超过更大参数量模型
practical_value: '- 可复用执行/知识瓶颈的二分诊断逻辑，在电商导购Agent、推荐解释生成场景中，区分是模型推理逻辑错误还是缺少商品/活动的最新参数知识，避免无意义的自迭代浪费算力

  - 多深度query+成本感知RL的训练范式可直接迁移到推荐系统的小模型调用大模型场景，先用SFT bootstrapped工具调用行为，再用RL校准调用时机和算力分配，平衡效果和推理成本

  - 可借鉴「先推理再精准求助」的设计，替代现有RAG/大模型调用的前置检索逻辑，在搜索Query理解、商品问答场景中，先推理缺失信息再定向检索/调用，降低无效检索开销'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
小推理模型（sRM）部署成本远低于大模型，是端侧推理、低成本Agent的核心选型，但现有通过延长推理链、自精炼优化的方式仅能修复逻辑执行错误，无法填补参数知识缺失的瓶颈；盲目的前置RAG/大模型调用又会带来不必要的成本开销，亟需可动态决策是否、何时、调用多少算力外部资源的方案。

### 方法关键点
- 通过反事实干预验证sRM推理失败分为两类：执行瓶颈（正确解可通过自精炼得到）、知识瓶颈（必须补充外部信息才能解决），自精炼仅对执行瓶颈有效；
- 设计多深度query工具，3个深度层级对应不同能力、成本的外部大模型，禁止外部模型获取原问题避免答案泄露；
- 两阶段训练：先用SFT在少量救援轨迹上bootstrapped模型的工具调用、外部信息整合能力，再用成本感知RL优化GRPO目标，仅对成功推理的轨迹惩罚调用成本，让模型优先用内部推理，仅在知识瓶颈时选择成本适配的外部服务。

### 关键实验
在6个覆盖数学、科学、医学的推理基准共1158道难题上测试：
- FlyBy-4B（基于Qwen3-4B）pass@8达45.96%，超过Qwen3-14B的41.64%，服务成本低2.7倍，pass@1也超过Qwen3-8B；
- FlyBy-8B pass@8达51.81%，比Qwen3-8B提升17.58pp，成本还低4.1%；
- 效果优于自精炼、前置检索、提前调用大模型等所有基线，在越难的问题上优势越大。

### 核心结论
有效的测试时间算力优化，不仅要决定花多少算力，还要判断当前状态需要什么类型的算力（内部推理还是外部求助）

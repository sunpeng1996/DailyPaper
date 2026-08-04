---
title: Global Optimization and Inference-Time Region Grafting for Agentic Workflows
title_zh: 面向智能体工作流的全局优化与推理时区域嫁接框架GRAFT
authors:
- Donghyeok Koh
- Gyuwan Kim
- Jinyeong Bak
- Seung-Hoon Na
- Tao Yang
- Haneol Jang
- Cheoneum Park
affiliations:
- HBNU
- UCSB
- SKKU
- UNIST
arxiv_id: '2608.02353'
url: https://arxiv.org/abs/2608.02353
pdf_url: https://arxiv.org/pdf/2608.02353
published: '2026-08-03'
collected: '2026-08-04'
category: Agent
direction: Agent 工作流推理时动态优化
tags:
- Agentic Workflow
- Inference-time Adaptation
- Training-free
- Local Search
- Cache Amortization
one_liner: 提出无训练的GRAFT框架，推理时局部替换智能体工作流区域适配单输入，性能超SOTA 3.85点
practical_value: '- 电商/广告多轮Agent服务（智能导购、售后答疑、推荐理由生成）可复用SESE区域拆分思路，离线先构造全局最优工作流，推理时仅替换故障区域，避免全链路重排的高成本

  - 无标注场景下的模块效果评估可直接复用label-free proxy组合：自一致性、证据groundedness、验证器信号（如代码跑通率、用户点击反馈），无需标注数据即可做局部算子的效果判断

  - 高并发Agent服务可落地配置缓存机制，按输入类型签名缓存效果达标的区域配置，后续相似请求直接复用，搜索成本可降低50%以上，适配标准化程度高的电商咨询、选品Agent等场景

  - 耦合guard机制可迁移到多模块推荐系统，替换局部召回/排序模块时加边界一致性校验，避免局部优化导致的全链路效果下降'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有智能体工作流优化要么离线搜索全局固定结构，无法适配不同输入的难度与推理需求，要么推理时全工作流重优化，计算成本极高，且替换局部模块易导致下游错误传播，无法兼顾全局稳定性和单输入适配性。

### 方法关键点
- 离线阶段：为每个任务搜索全局最优工作流，拆分为多个单入单出（SESE）区域，每个区域对应固定角色（规划/检索/推理/验证等），输入输出接口统一
- 推理阶段：仅对质量不达标的区域做局部候选搜索，候选集限制为同角色算子，用label-free信号（自一致性、证据覆盖率、验证器得分）评估局部质量，通过耦合guard校验替换后边界一致性，避免下游错误传播
- 配置缓存：按输入类型签名缓存效果达标的区域配置，相似请求直接复用，摊薄搜索成本

### 关键实验
在数学推理、代码生成、多跳QA、知识密集型QA共10个基准数据集测试，和此前SOTA MaAS相比，用gpt-4o-mini执行时平均得分87.44，高出3.85点；和BayesFlow相比，用Claude Sonnet执行时平均得分84.1，高出3.3点；内存命中后搜索成本降低约50%，无需重新训练即可无缝替换更强的执行模型获得性能增益。

优化后的工作流不是静态的离线产物，而是可以随着推理时反馈和更强执行器持续进化的自适应执行策略。

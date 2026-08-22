---
title: 'FormalTCS: Benchmarking End-to-End Frontier Formal Theoretical Computer Science
  Research of Large Language Models'
title_zh: FormalTCS：大语言模型端到端前沿理论计算机科学研究基准
authors:
- Dingzirui Wang
- Xuanliang Zhang
- Keyan Xu
- Qingfu Zhu
- Wanxiang Che
affiliations:
- Harbin Institute of Technology
arxiv_id: '2608.20153'
url: https://arxiv.org/abs/2608.20153
pdf_url: https://arxiv.org/pdf/2608.20153
published: '2026-08-20'
collected: '2026-08-22'
category: Eval
direction: LLM科研能力评测 · 理论计算机科学
tags:
- LLM
- Benchmark
- Autoformalization
- Theorem Proving
- Evaluation
one_liner: 构建专家验证的TCS端到端科研基准，揭示LLM自动科研的两大核心瓶颈
practical_value: '- 垂域端到端评测基准构建可复用「保留场景专属定义/依赖+专家交叉验证」的标注范式，适配电商合规校验、搜索query意图转换等任务的评测集搭建

  - 自然语言转结构化逻辑（如用户query转ES查询表达式、营销话术转合规规则）类任务可参考其autoformalization瓶颈结论，前置轻量人工校验环节降低错误率

  - 垂域自动化Agent pipeline可借鉴其「生成→形式化校验→过滤→落地验证」的链路设计，适配广告投放策略自动迭代、推荐规则自动挖掘场景'
score: 4
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有LLM理论计算机科学（TCS）能力基准脱离真实科研场景，无法衡量模型端到端完成前沿TCS研究的真实水平。
### 方法关键点
1. 构建专家验证的FormalTCS基准，收录2025-2026年STOC、FOCS等TCS顶会的175个研究实例，完整保留论文原定义、假设与证明依赖，配套专家核验的Lean形式化代码与证明
2. 提出包含「新论断生成→形式化转换→过滤→证明验证」的全链路自动化TCS科研框架
### 关键结果数字
- 顶尖LLM自动形式化（自然语言转形式化定理）得分仅11.5，远低于人工提供形式化语句时28.6的证明Pass@8，自动形式化是核心瓶颈
- 自研框架生成的64个新论断仅6个通过专家+证明核验，LLM科研判断力不足是另一核心障碍

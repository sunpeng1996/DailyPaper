---
title: 'SWE-Gate: Passing Functional Tests Is Not Enough for Software Engineering
  Agents'
title_zh: SWE-Gate：软件工程Agent评估不能仅满足于功能测试通过
authors:
- Xin He
- Yanlin Wang
- Mingwei Liu
- Jiachi Chen
- Hongyu Zhang
- Guanbin Li
affiliations:
- Sun Yat-sen University School of Software Engineering
- Zhejiang University College of Computer Science and Technology
- Chongqing University School of Big Data and Software Engineering
- Sun Yat-sen University School of Computer Science and Engineering
arxiv_id: '2609.04167'
url: https://arxiv.org/abs/2609.04167
pdf_url: https://arxiv.org/pdf/2609.04167
published: '2026-09-03'
collected: '2026-09-07'
category: Agent
direction: 软件工程Agent评估基准构建
tags:
- Agent Evaluation
- Coding Agent
- Benchmark
- LLM
- Constraint Compliance
one_liner: 推出同时评估功能正确性与评审约束遵从度的仓库级软件工程Agent基准SWE-Gate
practical_value: '- 构建业务Agent评估体系时可复用该思路，除功能正确性校验外新增业务规则/合规约束类校验项，避免上线后踩体验/合规坑

  - 构造领域Agent测试基准时，可参考从真实反馈（如用户投诉、运营审核意见）提取约束的方法，生成更贴合线上场景的用例

  - 可复用测试分层设计思路，拆分功能测试与规则约束测试，分别量化Agent问题解决能力与规则遵从能力，便于根因定位'
score: 6
source: arxiv-cs.AI
depth: abstract
---

- **动机**：现有仓库级编码Agent基准仅评估功能测试通过率，忽略真实开发中代码评审带来的接受约束，导致评估结果高估Agent实际落地能力
- **方法关键点**：推出SWE-Gate仓库级基准，从真实PR评审评论提取约束合成修复实例；每个实例拆分功能测试、约束测试，配套不合规补丁与金标准补丁，可独立评估问题解决能力与约束遵从度
- **关键结果**：基准覆盖75个跨领域Python开源仓库，共303个修复实例；测试4款不同能力LLM驱动的编码Agent发现，644个通过功能测试的修复中221个不符合评审约束，仅测功能会大幅高估Agent能力

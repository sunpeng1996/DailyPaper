---
title: 'Vero: Can AI Agents Build Formally Verified Software Repositories?'
title_zh: Vero：AI Agent能否构建经过形式化验证的软件仓库
authors:
- Zhe Ye
- Hantao Lou
- Yuechun Sun
- Peiyang Song
- Zhengxu Yan
- Timothe Kasriel
- Qingyang Zhang
- Kaiyu Yang
- Soonho Kong
- Jingxuan He
affiliations:
- UC Berkeley
- University of Chicago
- California Institute of Technology
- Stanford University
- Amazon Web Services
arxiv_id: '2608.13522'
url: https://arxiv.org/abs/2608.13522
pdf_url: https://arxiv.org/pdf/2608.13522
published: '2026-08-13'
collected: '2026-08-15'
category: Agent
direction: Agent评测 · 代码生成形式化验证
tags:
- AI Agent
- Code Generation
- Formal Verification
- Benchmark
- Repository-level Evaluation
one_liner: 首个面向仓库级代码与形式化证明联合生成任务的AI Agent评测基准
practical_value: '- 做代码生成类Agent（如推荐/广告系统后台逻辑自动生成、策略代码迭代）的团队，可借鉴Vero的验证思路，在单元测试外补充轻量形式化校验环节，降低线上bug风险

  - 复杂多模块任务的Agent评测可复用Vero的双模式（仅评测子任务/全链路评测）设计+审计校验机制，提升评测结果鲁棒性

  - 高可靠需求的Agent应用（如电商交易链路代码自动生成），可参考Vero的任务拆解逻辑，把形式化校验嵌入Agent生成的每一步输出'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有AI代码生成Agent无严格正确性保障，已有的验证代码生成基准仅针对单函数场景、或仅评测给定实现的证明生成能力，无法评估多模块仓库级的代码+证明联合生成效果。

### 方法关键点
- 发布Vero基准，包含43个源自真实仓库的多模块实例，覆盖Python、Dafny、Coq等多语言，跨密码协议、分布式系统等领域
- 支持仅证明、代码+证明两种评测模式，内置审计机制允许Agent验证规范不可满足或参考代码错误，自动修正基准隐存缺陷

### 关键结果
当前最强配备Lean工具链的代码Agent仅能完全解决27/43个实例，难度最高的仓库实例通过率为0，现有Agent在仓库级验证代码生成上能力缺口明显。

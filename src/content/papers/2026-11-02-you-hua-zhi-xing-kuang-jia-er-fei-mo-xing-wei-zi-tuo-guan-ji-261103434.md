---
title: 'Optimize the Harness, Not the Model: Fitting a Minimal Agent to a Self-Hostable
  LLM for Investigative Analysis'
title_zh: 优化执行框架而非模型：为自托管LLM适配极简调查分析Agent
authors:
- Shai Nahum Gefen
- Vered Chassida
- Dmitry Basin
- Guy Feigenblat
affiliations:
- Dream Security, Tel Aviv, Israel
arxiv_id: '2611.03434'
url: https://arxiv.org/abs/2611.03434
pdf_url: https://arxiv.org/pdf/2611.03434
published: '2026-11-02'
collected: '2026-11-03'
category: Agent
direction: Agent 执行框架优化 自托管部署
tags:
- LLM-Agent
- Harness-Optimization
- On-Premise-Deployment
- Minimal-Agent
- Autoresearch
one_liner: 提出自底向上的Agent执行框架优化方案CLEO，用极小代码量达到商用大框架相当的调查分析准确率
practical_value: '- 业务落地Agent时可复用自底向上的构建思路：从仅包含核心工具的最小可行框架开始迭代，仅保留能带来明确效果增益的组件，大幅降低代码审计、维护成本

  - 对于数据合规要求高的场景（如电商用户隐私数据处理、金融推荐），可采用「固定自托管LLM权重+仅优化外围执行框架」的方案，既满足数据不出域要求，又能保证效果达标

  - Agent迭代时设置双重准入规则：效果增益超过预设阈值+组件通用可审计无冗余，可有效避免框架过拟合单一场景、防止代码膨胀

  - 采用小批量高频评估方案：每次迭代仅用几十条标注数据，分钟级完成效果校验，适合快速落地Agent类业务'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
高安全合规场景下（如政府情报、金融、电商敏感数据处理），LLM Agent无法使用公有云大模型，只能部署自托管开源LLM；同时Agent的执行框架（Harness，包含工具集、内存策略、控制流、安全护栏）不能有多余能力，否则安全审计成本极高。现有通用Agent框架代码量达数十万行，审计难度大，人工设计的极简框架又难以保证效果。

### 方法关键点
- 固定自托管LLM的权重，不做任何微调，所有优化都围绕外围Harness展开，最大限度降低合规风险
- 采用自底向上的构建逻辑：初始Harness仅包含ls、read、grep、沙箱Python 4个核心工具，通过propose-test-justify自动迭代新增组件，只有同时满足「准确率提升超过阈值」和「通用、可审计、无冗余」两个条件的变更才会被保留
- 迭代过程中定期切换OOD评估数据集，避免框架过拟合单一场景，用LLM Judge做自动效果评估，降低人工标注成本

### 关键实验
基于3个情报调查场景共300+专家标注Q&A（240条为完全未暴露的held-out测试集），对比3个基线：Claude Code SDK（约512k行代码）、原生PI框架（75k行）、带CLEO优化Prompt的PI框架（75k行）。结果显示：CLEO仅用3k行代码，pass rate达83.8%，仅比最强基线Claude Code SDK低1.2个百分点，latency 114s优于所有基线，代码量比通用商用框架小2个数量级。

### 核心结论
对于有严格安全合规要求的Agent落地场景，优化外围执行框架的投入产出比远高于微调甚至替换大模型，极小的能力攻击面就能达到和大而全的通用框架相当的效果。

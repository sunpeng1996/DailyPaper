---
title: Retrofitting Code Using LLMs to Support Exceptional Behavior
title_zh: 基于大语言模型的代码异常相关逻辑自动补全方法
authors:
- Linghan Zhong
- Jiyang Zhang
- Jayanth Srinivasa
- Junyi Jessy Li
- Milos Gligoric
affiliations:
- The University of Texas at Austin, USA
- Cisco Systems, USA
arxiv_id: '2609.10397'
url: https://arxiv.org/abs/2609.10397
pdf_url: https://arxiv.org/pdf/2609.10397
published: '2026-09-09'
collected: '2026-09-11'
category: LLM
direction: LLM代码生成 · 异常逻辑自动补全
tags:
- LLM
- Code Generation
- Static Analysis
- Dynamic Analysis
- Test Driven Development
one_liner: 提出结合动静态程序分析与LLM的EXCODER框架，自动补全代码中缺失的异常相关逻辑
practical_value: '- 开发代码类Agent时，可复用「动静态信息提取+上下文工程」的范式提升领域代码生成准确率

  - 测试驱动的生成逻辑可迁移到需符合业务规则的生成任务，如推荐策略代码自动生成

  - pass@k评估方法可直接复用到所有生成类业务的效果量化评测'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
手动开发维护大规模代码库的异常相关代码（ERC，含throw语句、前置判断、try/catch块）成本高，现有LLM代码生成方案未覆盖基于测试用例补全ERC的全新任务。
### 方法关键点
EXCODER框架融合静态+动态程序分析提取代码上下文信息做针对性prompt工程，引导LLM生成符合异常行为测试（EBT）要求的缺失ERC，天然适配测试驱动开发流程。
### 关键结果
基于GitHub 75个Java项目的304个方法构造基准测试集，搭配Qwen 2.5 Coder 32b时，pass@1/5/10分别达85.92%/86.18%/86.51%，较基线分别提升12.56/12.82/13.15个百分点。

---
title: 'DFM Mimir v1: An Open HRM Delivering Frontier Performance at 1B Parameters
  Using Only Permissible Post-Training Data'
title_zh: DFM Mimir v1：仅用合规后训练数据的1B参数高性能开源HRM大模型
authors:
- Peter Schneider-Kamp
- Jacob Nielsen
- Gianluca Barmina
- Kenneth Enevoldsen
- Lukas Galke Poech
affiliations:
- University of Southern Denmark
- Ordbogen A/S
- Aarhus University
arxiv_id: '2608.13517'
url: https://arxiv.org/abs/2608.13517
pdf_url: https://arxiv.org/pdf/2608.13517
published: '2026-08-13'
collected: '2026-08-14'
category: LLM
direction: 大模型训练 · 合规数据训练
tags:
- LLM Training
- Permissible Data
- Open Source LLM
- HRM Architecture
- Small Parameter LLM
one_liner: 仅用合规公开数据训练的1B参数HRM架构大模型，性能匹敌4B量级主流开源模型
practical_value: '- 小参数LLM落地可参考该项目的合规训练数据筛选方案，规避版权风险的同时保障下游推荐/Agent任务性能

  - 1B参数模型性能匹敌4B量级方案，对端侧推荐、低算力场景的LLM部署选型有参考价值，可大幅降低推理成本

  - 跨境电商小语种场景的大模型定制可复用其多数据集混合训练配比策略，快速打造适配特定小语种的基座模型'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
当前大模型训练高度依赖非公开、版权存疑的大规模数据集，开源社区、合规导向项目训练高质量基座门槛极高，小语种优质合规训练数据稀缺，难以产出高性能基座模型。
### 方法关键点
采用HRM架构训练1B参数基座模型Mimir v1，全流程仅使用公开许可的后训练数据，混合161个合规数据集完成从零训练，覆盖英文、丹麦语、数学、代码多领域。
### 关键结果数字
在20个基准测试中，性能超过原生HRM-Text 1B，英文/数学/代码能力匹敌Qwen 3.5 4B、Gemma 4 E2B等4B量级开源模型，丹麦语任务刷新SOTA，模型已开源至Hugging Face。

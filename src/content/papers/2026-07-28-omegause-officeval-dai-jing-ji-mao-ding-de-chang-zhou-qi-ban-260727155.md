---
title: 'OmegaUse-OfficeVal: Benchmarking LLM Agents on Long-Horizon Office-Suite Tasks
  with Economic Grounding'
title_zh: OmegaUse-OfficeVal：带经济锚定的长周期办公任务LLM Agent评测基准
authors:
- Jingbo Zhou
- Yusai Zhao
- Qi Bao
- Jingjia Cao
- Zhenghai Chen
- Chang Gao
- Kaiqi Guo
- Muxin Guo
- Mingxuan Li
- Xinjiang Lu
affiliations:
- Baidu Inc. Agent Frontier Team, Large Model Frontier Research Department
arxiv_id: '2607.27155'
url: https://arxiv.org/abs/2607.27155
pdf_url: https://arxiv.org/pdf/2607.27155
published: '2026-07-28'
collected: '2026-07-30'
category: Agent
direction: LLM Agent 办公场景任务评测基准
tags:
- LLM Agent
- Benchmark
- Economic Grounding
- Long-Horizon Task
- Evaluation
one_liner: 推出绑定人力成本、任务定价的长周期办公LLM Agent评测基准，含100个真实任务与代码化校验工具
practical_value: '- 搭建业务Agent评测体系时，可参考其绑定人力成本、任务价值的加权评估逻辑，替代纯准确率指标，更贴近ROI核算需求

  - 复杂长周期任务的校验可复用其细粒度规则+代码化校验器的设计，降低人工标注成本，提升评测稳定性

  - 电商运营类办公Agent（如报表生成、文案批量处理）选型时，可直接用该基准做成本-效率-质量的tradeoff评估'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有LLM Agent评测基准缺乏对长周期办公类任务的成本合理性评估，无法支撑人力投入与Agent落地的ROI对比需求。
### 方法关键点
1. 构建含100个来自真实从业者需求的办公套件（DOCX/PPTX/XLSX/PDF）任务数据集，单任务平均需人类2.32小时完成；
2. 每个任务绑定人力时长、任务定价两个经济信号，支持价值加权评估；
3. 基于单任务平均20.09个细粒度评分规则开发代码化校验器，保障评测稳定性。
### 关键结果数字
当前前沿LLM Agent的成本、耗时均远低于人类，但交付质量仍远未达到人类水平。

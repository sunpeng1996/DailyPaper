---
title: 'From Prompts to Trees: Effective LLM-Guided Tree Generation for Few-Shot Tabular
  Classification'
title_zh: 从提示到树：面向少样本表格分类的LLM引导高效树生成方法
authors:
- Yue Qiu
- Zekang Du
- Yiqun Diao
- Bingsheng He
- Qinbin Li
affiliations:
- Huazhong University of Science and Technology
- National University of Singapore
arxiv_id: '2610.10227'
url: https://arxiv.org/abs/2610.10227
pdf_url: https://arxiv.org/pdf/2610.10227
published: '2026-10-07'
collected: '2026-10-08'
category: Training
direction: LLM知识蒸馏 · 可解释少样本分类
tags:
- Knowledge Distillation
- Decision Tree
- Few-Shot Learning
- Tabular Data
- Interpretability
one_liner: 将LLM知识蒸馏为可解释决策树，通过三阶段规则生成组装流程降低提示开销、提升少样本表格分类效果
practical_value: '- 电商用户分层、风控、客群标签预测等少样本表格分类场景，可复用「LLM知识蒸馏到决策树」的思路，兼顾小样本性能、推理速度与可解释性，避免LLM直接部署的高成本

  - 规则类生成任务不要让LLM直接输出完整结构（如完整分类树、全量召回规则），可拆分为分步生成单条规则再组装的范式，大幅降低prompt开销、提升输出稳定性

  - 推荐系统可解释规则挖掘场景，可借鉴三阶段规则生成+组装框架，用LLM补充小样本下的规则覆盖度，解决传统规则挖掘的冷启动短板'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
LLM直接处理表格分类任务存在推理成本高、可解释性差的缺陷，难以落地到低资源、强监管场景；而传统决策树虽推理快、全透明，但少样本场景下性能表现不佳，现有直接让LLM生成完整决策树的方案输出不稳定、提示开销极高。
### 方法关键点
提出三阶段蒸馏框架，不要求LLM直接输出完整树结构：1. 引导LLM基于少样本标注数据生成单条分类规则；2. 对生成规则做有效性校验、去重过滤；3. 将优质规则自动组织为结构合理的决策树，实现LLM世界知识向可解释轻量模型的迁移。
### 关键结果
在多个真实表格数据集上，相比现有基线方案准确率更优，提示开销降低60%以上，同时保留决策树的全可解释性与毫秒级推理速度，适合工业级低资源落地。

---
title: 'MMDM: Measuring Massive Multitask Decision Making'
title_zh: MMDM：大规模多任务决策能力评测基准
authors:
- Junhao Shen
- Qing Zong
- Yue Guo
- Zhanqiu Zhang
- Yiwen Guo
- Hong Cheng
affiliations:
- The Chinese University of Hong Kong
- Hong Kong University of Science and Technology
- LIGHTSPEED
- Independent Researcher
arxiv_id: '2611.14309'
url: https://arxiv.org/abs/2611.14309
pdf_url: https://arxiv.org/pdf/2611.14309
published: '2026-11-09'
collected: '2026-11-11'
category: Eval
direction: 决策模型评测 · 多任务基准
tags:
- Decision-Making
- Benchmark
- System-1 Model
- Multi-task Evaluation
- Agent Capability
one_liner: 构建覆盖16类任务共5448个样本的多任务决策基准，可评测System-1模型的多元决策能力
practical_value: '- 可复用MMDM的评测框架，针对电商推荐的工具选择、多意图识别、约束下选品等决策场景定制垂直评测集，避免通用基准的测试集污染问题

  - 参考其单选择/多选择/软标签三类任务定义和SB-F、Soft Brier等指标，替代单一准确率评估推荐/Agent决策可靠性，尤其适配多候选选全、概率校准场景

  - 当前决策模型在约束规划、多选项逻辑、长上下文决策上准确率不足60%，业务落地时这类场景（如满减规则下的商品组合推荐、多工具并行调用）需加规则校验兜底

  - 可复用其样本重写、重组方法，基于业务真实历史决策样本生成低重复、抗记忆的评测集，更准确衡量模型真实泛化能力'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前System-1决策模型（单前向步输出结构化概率决策，无需生成推理链）已广泛用于Agent工具选择、意图分类、质量打分等场景，但现有评测基准普遍存在测试集污染问题，且未覆盖长上下文、大选项空间、选项间复杂依赖等真实决策痛点，无法准确衡量模型实际落地能力。

### 方法关键点
- 构建5448个高质量决策样本，覆盖16类任务，选项数范围2~1024，输入最长达64817token，所有样本均经过重写、重组或全新构建，大幅降低测试集泄露风险
- 定义三类决策任务：Hard Single-select（单选唯一正确选项）、Hard Multi-select（多选全部有效选项）、Soft-label（输出符合参考分布的概率），匹配不同业务决策需求
- 设计针对性评测指标：单选/多选准确率、SB-F（衡量多选择的分离度与平衡性）、Soft Brier（软标签分布误差）、Score nMAE（打分任务归一化误差）

### 关键结果
评测了28款主流决策模型，最高单选准确率为76.00%，最高多选准确率仅36.81%，绝大多数模型在选项逻辑、约束规划类任务上准确率不足60%；单选择准确率高的模型可能软标签校准误差高，长上下文表现好的模型未必能处理大选项空间。

### 核心结论
单一准确率无法完整衡量决策模型的实际落地效果，多维度覆盖任务类型、上下文长度、选项规模的针对性评测是决策类模型上线前的必要步骤

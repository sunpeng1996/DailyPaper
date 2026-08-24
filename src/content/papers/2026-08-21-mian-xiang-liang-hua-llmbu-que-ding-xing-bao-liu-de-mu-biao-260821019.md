---
title: Target-Aware Calibration Data Selection for Preserving Uncertainty in Quantized
  Language Models
title_zh: 面向量化LLM不确定性保留的目标感知校准数据选择方法
authors:
- Zhen Yang
- Sizai Hou
- Kaiwen Zheng
- Yaofang Liu
- Liang He
- Yixuan Chen
- Kangning Cui
affiliations:
- Yale University
- The Hong Kong University of Science and Technology
- University of Oxford
- City University of Hong Kong
- Shanghai Institute of Optics and Fine Mechanics
arxiv_id: '2608.21019'
url: https://arxiv.org/abs/2608.21019
pdf_url: https://arxiv.org/pdf/2608.21019
published: '2026-08-21'
collected: '2026-08-24'
category: LLM
direction: 大语言模型量化 · 不确定性保留
tags:
- Quantization
- Calibration
- Uncertainty
- LLM Deployment
- Post-training Quantization
one_liner: 提出目标感知的DPQ校准数据选择框架，无需修改量化器即可保留LLM量化后的不确定性行为
practical_value: '- 部署LLM驱动的Agent（如智能导购、query理解）时，如果依赖模型置信度做拒答、路由决策，可复用DPQ校准逻辑：用全精度模型的低margin（高doubt）样本混通用锚点数据做量化校准，避免量化后置信度漂移导致下游决策错误

  - 电商多选项召回/排序场景如果用量化LLM做reranking，可根据业务目标选校准配方：涉及拒答/低置信度过滤的场景用DPQ-r75（75%高doubt样本），纯MCQA类打分场景用DPQ-r50或单信号（置信度/熵）校准配方，比通用WikiText校准大幅降低不确定性漂移

  - 量化LLM的评估不能只看准确率，要补充全精度模型行为对齐指标（置信度偏移、margin漂移、JSD），避免量化后top1结果一致但下游依赖的打分逻辑完全失效'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM量化方案仅优化准确率、困惑度等指标，忽略置信度、决策边界、拒答行为等不确定性特征的保留，量化后即使top1结果不变，置信度分布也可能发生大幅漂移，破坏依赖模型打分的下游链路（如选择性预测、拒答、多模型集成、排序），现有后处理校准方法要么无法修复决策翻转，要么会偏离全精度模型的原始行为。

### 方法关键点
- 定义两类不确定性保留风险：分布风险$R_{dist}$（量化后输出分布与全精度的JSD）、边界风险$R_{bdry}$（量化前后决策翻转的加权损失），适配不同业务目标
- DPQ（Doubt-Preserving Quantization）是轻量预量化校准数据选择框架，完全不修改量化器逻辑：首先用全精度模型给候选样本打分，基于$1-(top1概率-top2概率)$计算doubt得分，选择高doubt的边界样本，按比例$r$混合通用锚点数据（WikiText、随机QA）作为校准集
- 提供适配不同场景的配方家族：$r=0.75$（DPQ-r75）适配边界敏感场景，$r=0.5$（DPQ-r50）或单信号（置信度/熵）适配通用MCQA场景

### 关键实验
覆盖8款LLM（Qwen2.5、Llama3.1/3.2、Mistral）、9个NLP基准、22种对比方法；在SQUAD2拒答边界保留任务上，DPQ-r75相比GPTQ-WikiText校准，边界准确率偏差从0.4553降至0.2125，拒答率偏差从0.2271降至0.1000，JSD从0.0387降至0.0158；在通用MCQA任务上，DPQ-r50或单信号配方表现最优，不存在跨场景通用的最优校准配方。

最值得记住的结论：量化校准数据应该针对部署需要保留的全精度模型行为选择，而不是作为与业务目标无关的固定量化配置。

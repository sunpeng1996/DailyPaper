---
title: 'EarlyEval: Cheaper Agent Evaluation via Early Outcome Prediction'
title_zh: EarlyEval：基于早期结果预测的低成本Agent评估框架
authors:
- Yuling Shi
- Zhensu Sun
- Junsen Dong
- Chengcheng Wan
- David Lo
- Xiaodong Gu
affiliations:
- Shanghai Jiao Tong University
- Singapore Management University
- East China Normal University
- Shanghai Innovation Institute
arxiv_id: '2609.02783'
url: https://arxiv.org/abs/2609.02783
pdf_url: https://arxiv.org/pdf/2609.02783
published: '2026-09-01'
collected: '2026-09-03'
category: Eval
direction: Agent 评估效率优化
tags:
- Agent Evaluation
- Early Stopping
- LightGBM
- Cost Optimization
- LLM Agent
one_liner: 用轻量双LightGBM分类器提前终止Agent评估，最高省44%输入token，准确率89%-97%
practical_value: '- 自研业务Agent（如电商导购Agent、推荐调优Agent）快速迭代时可复用该框架：收集历史评估轨迹训练双分类器，达到置信阈值提前终止，可降30%左右推理token成本，迭代效率提20%以上

  - 特征设计可直接迁移：优先选无依赖的行为特征（操作计数、错误模式、重复行为、测试通过率趋势）+ 轻量文本特征（TF-IDF+SVD压缩），无需LLM judge，单步开销<1ms，不占用核心资源

  - 阈值可按场景灵活配置：快速验证、做相对A/B测时用0.8-0.85低阈值，最多省60%+步骤；发布最终指标时用0.9+高阈值，通过率偏差控制在2pp以内，排名相关性≥0.95，满足业务实验要求

  - 可和现有降本方法叠加：先做基准蒸馏缩小测试任务集，再叠加EarlyEval单任务提前终止，双重降本效果更显著，适合资源有限的中小团队做Agent迭代'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
LLM Agent迭代过程中评估成本激增，前沿模型单轮跑SWE-bench类基准需数百到数千美元，迭代几十次成本可达数万量级。现有降本方案集中在基准蒸馏，仅减少评估任务数，单任务执行成本完全未被优化，存在明显效率空白。
### 方法关键点
- 核心逻辑：Agent最终结果可从中间行为提前预判，正确完成核心修改后后续步骤多为冗余，反复重试同一错误即可判定最终失败
- 离线训练：基于历史带结果标注的Agent轨迹，训练两个独立的LightGBM分类器（成功预测、失败预测），特征包含三类：行为特征（操作计数、错误模式、重复行为、测试通过率趋势等）、轻量文本特征（TF-IDF+SVD压缩的任务prompt、操作历史、环境反馈）、参考解特征（可选，有gold答案时计算当前操作与参考的重叠度）
- 在线推理：Agent每步运行后抽取特征输入分类器，任意分类器置信度超过校准阈值就提前终止，输出预测结果，单步推理开销可忽略
### 关键结果
在SWE-bench Verified、TerminalBench、Toolathlon三个Agent基准上采用留一Agent出的严格评估协议：最多削减26%执行步骤、44.1%输入token、29.4%输出token，预测准确率89%-97%，Agent通过率平均偏差仅1-2个百分点，与全量评估的排名Spearman相关系数达0.959-0.991，几乎完全保留评估保真度。
### 核心记忆点
Agent评估降本无需仅依赖缩小测试集，单任务内基于行为信号提前终止的收益可观，且对评估结果的影响极小

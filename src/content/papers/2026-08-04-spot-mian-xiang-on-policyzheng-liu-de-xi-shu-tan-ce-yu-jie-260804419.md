---
title: 'SPOT: Sparse Probing and Outcome Calibration for On-Policy Distillation'
title_zh: SPOT：面向On-Policy蒸馏的稀疏探测与结果校准方法
authors:
- Zikun Qu
- Min Zhang
- Mingze Kong
- Zhiwei Shang
- Yikun Ban
- Shuang Qiu
- Zhongxiang Dai
affiliations:
- 香港中文大学（深圳）
- 华东师范大学
- 北京航空航天大学
- 香港城市大学
arxiv_id: '2608.04419'
url: https://arxiv.org/abs/2608.04419
pdf_url: https://arxiv.org/pdf/2608.04419
published: '2026-08-04'
collected: '2026-08-11'
category: Training
direction: LLM知识蒸馏 · On-Policy蒸馏优化
tags:
- Knowledge Distillation
- On-Policy Distillation
- LLM Training
- Reasoning
- Model Compression
one_liner: 提出稀疏探测+结果校准的On-Policy蒸馏框架，兼顾小模型推理准确率与多样本覆盖度
practical_value: '- 做电商智能导购、客服等推理类Agent的小模型蒸馏时，可复用稀疏探测打分逻辑：用教师熵、top-k概率质量、师生偏差三个维度筛选重点蒸馏的token位置，节省探测预算，避免无效计算

  - 多路径生成场景（如电商营销文案、推荐理由生成）需要提升多输出覆盖度时，可借鉴结果校准思路：在教师分布基础上用业务验证器（点击率/转化率预估器）的结果加权倾斜，既保留教师通用能力，又适配业务目标

  - 小模型蒸馏工程落地时，可参考SPOT的预算控制机制：固定每轮蒸馏的探测位置数M、每个位置的候选数k_p，将额外计算开销控制在生产环境可接受范围'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
传统On-Policy Distillation（OPD）依赖反向KL训练存在模式坍缩问题，仅用教师熵无法区分不确定性是集中在少量可行候选还是分散在长尾噪声，也无法判断学生是否已经掌握对应候选，同时教师的局部token概率无法保证下游生成效果，限制了小模型的多解覆盖能力。
### 方法关键点
- 采集阶段：设计三元组位置打分公式，融合归一化教师熵、top-k候选的概率质量占比、师生分布偏差，优先选择不确定性集中、学生掌握度差的位置分配有限探测预算
- 探索阶段：对选中位置的教师top-k候选，分别基于学生策略生成完整路径，用验证器评估每条路径的最终效果
- 利用阶段：基于验证结果构造KL正则化的校准目标，对下游效果好的候选加权，同时锚定教师分布，仅对存在正收益候选的位置增加额外分支损失
### 关键实验
以Qwen3-8B为教师，蒸馏0.6B/1.7B/4B三个尺度的学生模型，在6个数学推理基准上测试，对比KD、OPD、GRPO、EOPD四个基线：相对OPD，SPOT的宏Avg@8提升0.47~1.48个百分点，宏Pass@8提升4.55~5.28个百分点；相对最优基线EOPD，宏Avg@8提升0.29~0.68个百分点，宏Pass@8提升2.49~3.19个百分点，在高采样场景（k=64）下相对OPD仍有12.5~16.67个百分点的Pass@k优势。

最值得记住的一句话：On-Policy蒸馏应拆分「在哪探测」和「蒸馏什么」两个决策，用不确定性与师生偏差选探测位置，用下游结果校准蒸馏目标，可同时兼顾效果、覆盖度与效率。

---
title: 'Train Where the Quantized Model Goes: On-Policy Distillation for Low-Bit Reasoning'
title_zh: 在量化模型生成轨迹上训练：面向低比特推理的在策略蒸馏方法
authors:
- Yuanteng Chen
- Zhilei Liu
- Peisong Wang
- Yuantian Shao
- Chuangyi Li
- Weining Wang
- Shuang Qiu
- Gang Li
- Jing Liu
- Jian Cheng
affiliations:
- 中国科学院自动化研究所
- 中国科学院大学人工智能学院
- 中关村学院
- 香港城市大学
- 南京理工大学
arxiv_id: '2609.26708'
url: https://arxiv.org/abs/2609.26708
pdf_url: https://arxiv.org/pdf/2609.26708
published: '2026-09-22'
collected: '2026-09-23'
category: Training
direction: LLM低比特量化 · 推理性能恢复
tags:
- Quantization
- Knowledge Distillation
- Low-bit LLM
- On-policy Training
- Reasoning
one_liner: 提出QAD结合在策略蒸馏的两阶段框架，将亚3比特量化LLM长推理性能保留率从35%提升至70%
practical_value: '- 业务侧低比特LLM部署（如电商智能客服、个性化文案生成、端侧推荐Agent）可直接复用QAD+OPD两阶段方案：先用QAD做基础量化，追加几百步OPD即可恢复长生成能力，GPU成本仅为QAD的1/14~1/23，性价比极高

  - 遇到量化后LLM长生成重复、跑满解码步、无法完成长推理链路的问题时，可复用OPD的核心思路：在量化模型自身的生成轨迹上做全精度教师的token级监督，搭配轻量任务奖励，无需重构量化流程即可快速优化

  - 低比特蒸馏trick：OPD阶段优先用学生模型自身的全精度版本做教师，效果优于调用更大的外部模型，可进一步降低训练阶段的推理成本

  - 亚2比特极端量化场景下OPD收益尤为突出，1.88比特位宽下可将代码、数学推理性能提升2~4倍，适合算力受限的边缘侧、端侧LLM部署场景'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
亚3比特极端量化可大幅降低LLM内存和带宽开销，是低成本、端侧部署的核心路径，但现有量化感知蒸馏（QAD）仅能恢复80%+的短问答性能，数学、代码等长推理任务性能保留率仅35%，还易出现重复生成、耗尽解码预算的问题。根源在于QAD仅在固定语料前缀上训练，推理时量化误差沿自回归轨迹逐步累积，放大了暴露偏差，导致模型遇到自身生成的异常前缀时无监督信号校正。

### 方法关键点
- 两阶段恢复框架：先通过QAD初始化获得稳定的低比特模型，恢复通用能力；再追加轻量在策略蒸馏（OPD）阶段补全长推理能力
- OPD训练流程：量化学生通过部署用的低比特前向路径生成前缀，冻结的全精度教师在学生生成的前缀上做token级反向KL蒸馏，直接校正量化轨迹上的预测偏差
- 损失设计：结合token级蒸馏损失与任务验证器奖励（数学判答案正确性、代码判单测通过率），同时优化局部生成质量和最终任务效果

### 关键结果
在Qwen3 0.6B/1.7B/4B、Falcon3-1B四个模型，2.79、1.88两个有效比特位宽下测试：
- 平均MATH-500性能保留率从QAD的35%提升至70%，HumanEval从66%提升至91%，短问答性能无损失
- 1.88比特位宽下收益更显著，Qwen3-4B的GSM8K准确率从QAD的17.36%直接提升至64.59%
- OPD仅需数百步训练，GPU成本仅为QAD的1/14~1/23，相同训练预算下效果远超持续QAD训练

> 最值得记住的结论：低比特量化LLM的长推理能力缺失核心是训练-推理的轨迹分布不匹配，在模型自身生成的轨迹上做少量监督就能以极低代价补全能力

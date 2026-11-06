---
title: 'Terminal-style Mathematical Modeling Bench: The First Agentic and Verifiable
  Benchmark for Mathematical Modeling'
title_zh: TB-MathModel：首个可验证的终端式数学建模Agent评测基准
authors:
- Xiaojun Wu
- Cehao Yang
- Xuhui Jiang
- Chengjin Xu
- Jia Li
- Jian Guo
affiliations:
- IDEA Research
- The Hong Kong University of Science and Technology (Guangzhou)
- DataArcTech Ltd.
arxiv_id: '2611.08237'
url: https://arxiv.org/abs/2611.08237
pdf_url: https://arxiv.org/pdf/2611.08237
published: '2026-11-05'
collected: '2026-11-06'
category: Agent
direction: Agent 长程推理能力评测基准
tags:
- Agent
- Benchmark
- Mathematical Reasoning
- Verification
- Multimodal
one_liner: 首个支持容器化终端执行、双层可行性校验的数学建模Agent评测基准
practical_value: '- 可复用方向感知的单侧打分机制：在推荐/广告效果评估中，避免惩罚超过基线的优化结果，解决传统距离类指标的不对称缺陷

  - 双层可行性校验架构可迁移至Agent生成内容校验：先用规则门做快速过滤，再用形式化证明做可信校验，适配电商活动规则校验、权益发放合理性检查等场景

  - 多参考投票的评估范式可用于生成式推荐的质量评估：无需绑定单一ground truth，基于多个优质人工案例投票打分，适配多解的生成类任务'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有数学建模Agent评测要么只校验局部片段、要么靠LLM打分评估报告，无法验证输出数值的正确性与物理可行性，缺少支持完整建模流程、机器可校验的端到端评测基准。

### 方法关键点
- 覆盖2023-2025年18道CUMCM、MCM真实赛题，提供容器化终端运行环境，支持多模态输入（文本、附件、21张负载相关图片），Agent仅需输出结构化JSON即可完成评测
- 采用方向感知的单侧打分机制，超过参考答案的优化结果不会被惩罚；基于99篇获奖优秀论文构建多参考投票面板，避免单参考的偏见
- 双层可行性校验：第一层是规则门，覆盖6类可判定不变量做快速过滤，不合格答案直接打0分；第二层是624条Lean 4形式化证明，确保校验规则本身的正确性

### 关键结果
对比7个多模态模型Agent，GPT-6 Astra + codex 取得最高多参考O-EVAL 64.58%；DeepSeek V4.1 Flash以1/100的成本（单轮$2.54）取得59.81%的O-EVAL，仅比榜首低4.77个百分点；不同Agent Harness对得分影响不超过0.07pp，基准主要衡量模型本身能力。

最值得记住的一句话：面向多解的复杂任务评估，单侧打分+多参考投票+可行性硬校验的组合，能大幅提升评估的可信性与公平性。

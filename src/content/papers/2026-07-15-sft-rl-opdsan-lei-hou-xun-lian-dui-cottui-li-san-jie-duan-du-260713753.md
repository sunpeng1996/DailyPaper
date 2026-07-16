---
title: 'Post-Training Shifts Confidence: A Three-Stage Analysis of How SFT, RL, and
  OPD Shape Pre-, Intra-, and Post-CoT Calibration'
title_zh: SFT/RL/OPD三类后训练对CoT推理三阶段置信度校准的影响分析
authors:
- Shuhao Li
- Guodong Du
- Anhao Zhao
- Wanyu Lin
- Tianyu Yuan
- Xiaoyu Shen
affiliations:
- Eastern Institute of Technology
- The Hong Kong Polytechnic University
arxiv_id: '2607.13753'
url: https://arxiv.org/abs/2607.13753
pdf_url: https://arxiv.org/pdf/2607.13753
published: '2026-07-15'
collected: '2026-07-16'
category: Reasoning
direction: 大模型推理 · 置信度校准
tags:
- Confidence Calibration
- Chain-of-Thought
- SFT
- RL
- OPD
- Inference Optimization
one_liner: 对比SFT/RL/OPD后训练的CoT三阶段置信度特性，提出位置感知PosConf策略提升推理效率与精度
practical_value: '- 做Agent推理优化时，可直接匹配不同后训练模型的置信度优势场景：OPD模型用预生成置信度做问题难度路由，SFT模型用生成中置信度做无效路径早期剪枝，RL模型用生成后置信度做多候选答案聚合，无需额外训练即可提升推理性价比

  - 做LLM推理工程落地时，参考PosConf的位置感知思路，为不同后训练的模型设置专属可靠置信度区间：例如OPD仅取推理前60%位置的置信度，RL仅取后40%位置的置信度，可规避逆校准问题，进一步提升early
  stopping和答案聚合的效果

  - 电商场景的LLM应用（如智能导购推理、复杂query理解、营销文案生成）可复用该范式匹配逻辑，平衡推理成本和效果，无需额外开发奖励模型即可拿到可观的效率提升'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有面向推理的LLM后训练方法（SFT、RL、OPD）仅以最终答案准确率为评估指标，忽略了推理全流程的置信度校准特性。而置信度是推理阶段算力调度、无效路径剪枝、多候选答案聚合的核心信号，当前缺乏对不同后训练范式如何影响CoT三阶段置信度的系统性对照研究，导致置信度信号使用不当，推理性价比低。

### 方法关键点
- 提出三阶段校准框架：拆分Pre-CoT（生成前置信度做难度预测）、Intra-CoT（生成中置信度做早期终止）、Post-CoT（生成后置信度做答案聚合）三个场景，基于top-k token对数概率计算置信度，引入相对token位置适配不同长度推理链。
- 控制变量实验设计：基于相同Qwen2.5-7B-Instruct骨架、相同训练数据分别训练SFT、RL、OPD三个模型变体，排除骨架和数据分布的干扰，确保差异归因于后训练范式。
- 提出PosConf位置感知置信度策略：针对不同后训练模型的置信度可靠区间，仅在指定相对位置范围内提取、使用置信度信号，规避逆校准区域。

### 关键结果
在AIME2024/2025、AMC2023、MATH500四个数学推理benchmark上验证：
1. 三类后训练的置信度特性存在显著阶段差异：OPD的Pre-CoT难度预测AUROC平均达0.644，表现最优；SFT的Intra-CoT早期终止在30% token预算下，AIME2024精度提升8.06个点；RL的Post-CoT置信度聚合比多数投票平均高5.4个点。
2. PosConf策略效果显著：RL的答案聚合比多数投票提升6.1个点，OPD的低预算早期终止最高提升4.3个点。

### 核心结论
不同后训练范式的置信度可靠性是阶段依赖且位置相关的，需匹配对应场景使用而非全链路采用统一置信度策略

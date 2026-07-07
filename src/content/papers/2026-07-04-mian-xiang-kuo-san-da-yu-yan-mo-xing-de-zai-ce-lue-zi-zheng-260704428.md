---
title: 'dOPSD: On-Policy Self-Distillation for Diffusion Language Models'
title_zh: 面向扩散大语言模型的在策略自蒸馏方法dOPSD
authors:
- Phuong Tuan Dat
- Qi Li
- Xinchao Wang
affiliations:
- National University of Singapore
arxiv_id: '2607.04428'
url: https://arxiv.org/abs/2607.04428
pdf_url: https://arxiv.org/pdf/2607.04428
published: '2026-07-04'
collected: '2026-07-07'
category: Training
direction: 扩散大语言模型 · 在策略自蒸馏优化
tags:
- Diffusion LLM
- Self-Distillation
- On-Policy Training
- Reasoning
- LoRA
one_liner: 利用扩散大语言模型自身去噪轨迹作为特权信息，实现无外部参考的在策略自蒸馏提升推理性能
practical_value: '- 电商场景下用扩散LLM做广告文案、商品标题生成时，可复用dOPSD的轨迹自蒸馏思路，无需标注海量参考文案，仅用模型自身生成轨迹做监督，降低标注成本同时避免SFT的曝光偏差

  - 缺乏标注数据的个性化推荐/Agent对齐场景，可借鉴用模型自身中间状态作为特权信息的自蒸馏范式，无需额外大模型教师或奖励模型，大幅降低对齐成本

  - 多步生成类任务（如多轮Agent导购、长文案生成）中，可参考用后续更完备的生成状态反哺前面步骤训练的思路，提升中间决策的准确性

  - 业务中可搭配轻量结果校验（如文案点击率预筛、Agent执行结果校验），仅过滤正确轨迹做蒸馏，用极小成本进一步提升训练效果'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
扩散大语言模型（dLLM）具备并行解码、双向上下文优势，但后训练提升推理能力存在明显瓶颈：SFT是off-policy存在曝光偏差，RL类方法只有稀疏序列级奖励且dLLM缺乏可解析序列似度难以适配，传统OPSD依赖推理时不可用的外部参考作为特权信息，会坍塌为弱共识策略，无法有效提升dLLM推理能力。

### 方法关键点
- 无需外部参考，特权信息完全来自学生模型自身的去噪轨迹：采样真实解码中间步骤作为学生状态，用同一条轨迹后续更完整的解码状态作为教师的特权输入
- 教师目标为后续所有未解码步骤的预测分布平均，用token级Jensen-Shannon散度做蒸馏目标，无需修改模型架构，仅增加少量前向计算开销
- 可选引入轨迹校验机制，仅对最终结果正确的轨迹做蒸馏，避免错误轨迹放大偏差，无标注场景也可关闭校验直接蒸馏
- 训练采用LoRA参数高效微调，适配7B/8B级dLLM，训练成本低

### 关键结果
在Dream-7B、LLaDA-8B两个开源dLLM上验证，仅用数学推理数据集训练：域内GSM8K数学推理最高提升1.63个点，MATH500最高提升4.76个点；域外代码生成HumanEval最高提升4.17个点，MBPP最高提升1.06个点，所有指标均优于SFT、GRPO、传统OPSD等基线，且基线普遍出现性能下降或持平。

最值得记住的一句话：扩散模型的迭代去噪轨迹本身就是天然的特权信息源，无需外部标注即可构建密集、在策略的监督信号，有效提升模型能力。

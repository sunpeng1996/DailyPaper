---
title: Group Entropy-Controlled Policy Optimization
title_zh: 组熵控制的策略优化算法（GEPO）
authors:
- Guangran Cheng
- Chengqi Lyu
- Songyang Gao
- Wenwei Zhang
- Kai Chen
affiliations:
- Shanghai AI Laboratory
arxiv_id: '2607.16850'
url: https://arxiv.org/abs/2607.16850
pdf_url: https://arxiv.org/pdf/2607.16850
published: '2026-07-17'
collected: '2026-07-21'
category: Training
direction: LLM对齐 · 多任务RL训练优化
tags:
- GRPO
- Entropy Control
- RLHF
- Multi-task Training
- Policy Optimization
one_liner: GRPO轻量扩展，通过组级非对称优势塑形解决多任务RLHF异质性偏差
practical_value: '- 生成式推荐/推荐Agent多任务RL对齐时，可直接替换现有GRPO为GEPO，无额外采样成本，即可缓解跨任务优化不均衡问题

  - 多任务训练无需人工调任务权重，可复用GEPO的组熵自适应阈值思路，自动匹配不同任务的探索需求，避免简单任务梯度主导

  - 非对称优势塑形trick可直接复用：低熵任务衰减正优势防过拟合，高熵任务衰减负优势保探索，同时规避生成内容长度崩溃问题'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM多任务RL对齐范式（如GRPO）采用全局或token级熵控制，忽略不同任务天然的熵异质性，导致归一化优势存在熵依赖结构偏差：低熵任务梯度强且稳定，会主导训练进程；高熵任务梯度弱且噪声大，探索易被提前抑制，最终出现跨任务效果不均衡、训练振荡甚至后期崩溃的问题。
### 方法关键点
- 定义组熵：基于每个prompt对应的K个采样响应计算序列级熵，归一化到单token维度，无额外采样成本即可精准表征单任务的当前探索状态
- 非对称优势塑形：低熵组衰减正优势避免过 exploitation，高熵组衰减负优势保留探索空间；设置高熵衰减系数小于低熵，防止低熵组出现生成长度崩溃的病理现象
- 自适应熵阈值：基于每批组熵的均值和标准差计算动态阈值，用EMA平滑后使用，自动适配不同基座模型和训练阶段，无需任务级人工调参
### 关键实验
在Intern-S1-mini和Qwen3.5-9B两个基座上验证，覆盖数学、物理、代码、指令跟随等13个基准，对比GRPO、AEPO、Clip-Cov、KL-Cov等基线：GEPO在Intern-S1-mini上平均得分54.2，较最优基线高2.4分；在Qwen3.5-9B上平均得分71.2，较次优基线高0.3分，且训练全程无振荡或崩溃。
### 核心结论
多任务RL对齐中，保留不同任务的差异化探索水平，比强行统一所有任务的熵目标效果更优。

---
title: 'Sparse Hodge Preference Optimization: Fine-Tuning Language Models toward Alignment
  beyond Transitive Preferences'
title_zh: 稀疏霍奇偏好优化：突破传递性假设的LLM偏好对齐微调方法
authors:
- Yiming Liu
- Jianwei Ma
- Zhongwei Xing
- Tonghui Yu
affiliations:
- Harbin Institute of Technology
- Jinan University
- Peking University
arxiv_id: '2611.30135'
url: https://arxiv.org/abs/2611.30135
pdf_url: https://arxiv.org/pdf/2611.30135
published: '2026-11-23'
collected: '2026-11-24'
category: Training
direction: LLM对齐 · 偏好优化
tags:
- Preference Optimization
- DPO
- Hodge Decomposition
- LLM Alignment
- Sparse Estimation
one_liner: 基于霍奇分解为DPO添加稀疏反对称残差，突破传递性假设限制适配人类循环偏好
practical_value: '- 电商/Agent场景做LLM响应/推荐话术偏好对齐时，若遇到用户偏好循环（如不同场景下A>B、B>C、C>A），可在现有DPO流水线基础上叠加稀疏反对称curl头，新增参数不足10万，几乎不增加训练成本即可提升偏好匹配准确率

  - 多人群/多目标推荐的偏好融合场景中，遇到Condorcet循环（多数投票产生偏好环）时，可复用SHPO的设计思路：保留原有成熟的全局排序逻辑作为主信号，仅新增极少量稀疏参数拟合局部非传递偏好偏差，无需推翻现有架构

  - 偏好建模时可参考霍奇分解的信号拆分思路，将复杂偏好拆分为可全局排序的主信号、局部循环残差、全局拓扑残差三个分量，针对性建模降低整体复杂度'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
现有DPO等主流偏好优化方法基于Bradley-Terry模型的传递性假设，默认所有偏好可全局排序，无法拟合人类偏好中普遍存在的循环结构（如Condorcet悖论：3个及以上标注者投票易出现A≻B、B≻C、C≻A的偏好环），导致对齐效果无法匹配真实复杂的用户/标注者偏好。
### 方法关键点
- 基于组合霍奇分解将偏好流拆分为3个正交分量：梯度分量（对应可全局排序的传递性偏好，即DPO原生信号）、curl分量（对应局部循环偏好）、谐波分量（对应全局拓扑循环，全连接偏好图下为0可忽略）
- 新增稀疏反对称curl头拟合循环残差：用双线性映射构造满足反对称性的curl得分，对curl系数加L1正则化保证稀疏性，仅新增O(d*K)参数（d为骨干隐藏层维度，K为curl平面数，实验中K=8仅增5.7万参数）
- 端到端联合训练：原生DPO损失与curl残差损失联合反向传播，共享骨干网络梯度，保留DPO简单稳定的训练优势
### 关键实验
基于Qwen2.5-7B-Instruct做QLoRA微调，对比DPO、IPO、cDPO、rDPO、GPO共5个基线，在HH-RLHF、UltraFeedback、合成循环偏好3个数据集测试：
- 对比原生DPO，SHPO的偏好准确率accπ分别提升5.6、9.6、3.6个百分点；
- GPT-4o评测开放生成质量，SHPO平均得分6.31，显著高于DPO的5.11、GPO的5.89，头对头对比DPO胜率达57.1%（p<0.001）。
### 核心结论
人类偏好天然存在非传递性，偏好对齐无需追求全局一致排序，保留主流传递信号的同时用极小参数拟合局部循环残差即可大幅提升对齐效果。

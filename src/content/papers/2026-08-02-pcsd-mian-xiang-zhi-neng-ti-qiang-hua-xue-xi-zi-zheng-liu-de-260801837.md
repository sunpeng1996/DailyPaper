---
title: 'PCSD: Persistent Consistency for Self-Distillation in Agentic Reinforcement
  Learning'
title_zh: PCSD：面向智能体强化学习自蒸馏的持久一致性机制
authors:
- Chunji Lv
- Yangguang Wei
- Junlin Liu
- Yang Gao
- Ming Liu
- Xinming Wang
- Jinyang Wu
- Guoren Wang
- Changsheng Li
affiliations:
- Beijing Institute of Technology
- Meituan
- Institute of Automation, Chinese Academy of Sciences
- Tsinghua University
arxiv_id: '2608.01837'
url: https://arxiv.org/abs/2608.01837
pdf_url: https://arxiv.org/pdf/2608.01837
published: '2026-08-02'
collected: '2026-08-05'
category: Agent
direction: Agent强化训练 · 自蒸馏优化
tags:
- Agentic RL
- Self-Distillation
- GRPO
- Token-Level Weighting
- ALFWorld
one_liner: 提出基于局部信号持久度的token级自蒸馏权重机制，显著提升长序列Agent RL效果
practical_value: '- 电商导购/客服Agent的RL训练可直接复用PCSD权重方案，解决长轮次任务稀疏奖励下的credit assignment问题，比单点/整步加权更鲁棒

  - LLM4Rec、工具调用蒸馏等场景可借鉴「用局部信号持久度而非单点差判断教师可信度」的trick，有效降低噪声干扰

  - 电商购物类Agent训练可采用GRPO+PCSD联合优化框架，推理无需外挂特权技能，降低线上部署复杂度的同时提升任务成功率

  - 长序列生成蒸馏场景可复用自适应窗口设计：低方差区域用短窗口保细粒度，高方差区域用长窗口抗噪，平衡精度和鲁棒性'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
LLM Agent执行长轮次交互任务时，RL训练面临严重的奖励稀疏问题：单轨迹仅末尾有1个标量奖励，无法为中间token提供有效监督。On-policy自蒸馏（OPSD）通过带特权信息的教师模型提供token级密集监督，但现有方法要么用单点token差异易受噪声干扰，要么用整步统一权重忽略位置差异，始终存在精度和鲁棒性的权衡矛盾。

### 方法关键点
- 核心假设：教师对token的支持度如果在局部窗口内持续存在才是可信信号，单点突变大概率为噪声
- 自适应窗口聚合：根据教师-学生log概率差的局部方差动态选择窗口大小，低方差区域用短窗口保精度，高方差区域用长窗口抗噪；窗口内采用指数衰减加权，近邻token权重更高
- 趋势感知调制：对局部支持度呈下降趋势的位置衰减权重，过滤不稳定信号，最终通过sigmoid门控输出连续token级蒸馏权重，和GRPO的稀疏轨迹奖励联合优化

### 关键实验
在ALFWorld（具身交互）、WebShop（电商购物）两个基准上对比GRPO、SDAR等主流baseline：
1. Qwen2.5-3B backbone下，ALFWorld总体成功率达90.6%，超GRPO 15.6个百分点，超最优蒸馏baseline SDAR 6.2个百分点；WebShop得分85.0，Acc 67.2%和最优baseline持平
2.  unseen ALFWorld split上超GRPO 15.8个百分点，泛化性显著更强
3. 推理时无需外挂特权技能，能力完全内化到学生模型

> 最值得记住的结论：自蒸馏的token级可信度不看单点差异，看局部信号的持久一致性，这是平衡细粒度监督和抗噪性的核心。

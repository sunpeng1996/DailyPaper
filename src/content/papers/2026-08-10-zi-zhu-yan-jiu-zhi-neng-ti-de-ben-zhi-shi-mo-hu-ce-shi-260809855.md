---
title: Agentic Auto-Research is Fuzz Testing
title_zh: 自主研究智能体的本质是模糊测试
authors:
- Yifeng He
- Jicheng Wang
- Yinzhe Zhao
- Jiachen Liu
- Hao Chen
affiliations:
- University of California, Davis
- Zhejiang University
- ARA Lab
- The University of Hong Kong
arxiv_id: '2608.09855'
url: https://arxiv.org/abs/2608.09855
pdf_url: https://arxiv.org/pdf/2608.09855
published: '2026-08-10'
collected: '2026-08-11'
category: Agent
direction: 自主研究Agent · 反馈导向架构设计
tags:
- Autonomous Agent
- Fuzz Testing
- Feedback Directed Search
- Auto Research
- Validation
one_liner: 将自主研究智能体工作流映射为灰盒模糊测试，提出三层架构解决生成-排序范式反馈稀疏问题
practical_value: '- 做电商/推荐多轮迭代Agent时，可拆分评估为两部分：低成本中间信号（如用户点击意图、停留时长）引导Agent下一步动作，高成本业务评估（如GMV、留存）做最终校验，避免单指标过拟合

  - 生成式推荐候选生成环节，可借鉴模糊测试的反馈导向搜索逻辑：无需每次随机采样大量候选再排序，基于上一轮候选的中间反馈（如召回分、语义匹配度）做定向突变，提升高价值候选产出效率，降低推理成本

  - 做Agent效果评估时，必须保留独立的、不参与搜索过程的验证集/业务指标，避免优化过程中对中间信号的过拟合导致最终业务效果下降'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前自主研究Agent的主流「生成-排序」范式存在严重效率缺陷：大量生成候选后用打分模型或人工筛选，最终验证成本极高（专家评审、物理实验等），且问题解决率随采样量仅呈对数线性增长，边际收益快速下降，反馈稀疏成为核心瓶颈。

### 方法关键点
- 将自主研究Agent工作流完整映射为灰盒模糊测试的控制循环，提出三层核心架构：
  1. 低成本中间进展信号：每次实验输出认知进展量化值（如是否排除假设、是否缩小搜索边界），需满足廉价、与真实进展相关、抗优化作弊三个条件
  2. 反馈导向搜索：用中间信号指导下一步实验方向（突变高价值种子、优先探索未覆盖区域），而非仅对已完成候选排序
  3. 独立保护验证：中间信号仅用来引导搜索，最终有效性必须用未参与搜索过程的独立证据（如隐藏测试集、物理实验）校验，避免中间信号过拟合

### 关键结果数字
本文为立场论文，核心结论均基于已有公开实验结果：xmlwf分支约束求解任务上，反馈导向梯度方法比随机采样效果高19.6pp（97.0% vs 77.4%）；MLE-bench数据显示，用独立测试集选最优方案比用交叉验证代理指标高9-13pp的奖牌率。

### 核心记忆点
优化后的进展信号不能证明研究发现成立，就像模糊测试的覆盖率不能证明存在漏洞一样。

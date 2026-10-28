---
title: 'Your Policy Is Secretly a Harness: The Decision Geometry of Agent Interfaces'
title_zh: 策略隐式承载训练接口特征：Agent接口的决策几何分析
authors:
- Jian Mu
- Ruibo Shen
- Yao Shu
affiliations:
- The Hong Kong University of Science and Technology (Guangzhou)
- The Hong Kong University of Science and Technology
arxiv_id: '2610.37255'
url: https://arxiv.org/abs/2610.37255
pdf_url: https://arxiv.org/pdf/2610.37255
published: '2026-10-26'
collected: '2026-10-28'
category: Agent
direction: Agent 接口与策略迁移优化
tags:
- LLM Agent
- Harness
- Policy Transfer
- Decision Geometry
- Regularized RL
one_liner: 揭示Agent策略隐式编码训练接口偏好，提出天花板-失配度框架评估接口与策略适配性
practical_value: '- 迭代Agent的prompt/工具链/harness时，不要仅用固定权重的模型评估直接毙掉初始掉点的方案：若新接口天花板更高，仅需少量适配训练即可抵消初始失配带来的掉点，拿到更高最终收益，可直接复用在电商导购、客服Agent的工具链选型流程

  - 跨接口策略迁移掉点时可拆分三类错误定位问题：若为仅输入输出格式变化导致的「读出漂移」（最优决策完全不变），仅需做格式对齐或少量样本微调即可快速恢复性能，无需全量重训，可用于推荐系统Agent、广告投放Agent的接口迭代优化

  - 评估接口潜力时，可直接用更强的LLM作为最优代理计算该接口的天花板，再结合当前策略的失配度预测最终可达性能，比固定权重跑的准确率指标可靠度更高，可大幅降低Agent接口选型的试错成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前LLM Agent的接口（包含提示词、工具、控制逻辑，统称harness）迭代普遍采用固定训练好的模型评估性能，默认策略在不同接口下的知识可迁移，但实际常出现同一接口改动让基础模型涨点、微调后模型掉点的矛盾现象，业界缺乏对「策略从训练接口中学习到什么、换接口后哪些能力可保留」的量化分析框架。
### 方法关键点
- 理论层面：在KL正则化强化学习框架下证明，最优策略的动作对数几率完全还原训练接口对各动作的相对偏好权重，训练完成的策略会隐式编码训练接口的决策特征
- 收益拆分公式：部署收益 = 接口天花板（该接口下任何策略能达到的最优收益） - 策略失配度（策略偏离该接口最优决策带来的收益损失），训练仅改变失配度，换接口会同时影响两个项
- 迁移错误拆分：将跨接口迁移的误差拆分为目标偏移（新接口最优决策变化）、训练残差（原训练未达最优的误差）、读出漂移（仅接口格式变化导致的策略输出变化）三类
### 关键实验结果
- 实验覆盖MiniWoB++网页Agent任务、Terminal-Bench Lite编码Agent任务，底座模型采用Qwen3.5系列
- MiniWoB++上仅反转观测字段顺序（最优决策完全不变），训练好的模型任务成功率从85.0%暴跌至19.2%，掉点完全来自读出漂移
- 给接口新增批量点击功能时，固定权重评估初始掉点12.1%，经过等量适配训练后成功率反超原接口3.2个百分点
- 编码Agent任务上，用强模型作为最优代理计算的「天花板-失配度」与实际准确率的斯皮尔曼相关系数达1.0，单独用天花板或失配度的相关系数仅为0.7和-0.7
### 核心结论
不要用固定权重的模型评估新接口的潜力，高天花板的接口即使初始掉点，适配后往往能带来更高的最终收益
